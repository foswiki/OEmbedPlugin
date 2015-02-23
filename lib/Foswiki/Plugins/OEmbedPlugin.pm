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

package Foswiki::Plugins::OEmbedPlugin;

use strict;
use warnings;

use Foswiki::Func ();

our $VERSION = '5.10';
our $RELEASE = '23 Feb 2015';
our $SHORTDESCRIPTION = 'Easy embedding of third party content';
our $NO_PREFS_IN_TOPIC = 1;
our $core;

sub core {

  unless (defined $core) {
    require Foswiki::Plugins::OEmbedPlugin::Core;
    $core = new Foswiki::Plugins::OEmbedPlugin::Core();
  }

  return $core;
}


sub initPlugin {

  core->init;

  Foswiki::Func::registerTagHandler('OEMBED', sub { return core->EMBED(@_); });
  Foswiki::Func::registerTagHandler('EMBED', sub { return core->EMBED(@_); });

  Foswiki::Func::registerRESTHandler('purgeCache', sub { return core->purgeCache(@_); },
    authenticate => 0,
    validate => 0,
    http_allow => 'GET,POST',
  );

  Foswiki::Func::registerRESTHandler('provider', sub { return core->provider(@_); },
    authenticate => 0,
    validate => 0,
    http_allow => 'GET,POST',
  );

  return 1;
}


1;
