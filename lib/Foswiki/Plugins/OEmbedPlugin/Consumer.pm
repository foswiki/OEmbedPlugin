# Plugin for Foswiki - The Free and Open Source Wiki, http://foswiki.org/
#
# OEmbedPlugin is Copyright (C) 2013-2022 Michael Daum http://michaeldaumconsulting.com
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

package Foswiki::Plugins::OEmbedPlugin::Consumer;

use strict;
use warnings;

use Error qw(:try);
use Web::oEmbed ();
use Foswiki::Func ();
use Foswiki::Contrib::CacheContrib ();
our @ISA = qw( Web::oEmbed );

sub new {
  my $class = shift;

  my $this = bless($class->SUPER::new(@_), $class);

  my $workingDir = Foswiki::Func::getWorkArea('OEmbedPlugin');
  $this->{cacheRoot} = $workingDir . '/cache';
  $this->{cacheExpire} = "1 d";

  return $this;
}

sub embed {
  my ($this, $uri, $opt) = @_;

  my $url = $this->request_url($uri, $opt) or return;

  my $ua = Foswiki::Contrib::CacheContrib::getUserAgent();
  my $res = $ua->get($url);

  return unless defined $res;
  throw Error::Simple($res->status_line()) unless $res->is_success();  

  return Web::oEmbed::Response->new_from_response($res, $uri);
}

sub request_url {
  my ($self, $uri, $opt) = @_;

  my $provider = $self->provider_for($uri) or return;

  # SMELL: how to deal with provider interpreting standards differently
  if ($provider->{name} eq 'Vine') {
    my $api = $provider->{api};
    my $id = '';

    if ($uri =~ /.*\/(.*?)$/) {
      $id = $1;
      $api =~ s/%id%/$id/g;
    }

    return URI->new($api);
  }

  return $self->SUPER::request_url($uri, $opt);
}

sub _untaint {
  my $content = shift;
  if (defined $content && $content =~ /^(.*)$/s) {
    $content = $1;
  }
  return $content;
}

1;
