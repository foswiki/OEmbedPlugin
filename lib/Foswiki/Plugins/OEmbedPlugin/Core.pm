# Plugin for Foswiki - The Free and Open Source Wiki, http://foswiki.org/
#
# OEmbedPlugin is Copyright (C) 2013-2015 Michael Daum http://michaeldaumconsulting.com
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
use Foswiki::Plugins::OEmbedPlugin::Consumer ();
#use Data::Dump qw(dump);

use constant TRACE => 0;    # toggle me

sub writeDebug {
  print STDERR "OEmbedPlugin::Core - $_[0]\n" if TRACE;
}

sub new {
  my $class = shift;

  my $this = bless({@_}, $class);

  $this->{consumer} = Foswiki::Plugins::OEmbedPlugin::Consumer->new({format => 'json'});

  if (defined $Foswiki::cfg{OEmbedPlugin}{Providers}) {

    foreach my $provider (keys %{$Foswiki::cfg{OEmbedPlugin}{Providers}}) {
      #print STDERR "registering provider $provider\n";

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
          print STDERR "WARNING: no api key for embed.ly ... skipping\n";
          next;
        }
      }

      foreach $url (@urls) {
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

sub EMBED {
  my ($this, $session, $params, $theTopic, $theWeb) = @_;

  writeDebug("called EMBED()");

  my $url = $params->{_DEFAULT} || $params->{url};
  my $warn = Foswiki::Func::isTrue($params->{warn}, 1);
  unless ($url) {
    return "<span class='foswikiAlert'>ERROR: no url param</span>" if $warn;
    return "";
  }

  my $response = eval { $this->{consumer}->embed($url) };
  #writeDebug("response=".dump($response));
  if ($@) {
    print STDERR "ERROR: $@\n" if $warn;
  }

  unless (defined $response) {
    writeDebug("no response for $url");
    return $url;
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

    my $thumbnailUrl = $params->{thumbnail_url} || 'https://i.ytimg.com/vi/$vid/$quality.jpg';

    my $quality = $params->{quality} || "mqdefault";
    $quality .= 'default' if $quality =~ /^(mq|hq|sd|maxres)$/;

    my $vid = '';
    my $html = $response->html || '';
    if ($html =~ /www.youtube.com\/embed\/(.*)\?/) {
      $vid = $1;
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
    if (defined $origWidth && defined $origHeight) {
      my $ratio = $origWidth / $origHeight;
      if (defined $width && $width ne 'auto') {
        if (!defined $height || $height eq 'auto') {
          $height = $width / $ratio;
        }
      } else {
        if (defined $height && $height ne 'auto') {
          $width = $height * $ratio;
        }
      }
    }

    $width .= 'px' if defined $width && $width =~ /^[\d\.]+$/;
    $height .= 'px' if defined $height && $height =~ /^[\d\.]+$/;

    $height ||= '';
    $width ||= '';

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
      $result = '<literal>' . $result . '</literal>';
    }
  }

  unless ($result) {
    writeDebug("WARNING: Hm, can't render response from $url");
    return $url;
  }

  $result =~ s/\$(thumbnail_url|thumbnail_width|thumbnail_height|html|provider_url|provider_name|description|title|author_name|height|width|author_url|version|type|class)\b//g;

  return $result;
}

sub purgeCache {
  my $this = shift;

  $this->{consumer}->purgeCache;
}

1;
