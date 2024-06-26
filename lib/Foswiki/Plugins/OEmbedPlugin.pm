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

package Foswiki::Plugins::OEmbedPlugin;

use strict;
use warnings;

use Foswiki::Func ();

our $VERSION = '7.10';
our $RELEASE = '%$RELEASE%';
our $SHORTDESCRIPTION = 'Easy embedding of third party content';
our $LICENSECODE = '%$LICENSECODE%';
our $NO_PREFS_IN_TOPIC = 1;
our $core;

sub initPlugin {

  getCore()->init if defined $core;

  Foswiki::Func::registerTagHandler('OEMBED', sub { return getCore()->EMBED(@_); });
  Foswiki::Func::registerTagHandler('EMBED', sub { return getCore()->EMBED(@_); });
  Foswiki::Func::registerTagHandler('OEMBED_PROVIDER', sub { return getCore()->OEMBED_PROVIDER(@_); });

  Foswiki::Func::registerRESTHandler('provider', sub { return getCore()->provider(@_); },
    authenticate => 0,
    validate => 0,
    http_allow => 'GET,POST',
  );

  return 1;
}

sub getCore {

  unless (defined $core) {
    require Foswiki::Plugins::OEmbedPlugin::Core;
    $core = new Foswiki::Plugins::OEmbedPlugin::Core();
  }

  return $core;
}

1;
