# ---+ Extensions
# ---++ OEmbedPlugin
# This is the configuration used by the <b>OEmbedPlugin</b>.

# **STRING**
# To use embed.ly as an oEmbed gateway, you'll have to register and copy-paste the api-key in here.
# Otherwise embed.ly providers won't be available.
$Foswiki::cfg{OEmbedPlugin}{EmbedlyKey} = '';

# **PERL**
# List of providers and their oEmbed API endpoints.
# See http://oembed.com/ and http://embed.ly for more.
$Foswiki::cfg{OEmbedPlugin}{Providers} = {
  '23HQ' => {
    url => 'http://www.23hq.com/*/photo/*',
    api => 'http://www.23hq.com/23/oembed',
  },

  'AlphaAppNet' => {
    url => [
      'https://alpha.app.net/*/post/*',
      'https://photos.app.net/*/*',
    ],
    api => 'https://alpha-api.app.net/oembed',
  },

  'amChartsLiveEditor' => {
    url => [
      'http://live.amcharts.com/*',
      'https://live.amcharts.com/*',
    ],
    api => 'https://live.amcharts.com/oembed',
    params => {
      format => 'json'
    },
  },

  'Animoto' => {
    url => 'http://animoto.com/play/*',
    api => 'http://animoto.com/oembeds/create',
    params => {
      format => 'json'
    },
  },

  'AudioSnaps' => {
    url => [
      'http://audiosnaps.com/k/*',
      'https://audiosnaps.com/k/*',
    ],
    api => 'http://audiosnaps.com/service/oembed',
  },

  'BlipTV' => {
    url => 'http://*.blip.tv/*',
    api => 'http://blip.tv/oembed/',
  },

  'Cacoo' => {
    url => 'https://cacoo.com/diagrams/*',
    api => 'https://cacoo.com/oembed.json',
  },

  'ChartBlocks' => {
    url => [
      'http://public.chartblocks.com/c/*',
      'https://public.chartblocks.com/c/*',
    ],
    api => 'http://embed.chartblocks.com/1.0/oembed',
    params => {
      format => 'json'
    },
  },

  'chirbit' => {
    url => 'http://chirb.it/*',
    api => 'http://chirb.it/oembed.json',
  },

  'CircuitLab' => {
    url => 'https://www.circuitlab.com/circuit/*',
    api => 'https://www.circuitlab.com/circuit/oembed/',
  },

  'Clyp' => {
    url => [
      'http://clyp.it/*',
      'http://clyp.it/playlist/*',
    ],
    api => 'http://api.clyp.it/oembed/',
  },

  'CollegeHumor' => {
    url => 'http://www.collegehumor.com/video/*',
    api => 'http://www.collegehumor.com/oembed.json',
  },

  'Coub' => {
    url => [
      'http://coub.com/embed/*',
      'http://coub.com/view/*',
    ],
    api => 'http://coub.com/api/oembed.json',
  },

  'CrowdRanking' => {
    url => 'http://crowdranking.com/*/*',
    api => 'http://crowdranking.com/api/oembed.json',
  },

  'DailyMile' => {
    url => 'http://www.dailymile.com/people/*/entries/*',
    api => 'http://api.dailymile.com/oembed',
    params => {
      format => 'json'
    },
  },

  'Dailymotion' => {
    url => 'http://*.dailymotion.com/*',
    api => 'http://www.dailymotion.com/api/oembed/',
  },

  'Deviantart.com' => {
    url => [
      'http://*.deviantart.com/*#/d*',
      'http://*.deviantart.com/art/*',
      'http://fav.me/*',
      'http://sta.sh/*',
    ],
    api => 'http://backend.deviantart.com/oembed',
  },

  'Dipity' => {
    url => 'http://www.dipity.com/*/*/',
    api => 'http://www.dipity.com/oembed/timeline/',
  },

  'Dotsub' => {
    url => 'http://dotsub.com/view/*',
    api => 'http://dotsub.com/services/oembed',
  },

  'edocr' => {
    url => [
      'http://*.edocr.com/doc/*',
      'https://*.edocr.com/doc/*',
    ],
    api => 'http://edocr.com/api/oembed',
  },

  'Embedly' => {
    url => [
      'http://*.amazon.com/*',
      'http://*.amazon.de/*',
      'http://*.clipfish.de/*',
      'http://*.imdb.com/*',
      'http://*.screencast.com/*',
      'http://bcove.me/*',
      'http://goo.gl/maps/*',
      'http://twitpic.com/*',
      'http://www.washingtonpost.com/*',
      'https://foursquare.com/*',
      'https://maps.google.com/maps/*',
    ],
    api => 'http://api.embed.ly/1/oembed',
  },

  "Facebook(Video)" => {
    api => "https://www.facebook.com/plugins/video/oembed.json",
    url => [
      "https://www.facebook.com/*/videos/*",
      "https://www.facebook.com/video.php",
    ],
  },

  'Flickr' => {
    url => 'http://*.flickr.com/*',
    api => 'http://www.flickr.com/services/oembed/',
  },

  'FunnyOrDie' => {
    url => 'http://www.funnyordie.com/videos/*',
    api => 'http://www.funnyordie.com/oembed.json',
  },

  'GeographBritainandIreland' => {
    url => [
      'http://*.geograph.co.uk/*',
      'http://*.geograph.ie/*',
      'http://*.geograph.org.uk/*',
      'http://*.wikimedia.org/*_geograph.org.uk_*',
    ],
    api => 'http://api.geograph.org.uk/api/oembed',
  },

  'GeographChannelIslands' => {
    url => [
      'http://*.channel.geographs.org/*',
      'http://*.geograph.org.gg/*',
      'http://*.geograph.org.je/*',
      'http://channel-islands.geograph.org/*',
      'http://channel-islands.geographs.org/*',
    ],
    api => 'http://www.geograph.org.gg/api/oembed',
  },

  'GeographGermany' => {
    url => [
      'http://geo-en.hlipp.de/*',
      'http://geo.hlipp.de/*',
      'http://germany.geograph.org/*',
    ],
    api => 'http://geo.hlipp.de/restapi.php/api/oembed',
  },

  'GettyImages' => {
    url => 'http://gty.im/*',
    api => 'http://embed.gettyimages.com/oembed',
  },

  'GMEP' => {
    url => 'https://gmep.org/media/*',
    api => 'https://gmep.org/oembed.json',
  },

  'HuffDuffer' => {
    url => 'http://huffduffer.com/*/*',
    api => 'http://huffduffer.com/oembed',
    params => {
      format => 'json'
    },
  },

  'Hulu' => {
    url => 'http://www.hulu.com/watch/*',
    api => 'http://www.hulu.com/api/oembed.json',
  },

  'iFixit' => {
    url => 'http://www.ifixit.com/*',
    api => 'http://www.ifixit.com/Embed',
  },

  'IFTTT' => {
    url => [
      'http://ifttt.com/recipes/*',
      'https://ifttt.com/recipes/*',
    ],
    api => 'http://www.ifttt.com/oembed/',
  },

  'Infogram' => {
    url => 'https://infogr.am/*',
    api => 'https://infogr.am/oembed',
  },

  'Instagram' => {
    url => [
      'http://instagr.am/p/*',
      'http://instagram.com/p/*',
    ],
    api => 'http://api.instagram.com/oembed',
  },

  'Kickstarter' => {
    url => 'http://www.kickstarter.com/projects/*',
    api => 'http://www.kickstarter.com/services/oembed',
  },

  'Meetup' => {
    url => [
      'http://meetu.ps/*',
      'http://meetup.com/*',
      'http://www.meetup.com/*',
    ],
    api => 'https://api.meetup.com/oembed',
  },

  'MixCloud' => {
    url => [
      'http://*.mixcloud.com/*',
      'https://*.mixcloud.com/*',
    ],
    api => 'http://www.mixcloud.com/oembed/',
    params => {
      format => 'json'
    },
  },

  'MobyPicture' => {
    url => [
      'http://moby.to/*',
      'http://mobypicture.com/user/*/view/*',
      'http://www.mobypicture.com/user/*/view/*',
    ],
    api => 'http://api.mobypicture.com/oEmbed',
    params => {
      format => 'json'
    },
  },

  'nfb' => {
    url => 'http://*.nfb.ca/film/*',
    api => 'http://www.nfb.ca/remote/services/oembed/',
  },

  'OfficialFM' => {
    url => [
      'http://official.fm/playlists/*',
      'http://official.fm/tracks/*',
    ],
    api => 'http://official.fm/services/oembed.json',
  },

  'OnAol' => {
    url => 'http://on.aol.com/*',
    api => 'http://on.aol.com/api',
  },

  'PollDaddy' => {
    url => [
      'http://*.polldaddy.com/poll/*',
      'http://*.polldaddy.com/ratings/*',
      'http://*.polldaddy.com/s/*',
    ],
    api => 'http://polldaddy.com/oembed/',
    params => {
      format => 'json'
    },
  },

  'PollEverywhere' => {
    url => [
      'http://www.polleverywhere.com/free_text_polls/*',
      'http://www.polleverywhere.com/multiple_choice_polls/*',
      'http://www.polleverywhere.com/polls/*',
    ],
    api => 'http://www.polleverywhere.com/services/oembed/',
  },

  'Portfolium' => {
    url => [
      'https://portfolium.com/entry/*',
    ],
    api => 'https://api.portfolium.com/oembed',
  },

  'Quiz.biz' => {
    url => 'http://www.quiz.biz/quizz*',
    api => 'http://www.quiz.biz/api/oembed',
  },

  'Quizz.biz' => {
    url => 'http://www.quizz.biz/quizz-*.html',
    api => 'http://www.quizz.biz/api/oembed',
  },

  'RapidEngage' => {
    url => 'https://rapidengage.com/s/*',
    api => 'https://rapidengage.com/api/oembed',
  },

  'Rdio' => {
    url => [
      'http://*.rdio.com/artist/*',
      'http://*.rdio.com/people/*',
    ],
    api => 'http://www.rdio.com/api/oembed/',
  },

  'ReverbNation' => {
    url => [
      'https://www.reverbnation.com/*',
      'https://www.reverbnation.com/*/songs/*',
    ],
    api => 'https://www.reverbnation.com/oembed',
  },

  'Roomshare' => {
    url => [
      'http://roomshare.jp/en/post/*',
      'http://roomshare.jp/post/*',
    ],
    api => 'http://roomshare.jp/en/oembed.json',
  },

  'SapoVideos' => {
    url => 'http://videos.sapo.pt/*',
    api => 'http://videos.sapo.pt/oembed',
    params => {
      format => 'json'
    },
  },

  'Screenr' => {
    url => 'http://*.screenr.com/*',
    api => 'http://www.screenr.com/api/oembed.json',
  },

  'Scribd' => {
    url => 'http://*.scribd.com/*',
    api => 'http://www.scribd.com/services/oembed',
  },

  'ShortNote' => {
    url => 'https://www.shortnote.jp/view/notes/*',
    api => 'https://www.shortnote.jp/oembed/',
  },

  'Shoudio' => {
    url => [
      'http://shoud.io/*',
      'http://shoudio.com/*',
    ],
    api => 'http://shoudio.com/api/oembed',
    params => {
      format => 'json'
    },
  },

  'Sketchfab' => {
    url => [
      'http://sketchfab.com/*/folders/*',
      'http://sketchfab.com/models/*',
      'http://sketchfab.com/show/*',
      'https://sketchfab.com/*/folders/*',
      'https://sketchfab.com/models/*',
      'https://sketchfab.com/show/*',
    ],
    api => 'http://sketchfab.com/oembed',
  },

  'SlideShare' => {
    url => [
      'http://www.slideshare.net/*/*',
      'https://www.slideshare.net/*/*',
    ],
    api => 'https://www.slideshare.net/api/oembed/2',
  },

  'SoundCloud' => {
    url => [
      'http://soundcloud.com/*',
      'http://www.soundcloud.com/*',
      'https://soundcloud.com/*',
      'https://www.soundcloud.com/*',
    ],
    api => 'http://soundcloud.com/oembed',
    params => {
      format => 'json'
    },
  },

  'SpeakerDeck' => {
    url => 'https://speakerdeck.com/*',
    api => 'https://speakerdeck.com/oembed.json',
  },

  'Ted' => {
    url => 'http://www.ted.com/talks/*',
    api => 'http://www.ted.com/talks/oembed.json',
  },

  'Ustream' => {
    url => [
      'http://*.ustream.com/*',
      'http://*.ustream.tv/*',
    ],
    api => 'http://www.ustream.tv/oembed',
  },

  'Viddler' => {
    url => 'http://www.viddler.com/v/*',
    api => 'http://www.viddler.com/oembed/',
  },

  'VideoJug' => {
    url => [
      'http://www.videojug.com/film/*',
      'http://www.videojug.com/interview/*',
    ],
    api => 'http://www.videojug.com/oembed.json',
  },

  'Vimeo' => {
    url => [
      'http://vimeo.com/*',
      'http://vimeo.com/groups/*/videos/*',
      'https://vimeo.com/*',
      'https://vimeo.com/groups/*/videos/*',
    ],
    api => 'https://vimeo.com/api/oembed.json',
  },

  'Vine' => {
    url => [
      'http://vine.co/v/*',
      'http://www.vine.co/v/*',
      'https://vine.co/v/*',
      'https://www.vine.co/v/*',
    ],
    api => 'https://vine.co/oembed/%id%.json',
  },

  'WordPress.com' => {
    url => 'http://*.wordpress.com',
    api => 'http://public-api.wordpress.com/oembed/',
    params => {
      for => 'foswiki'
    },
  },

  'YFrog' => {
    url => [
      'http://*.yfrog.com/*',
      'http://yfrog.us/*',
    ],
    api => 'http://www.yfrog.com/api/oembed',
  },

  'YouTube' => {
    url => [
      'http://*.youtube.com/*',
      'https://*.youtube.com/*',
    ],
    api => 'https://www.youtube.com/oembed',
  },
};


1;
