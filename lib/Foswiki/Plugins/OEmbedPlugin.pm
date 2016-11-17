# Plugin for Foswiki - The Free and Open Source Wiki, http://foswiki.org/
#
# OEmbedPlugin is Copyright (C) 2013-2016 Michael Daum http://michaeldaumconsulting.com
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

our $VERSION = '5.30';
our $RELEASE = '17 Nov 2016';
our $SHORTDESCRIPTION = 'Easy embedding of third party content';
our $NO_PREFS_IN_TOPIC = 1;
our $core;

sub initPlugin {

  getCore()->init if defined $core;

  Foswiki::Func::registerTagHandler('OEMBED', sub { return getCore()->EMBED(@_); });
  Foswiki::Func::registerTagHandler('EMBED', sub { return getCore()->EMBED(@_); });

  Foswiki::Func::registerRESTHandler('purgeCache', sub { return getCore()->purgeCache(@_); },
    authenticate => 0,
    validate => 0,
    http_allow => 'GET,POST',
  );

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
