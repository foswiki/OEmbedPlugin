# Plugin for Foswiki - The Free and Open Source Wiki, http://foswiki.org/
#
# OEmbedPlugin is Copyright (C) 2013-2024 Michael Daum http://michaeldaumconsulting.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details, published at
# http://www.gnu.org/copyleft/gpl.html

package Foswiki::Plugins::OEmbedPlugin::Core;

use strict;
use warnings;

use Foswiki::Func ();
use Error qw(:try);
use HTTP::Request ();
use Foswiki::Plugins::OEmbedPlugin::Consumer ();
use Foswiki::Contrib::CacheContrib ();

use constant TRACE => 0;    # toggle me

sub new {
  my $class = shift;

  my $this = bless({@_}, $class);

  $this->{consumer} = Foswiki::Plugins::OEmbedPlugin::Consumer->new({format => 'json'});

  if (defined $Foswiki::cfg{OEmbedPlugin}{Providers}) {

    foreach my $provider (keys %{$Foswiki::cfg{OEmbedPlugin}{Providers}}) {
      #_writeDebug("registering provider $provider");

      my $url = $Foswiki::cfg{OEmbedPlugin}{Providers}{$provider}{url};
      my $api = $Foswiki::cfg{OEmbedPlugin}{Providers}{$provider}{api};
      my $regexp = $Foswiki::cfg{OEmbedPlugin}{Providers}{$provider}{regexp};
      my $params = $Foswiki::cfg{OEmbedPlugin}{Providers}{$provider}{params} || {};

      my @urls;
      if (ref($url) eq 'ARRAY') {
        @urls = @$url;
      } else {
        push @urls, $url;
      }

      if ($provider eq 'Embedly') {
        if ($Foswiki::cfg{OEmbedPlugin}{EmbedlyKey}) {
          $params->{key} = $Foswiki::cfg{OEmbedPlugin}{EmbedlyKey};
        } else {
          #print STDERR "WARNING: no api key for embed.ly ... skipping\n";
          next;
        }
      }

      foreach my $url (@urls) {
        $this->{consumer}->register_provider({
            name => $provider,
            url => $url,
            regexp => $regexp,
            api => $api,
            params => $params,
          }
        );
      }
    }
  }

  $this->init();

  return $this;
}

sub init {
  my $this = shift;

  $this->{_doneReadTemplate} = 0;
}

sub provider {
  my $this = shift;

  return "" unless defined $Foswiki::cfg{OEmbedPlugin}{Providers};

  foreach my $provider (sort {lc($a) cmp lc($b)} keys %{$Foswiki::cfg{OEmbedPlugin}{Providers}}) {
    my $url = $Foswiki::cfg{OEmbedPlugin}{Providers}{$provider}{url};
    my $api = $Foswiki::cfg{OEmbedPlugin}{Providers}{$provider}{api};
    my $regexp = $Foswiki::cfg{OEmbedPlugin}{Providers}{$provider}{regexp};
    my $params = $Foswiki::cfg{OEmbedPlugin}{Providers}{$provider}{params};

    print "'$provider' => {\n";
    print "  url => ";

    if (ref $url) {
      $url = "[\n    '" . join("',\n    '", sort @$url) . "',\n  ]";
    } else {
      $url = "'$url'";
    }

    print "$url,\n";
    print "  api => '$api',\n";
    print "  regexp => '$regexp'\n" if defined $regexp;

    if ($params) {
      print "  params => {\n";
      foreach my $key (sort keys %$params) {
        print "    $key => '$params->{$key}'\n";
      }
      print "  },\n";
    }


    print "},\n\n";
  }
}

sub expandTemplate {
  my ($this, $tmpl) = @_;

  unless ($this->{_doneReadTemplate}) {
    $this->{_doneReadTemplate} = 1;
    Foswiki::Func::readTemplate("oembed");
  }

  return Foswiki::Func::expandTemplate($tmpl);
}

#use Data::Dump qw(dump);
sub EMBED {
  my ($this, $session, $params, $topic, $web) = @_;

  #_writeDebug("called EMBED()");

  my $url = $params->{_DEFAULT} || $params->{url};
  my $warn = Foswiki::Func::isTrue($params->{warn}, 1);
  unless ($url) {
    return "<span class='foswikiAlert'>ERROR: no url param</span>" if $warn;
    return "";
  }
  my ($theWeb, $theTopic) = Foswiki::Func::normalizeWebTopicName($web, $params->{topic}||$topic);

  my $response;
  my $error;

  try {
    _writeDebug("loading url $url");
    $response = $this->{consumer}->embed($url);
    #_writeDebug("response=".dump($response));
  } catch Error with {
    $error = shift;
  };

  if (defined $error) {
    #print STDERR "ERROR: $error\n";
    $error =~ s/ at \/.*$//;
    return $warn ? "<span class='foswikiAlert'>$error</span>" : "";
  }

  unless (defined $response) {
    _writeDebug("no response for $url");
    return "<span class='foswikiAlert'>no response from url</span>" if $warn;
  }

  $response->web_page($url);    # SMELL: hook in the orig url

  my $format = $params->{format};
  my $template = $params->{template};
  $format = $this->expandTemplate($template) if defined $template;

  my $providerName = $response->provider_name || '';
  unless (defined $format) {
    $format = $this->expandTemplate($providerName);
    $format = undef unless $format;
  }

  my $result;

  if ($providerName eq "YouTube") {

    my $vid = '';
    my $html = $response->html || '';
    _writeDebug("html=$html");
    if ($html =~ /www.youtube.com\/embed\/(.*?)\?/) {
      $vid = $1;
    }
    _writeDebug("vid=$vid");

    my $thumbnailUrl = $params->{thumbnail_url} || 'https://img.youtube.com/vi/$vid/$quality.jpg';
    _writeDebug("thumbnailUrl=$thumbnailUrl");

    my $quality = $params->{quality};
    if (defined $quality && $quality ne "" && $quality ne 'auto') {
      $quality .= 'default' if $quality =~ /^(mq|hq|sd|maxres)$/;
    } else {
      foreach my $q (qw(maxresdefault hqdefault mqdefault sddefault default)) {
        my $tmp = $thumbnailUrl;
        $tmp =~ s/\$quality/$q/g;
        $tmp =~ s/\$vid/$vid/g;
        if ($this->urlExists($tmp)) {
          $quality = $q;
          last;
        }
      }
    }

    if ($format) {
      $format =~ s/\$thumbnail_url/$thumbnailUrl/g;
      $format =~ s/\$quality/$quality/g;
      $format =~ s/\$vid\b/$vid/g;
    }
  }

  if (defined $format) {
    my $data = $response->data();
    $result = $format;

    my $class = $params->{class} || '';
    my $width = $params->{width};
    my $height = $params->{height};
    my $origWidth = $response->width;
    my $origHeight = $response->height;

    if ($origWidth && $origHeight) {
      my $ratio = $origWidth / $origHeight;

      if ($origWidth < 400) { # TODO: make min width configurable
        $origWidth = 400;
        $origHeight = $origWidth / $ratio;
      }

      if (defined $width && $width ne 'auto') {
        if (!defined $height || $height eq 'auto') {
          $height = $width / $ratio;
        }
      } elsif ($height && $height ne 'auto') {
        $width = $height * $ratio;
      } else {
        $width ||= $origWidth;
        $height ||= $origHeight;
      }
    }

    $width .= 'px' if defined $width && $width =~ /^[\d\.]+$/;
    $height .= 'px' if defined $height && $height =~ /^[\d\.]+$/;

    $height = 'auto' unless defined $height;
    $width = 'auto' unless defined $height;

    $result =~ s/\$url\b/$url/g;    # ... if left over
    $result =~ s/\$class\b/$class/g;
    $result =~ s/\$height\b/$height/g;
    $result =~ s/\$width\b/$width/g;

    while (my ($key, $val) = each %$data) {
      next unless defined $val;
      $val =~ s/^<!\[CDATA\[([^]+]*)\]\]>$/$1/;
      $val = $params->{$key} if defined $params->{$key};
      $result =~ s/\$$key\b/$val/g;
    }

    $result = Foswiki::Func::decodeFormatTokens($result);
  } else {
    $result = $response->render();
    if (defined $result) {
      $result =~ s/\bwidth="\d+"/width="$params->{width}"/g if defined $params->{width};
      $result =~ s/\bheight="\d+"/height="$params->{height}"/g if defined $params->{height};
      $result = '<literal>' . $result . '</literal>';
    }
  }

  unless ($result) {
    _writeDebug("WARNING: Hm, can't render response from $url");
    return $url;
  }

  $result =~ s/\$topic/$theTopic/g;
  $result =~ s/\$web/$theWeb/g;

  $result =~ s/\$(thumbnail_url|thumbnail_width|thumbnail_height|html|provider_url|provider_name|description|title|author_name|height|width|author_url|version|type|class)\b//g;

  return $result;
}

sub OEMBED_PROVIDER {
  my ($this, $session, $params, $topic, $web) = @_;

  my $id = $params->{_DEFAULT} || $params->{id};
  my $format = $params->{format} || '   1 [[$provider][$name]]';
  my $header = $params->{header} // '';
  my $footer = $params->{footer} // '';
  my $sep = $params->{separator} // '$n';
  my $include = $params->{include};
  my $exclude = $params->{exclude};
  my $exampleFormat = $params->{exampleformat} // '$url';
  my $exampleHeader = $params->{exampleheader} // '';
  my $exampleFooter = $params->{examplefooter} // '';
  my $exampleSep = $params->{exampleseparator} // ', ';
  my @result = ();

  my @ids = ();
  if (defined $id) {
    push @ids, $id if defined $Foswiki::cfg{OEmbedPlugin}{Providers}{$id};
  } else {
    @ids = keys %{$Foswiki::cfg{OEmbedPlugin}{Providers}};
  }

  foreach my $name (sort @ids) {
    next if $include && $name !~ /$include/;
    next if $exclude && $name =~ /$exclude/;

    my $rec = $Foswiki::cfg{OEmbedPlugin}{Providers}{$name};

    my @examples = ();
    if ($rec->{examples}) {
      foreach my $example (sort @{$rec->{examples}}) {
        my $exline = $exampleFormat;
        $exline =~ s/\$url\b/$example/g;
        push @examples, $exline;
      }
    }
    my $examples = @examples ? $exampleHeader.join($exampleSep, @examples).$exampleFooter:"";
    
    my $line = $format;
    $line =~ s/\$examples\b/$examples/g;
    $line =~ s/\$name\b/$name/g;
    $line =~ s/\$url\b/join(", ", @{$rec->{url}})/ge;
    $line =~ s/\$api\b/$rec->{api}/g;
    $line =~ s/\$provider\b/$rec->{provider}/g;

    push @result, $line if $line ne "";;
  }

  return "" unless @result;
  return Foswiki::Func::decodeFormatTokens($header.join($sep, @result).$footer);
}

sub urlExists {
  my ($this, $url) = @_;

  _writeDebug("called urlExists($url)");

  my $request = HTTP::Request->new(HEAD => $url);
  my $ua = Foswiki::Contrib::CacheContrib::getUserAgent("oembed");
  my $res = $ua->request($request);

  return $res->is_success ? 1 : 0;
}

sub _writeDebug {
  print STDERR "OEmbedPlugin::Core - $_[0]\n" if TRACE;
}

1;
