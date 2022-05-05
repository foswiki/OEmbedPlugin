# ---+ Extensions
# ---++ OEmbedPlugin
# This is the configuration used by the <b>OEmbedPlugin</b>.

# **STRING**
# To use embed.ly as an oEmbed gateway, you'll have to register and copy-paste the api-key in here.
# Otherwise embed.ly providers won't be available.
$Foswiki::cfg{OEmbedPlugin}{EmbedlyKey} = '';

# **NUMBER**
$Foswiki::cfg{OEmbedPlugin}{CacheExpire} = 3600;

# **PERL**
# List of providers and their oEmbed API endpoints.
# See http://oembed.com/ and http://embed.ly for more.
$Foswiki::cfg{OEmbedPlugin}{Providers} = { 
  "23HQ" => {
    api => "http://www.23hq.com/23/oembed",
    examples => ["http://www.23hq.com/mprove/photo/13297717"],
    provider => "http://www.23hq.com",
    url => ["http://www.23hq.com/*/photo/*"],
  },
  "Abraia" => {
    api => "https://api.abraia.me/oembed",
    examples => ["https://store.abraia.me/demo/videos/sample/index.html"],
    provider => "https://abraia.me",
    url => ["https://store.abraia.me/*"],
  },
  "Adways" => {
    api => "http://play.adpaths.com/oembed/*",
    provider => "http://www.adways.com",
    url => ["http://play.adpaths.com/experience/*"],
  },
  "AlphaAppNet" => {
    api => "https://alpha-api.app.net/oembed",
    examples => ["https://alpha.app.net/breakingnews/post/9153521"],
    provider => "https://alpha.app.net/browse/posts/",
    url => ["https://alpha.app.net/*/post/*", "https://photos.app.net/*/*",],
  },
  "Altru" => {
    api => "https://api.altrulabs.com/social/oembed",
    examples => ["https://app.altrulabs.com/talentbrand/feed?answer_id=2059"],
    provider => "https://www.altrulabs.com",
    url => ["https://app.altrulabs.com/*/*?answer_id=*"],
  },
  "amChartsLiveEditor" => {
    api => "https://live.amcharts.com/oembed",
    examples => [
      "http://live.amcharts.com/czNjJ/",
      "http://live.amcharts.com/czNjJ/",
    ],
    params => {format => "json"},
    provider => "https://live.amcharts.com/",
    url => ["http://live.amcharts.com/*", "https://live.amcharts.com/*"],
  },
  "Animatron" => {
    api => "https://animatron.com/oembed/json",
    examples => [
      "https://www.animatron.com/project/6487dd52e5835971c6bec25d",
      "https://www.animatron.com/project/6487dd52e5835971c6bec25d",
    ],
    provider => "https://www.animatron.com/",
    url => [
      "https://www.animatron.com/project/*",
      "https://animatron.com/project/*",
    ],
  },
  "Animoto" => {
    api => "http://animoto.com/oembeds/create",
    examples => ["http://animoto.com/play/JzwsBn5FRVxS0qoqcBP5zA"],
    params => {format => "json"},
    provider => "http://animoto.com/",
    url => ["http://animoto.com/play/*"],
  },
  "Apester" => {
    api => "https://display.apester.com/oembed",
    params => {iframe_preview => "true", preview => "true"},
    provider => "https://www.apester.com",
    url => [
      "https://renderer.apester.com/v2/*?preview=true&iframe_preview=true",
    ],
  },
  "Archivos" => {
    api => "https://app.archivos.digital/oembed/",
    examples => ["https://app.archivos.digital/app/view/709/?embed"],
    provider => "https://app.archivos.digital",
    url => ["https://app.archivos.digital/app/view/*"],
  },
  "Audioboom" => {
    api => "https://audioboom.com/publishing/oembed/v4.{format}",
    examples => [
      "https://audioboom.com/channels/4971939",
      "https://audioboom.com/channels/4971939",
      "https://audioboom.com/posts/7193185-stephen-merchant",
      "https://audioboom.com/posts/7193185-stephen-merchant",
    ],
    provider => "https://audioboom.com",
    url =>
        ["https://audioboom.com/channel/*", "https://audioboom.com/posts/*",],
  },
  "AudioClip" => {
    api => "https://audioclip.naver.com/oembed",
    examples => [
      "https://audioclip.naver.com/channels/70/clips/25",
      "https://audioclip.naver.com/audiobooks/FE8C3FCBB6",
      "https://audioclip.naver.com/channels/70/clips/25",
      "https://audioclip.naver.com/audiobooks/FE8C3FCBB6",
    ],
    params => {format => "json"},
    provider => "https://audioclip.naver.com",
    url => [
      "https://audioclip.naver.com/channels/*/clips/*",
      "https://audioclip.naver.com/audiobooks/*",
    ],
  },
  "Audiomack" => {
    api => "https://www.audiomack.com/oembed",
    examples => ["https://www.audiomack.com/playlist/audiomack/just-chillin"],
    params => {format => "json"},
    provider => "https://www.audiomack.com",
    url => [
      "https://www.audiomack.com/song/*",
      "https://www.audiomack.com/album/*",
      "https://www.audiomack.com/playlist/*",
    ],
  },
  "AudioSnaps" => {
    api => "http://audiosnaps.com/service/oembed",
    examples =>
        ["http://audiosnaps.com/k/d8wi/", "http://audiosnaps.com/k/d8wi/",],
    params => {format => "json"},
    provider => "http://audiosnaps.com",
    url => ["http://audiosnaps.com/k/*"],
  },
  "Avocode" => {
    api => "https://stage-embed.avocode.com/api/oembed",
    examples => [
      "https://app.avocode.com/view/a851fc49602446be8c1ef6e5dc3845d8/33250729/comments/",
    ],
    params => {format => "json"},
    provider => "https://www.avocode.com/",
    url => ["https://app.avocode.com/view/*/_/comments/"],
  },
  "Backtracks" => {
    api => "https://backtracks.fm/oembed",
    examples => [
      "https://backtracks.fm/ycombinator/ycombinator/e/4-elon-musk-on-how-to-build-the-future",
    ],
    params => {format => "json"},
    provider => "https://backtracks.fm",
    url => [
      "https://backtracks.fm/*/*/e/*", "https://backtracks.fm/*",
      "http://backtracks.fm/*",
    ],
  },
  "Beautiful.AI" => {
    api => "https://www.beautiful.ai/api/oembed",
    examples => [
      "https://www.beautiful.ai/deck/-L7QETWHKx_3vn8eIswg",
      "https://www.beautiful.ai/player/-L7QHgT26tkTPnqtB84U",
    ],
    provider => "https://www.beautiful.ai/",
    url => "https://www.beautiful.ai/*",
  },
  "Blackfire.io" => {
    api => "https://blackfire.io/oembed",
    examples => [
      "https://blackfire.io/profiles/ffcffdc1-50db-42bc-bcbb-dcfe86758e26/graph",
    ],
    params => {format => "json"},
    provider => "https://blackfire.io",
    url => [
      "https://blackfire.io/profiles/*/graph",
      "https://blackfire.io/profiles/compare/*/graph",
    ],
  },
  "Blogcast" => {
    api => "https://blogcast.host/oembed",
    examples =>
        ["https://blogcast.host/embed/1", "https://blogcast.host/embed/300",],
    provider => "https://blogcast.host/",
    url =>
        ["https://blogcast.host/embed/*", "https://blogcast.host/embedly/*",],
  },
  "BoxOfficeBuz" => {
    api => "http://boxofficebuz.com/oembed",
    examples => [
      "http://movies.boxofficebuz.com/video/jack-reacher-never-go-back-tv-spot-hunting",
      "http://movies.boxofficebuz.com/video/ghost-in-the-shell-trailer-teaser-5",
    ],
    provider => "http://boxofficebuz.com",
    url => "https://boxofficebuz.com/*",
  },
  "BrioVR" => {
    api => "https://view.briovr.com/api/v1/worlds/oembed/",
    examples =>
        ["https://view.briovr.com/90487725-89bf-4acf-b8d2-0cbf0f560f7d/",],
    params => {format => "json"},
    provider => "https://view.briovr.com/",
    url => ["https://view.briovr.com/api/v1/worlds/oembed/*"],
  },
  "Buttondown" => {
    api => "https://buttondown.email/embed",
    provider => "https://buttondown.email/",
    url => ["https://buttondown.email/*"],
  },
  "ByzartProject" => {
    api => "https://cmc.byzart.eu/oembed/",
    examples => [
      "https://cmc.byzart.eu/files/original/ouc/ouc_cyprus_broadcasting_corporation/006_014_006448_01.mp4",
    ],
    params => {format => "json"},
    provider => "https://cmc.byzart.eu",
    url => ["https://cmc.byzart.eu/files/*"],
  },
  "Cacoo" => {
    api => "http://cacoo.com/oembed.{format}",
    examples => ["http://cacoo.com/diagrams/m9uZtizE5I2GkFR6"],
    provider => "https://cacoo.com",
    url => ["https://cacoo.com/diagrams/*"],
  },
  "CarbonHealth" => {
    api => "http://carbonhealth.com/oembed",
    provider => "https://carbonhealth.com",
    url => ["https://carbonhealth.com/practice/*"],
  },
  "CatBoat" => {
    api => "http://img.catbo.at/oembed.json",
    examples =>
        ["http://img.catbo.at/3fb93c1b7891aedb18aa41fb325cbc92e82e58a1.jpg",],
    params => {format => "json"},
    provider => "http://img.catbo.at/",
    url => ["http://img.catbo.at/*"],
  },
  "Ceros" => {
    api => "http://view.ceros.com/oembed",
    examples => [
      "https://view.ceros.com/ceros/new-experience-3",
      "https://view.ceros.com/ceros-inspire/fendi-desktop-4",
    ],
    provider => "http://www.ceros.com/",
    url => ["http://view.ceros.com/*"],
  },
  "ChartBlocks" => {
    api => "http://embed.chartblocks.com/1.0/oembed",
    examples => [
      "http://public.chartblocks.com/c/53f7702dc9a61d7935942613/",
      "http://public.chartblocks.com/c/53f7702dc9a61d7935942613/",
    ],
    params => {format => "json"},
    provider => "http://www.chartblocks.com/",
    url => ["http://public.chartblocks.com/c/*"],
  },
  "chirbit.com" => {
    api => "http://chirb.it/oembed.{format}",
    examples => ["http://chirb.it/OBnAr1"],
    provider => "http://www.chirbit.com/",
    url => ["http://chirb.it/*"],
  },
  "CircuitLab" => {
    api => "https://www.circuitlab.com/circuit/oembed/",
    examples => [
      "https://www.circuitlab.com/circuit/e38756/555-timer-as-astable-multivibrator-oscillator/",
    ],
    params => {format => "json"},
    provider => "https://www.circuitlab.com/",
    url => ["https://www.circuitlab.com/circuit/*"],
  },
  "Clipland" => {
    api => "https://www.clipland.com/api/oembed",
    examples =>
        ["http://www.clipland.com/v/1010", "http://www.clipland.com/v/1010",],
    params => {format => "json"},
    provider => "http://www.clipland.com/",
    url => ["http://www.clipland.com/v/*", "https://www.clipland.com/v/*"],
  },
  "Clyp" => {
    api => "http://api.clyp.it/oembed/",
    examples =>
        ["http://clyp.it/zhwuptos", "http://clyp.it/playlist/1kmfioze"],
    provider => "http://clyp.it/",
    url => ["http://clyp.it/*", "http://clyp.it/playlist/*"],
  },
  "CodeHS" => {
    api => "https://codehs.com/api/sharedprogram/*/oembed/",
    examples =>
        ["https://codehs.com/editor/share_abacus/xtOPDik2wNFjSDUoyl2T",],
    provider => "http://www.codehs.com",
    url => ["https://codehs.com/editor/share_abacus/*"],
  },
  "Codepen" => {
    api => "http://codepen.io/api/oembed",
    examples => ["https://codepen.io/gingerdude/pen/JXwgdK"],
    params => {format => "json"},
    provider => "https://codepen.io",
    url => ["http://codepen.io/*", "https://codepen.io/*"],
  },
  "Codepoints" => {
    api => "https://codepoints.net/api/v1/oembed",
    examples => ["https://codepoints.net/U+00E4", "https://codepoints.net/A"],
    params => {format => "json"},
    provider => "https://codepoints.net",
    url => [
      "http://codepoints.net/*", "https://codepoints.net/*",
      "http://www.codepoints.net/*", "https://www.codepoints.net/*",
    ],
  },
  "CodeSandbox" => {
    api => "https://codesandbox.io/oembed",
    examples => ["https://codesandbox.io/s/new"],
    params => {format => "json"},
    provider => "https://codesandbox.io",
    url => ["https://codesandbox.io/s/*", "https://codesandbox.io/embed/*",],
  },
  "CollegeHumor" => {
    api => "http://www.collegehumor.com/oembed.{format}",
    examples => [
      "http://www.collegehumor.com/video/3922232/prank-war-7-the-half-million-dollar-shot",
    ],
    provider => "http://www.collegehumor.com/",
    url => ["http://www.collegehumor.com/video/*"],
  },
  "Commaful" => {
    api => "https://commaful.com/api/oembed/",
    examples => ["//commaful.com/play/willyoumaryme/the-stars-in-us/"],
    provider => "https://commaful.com",
    url => ["https://commaful.com/play/*"],
  },
  "Coub" => {
    api => "http://coub.com/api/oembed.{format}",
    examples => [
      "http://coub.com/view/um0um0", "http://coub.com/view/um0um0",
      "http://coub.com/embed/um0um0", "http://coub.com/embed/um0um0",
    ],
    provider => "http://coub.com/",
    url => ["http://coub.com/view/*", "http://coub.com/embed/*"],
  },
  "CrowdRanking" => {
    api => "http://crowdranking.com/api/oembed.{format}",
    examples => ["http://crowdranking.com/rankings/t470g0--best-tea"],
    provider => "http://crowdranking.com",
    url => ["http://crowdranking.com/*/*"],
  },
  "CyranoSystems" => {
    api => "https://staging.cyranosystems.com/oembed",
    examples => [
      "https://staging.cyranosystems.com/msg/#/guestPlayProgram/000181d4-2b11-8702-0035-45f0449eb025",
    ],
    provider => "http://www.cyranosystems.com/",
    url => [
      "https://staging.cyranosystems.com/msg/*",
      "https://app.cyranosystems.com/msg/*",
    ],
  },
  "DailyMile" => {
    api => "http://api.dailymile.com/oembed?format=json",
    examples => ["http://www.dailymile.com/people/EddieJ3/entries/24776213"],
    params => {format => "json"},
    provider => "http://www.dailymile.com",
    url => ["http://www.dailymile.com/people/*/entries/*"],
  },
  "Dailymotion" => {
    api => "https://www.dailymotion.com/services/oembed",
    examples =>
        ["http://www.dailymotion.com/video/xoxulz_babysitter_animals"],
    params => {format => "json"},
    provider => "https://www.dailymotion.com",
    url => ["https://www.dailymotion.com/video/*"],
  },
  "DeseretNews" => {
    api => "https://embed.deseret.com/",
    examples => [
      "https://graphics.deseret.com/american-family-survey/becoming-an-adult",
    ],
    params => {format => "json"},
    provider => "https://www.deseret.com",
    url => ["https://*.deseret.com/*"],
  },
  "Deviantart.com" => {
    api => "http://backend.deviantart.com/oembed",
    examples => ["http://browse.deviantart.com/art/Vita-Brevis-379998342"],
    params => {format => "json"},
    provider => "http://www.deviantart.com",
    url => [
      "http://*.deviantart.com/art/*", "http://*.deviantart.com/*#/d*",
      "http://fav.me/*", "http://sta.sh/*",
      "https://*.deviantart.com/art/*", "https://*.deviantart.com/*/art/*",
      "https://sta.sh/*\",", "https://*.deviantart.com/*#/d*\"",
    ],
  },
  "Didacte" => {
    api => "https://*.didacte.com/cards/oembed'",
    examples => ["https://finchp.didacte.com/a/course/363?locale=fr"],
    provider => "https://www.didacte.com/",
    url => ["https://*.didacte.com/a/course/*"],
  },
  "Digiteka" => {
    api => "https://www.ultimedia.com/api/search/oembed",
    examples => [
      "https://www.ultimedia.com/default/index/videogeneric/id/smxuxm",
      "https://www.ultimedia.com/default/index/videogeneric/id/smxuxm",
    ],
    params => {format => "json"},
    provider => "https://www.ultimedia.com/",
    url => [
      "https://www.ultimedia.com/central/video/edit/id/*/topic_id/*/",
      "https://www.ultimedia.com/default/index/videogeneric/id/*/showtitle/1/viewnc/1",
      "https://www.ultimedia.com/default/index/videogeneric/id/*",
    ],
  },
  "Dipity" => {
    api => "http://www.dipity.com/oembed/timeline/",
    examples => ["http://www.dipity.com/ragutier/Historia_de_la_Web/"],
    params => {format => "json"},
    provider => "http://www.dipity.com",
    url => ["http://www.dipity.com/*/*/"],
  },
  "DocDroid" => {
    api => "https://www.docdroid.net/api/oembed",
    examples =>
        ["https://www.docdroid.net/hptvUCe/example-document.docx.html",],
    provider => "https://www.docdroid.net/",
    url => [
      "https://*.docdroid.net/*", "http://*.docdroid.net/*",
      "https://docdro.id/*", "http://docdro.id/*",
    ],
  },
  "Dotsub" => {
    api => "http://dotsub.com/services/oembed",
    examples =>
        ["http://dotsub.com/view/665bd0d5-a9f4-4a07-9d9e-b31ba926ca78",],
    params => {format => "json"},
    provider => "http://dotsub.com/",
    url => ["http://dotsub.com/view/*"],
  },
  "DTube" => {
    api => "https://api.d.tube/oembed",
    examples => [
      "https://d.tube/v/benswann/zqd630em",
      "https://d.tube/v/marketingmonk/t0fj6eip",
    ],
    params => {format => "json"},
    provider => "https://d.tube/",
    url => ["https://d.tube/v/*"],
  },
  "edocr" => {
    api => "http://edocr.com/api/oembed",
    examples => [
      "http://www.edocr.com/doc/144677/capillary-technologies-corporate-brochure",
    ],
    params => {format => "json"},
    provider => "http://www.edocr.com",
    url => ["http://edocr.com/docs/*"],
  },
  "eduMedia" => {
    api => "https://www.edumedia-sciences.com/oembed.json",
    examples => [
      "https://www.edumedia-sciences.com/en/media/834-9-months-to-create-life",
      "https://www.edumedia-sciences.com/fr/media/836",
    ],
    provider => "https://www.edumedia-sciences.com/",
    url => "https://www.edumedia-sciences.com/*",
  },
  "EgliseInfo" => {
    api => "http://egliseinfo.catholique.fr/api/oembed",
    examples => [
      "http://egliseinfo.catholique.fr/horaires/paris",
      "http://egliseinfo.catholique.fr/horaires/paris",
    ],
    params => {format => "json"},
    provider => "http://egliseinfo.catholique.fr/",
    url => ["http://egliseinfo.catholique.fr/*"],
  },
  "EmbedArticles" => {
    api => "http://embedarticles.com/oembed/",
    examples => [
      "http://embedarticles.com/article/101887/yemi~alade~ft.~selebobo~~na~gode/",
    ],
    provider => "http://embedarticles.com/",
    url => ["http://embedarticles.com/*"],
  },
  "Embedly" => {
    api => "http://api.embed.ly/1/oembed",
    examples => ["http://www.youtube.com/watch?v=B-m6JDYRFvk"],
    provider => "http://api.embed.ly/",
    url => "https://api.embed.ly/*",
  },
  "Ethfiddle" => {
    api => "https://ethfiddle.com/services/oembed/",
    examples => ["https://ethfiddle.com/Y8Iy49zDJ0"],
    params => {format => "json"},
    provider => "https://www.ethfiddle.com/",
    url => ["https://ethfiddle.com/*"],
  },
  "Eyrie" => {
    api => "https://eyrie.io/v1/oembed",
    examples => ["https://eyrie.io/board/747d351c00bc4f91ae7b95635942e685"],
    params => {format => "json"},
    provider => "https://eyrie.io/",
    url => ["https://eyrie.io/board/*", "https://eyrie.io/sparkfun/*"],
  },
  "Facebook" => {
    api => "https://www.facebook.com/plugins/post/oembed.json",
    provider => "https://www.facebook.com/",
    url => [
      "https://www.facebook.com/*/posts/*",
      "https://www.facebook.com/photos/*",
      "https://www.facebook.com/*/photos/*",
      "https://www.facebook.com/photo.php*",
      "https://www.facebook.com/photo.php",
      "https://www.facebook.com/*/activity/*",
      "https://www.facebook.com/permalink.php",
      "https://www.facebook.com/media/set?set=*",
      "https://www.facebook.com/questions/*",
      "https://www.facebook.com/notes/*/*/*",
      "https://www.facebook.com/watch/*",
      "https://www.facebook.com/*/videos/*",
    ],
  },
  "Fader" => {
    api => "https://app.getfader.com/api/oembed",
    examples => [
      "https://app.getfader.com/projects/89a73dd0-4926-4f05-a9a8-6896a0a07a71/publish",
    ],
    params => {format => "json"},
    provider => "https://app.getfader.com",
    url => ["https://app.getfader.com/projects/*/publish"],
  },
  "FaithlifeTV" => {
    api => "https://faithlifetv.com/api/oembed",
    examples => [
      "https://faithlifetv.com/items/300027",
      "https://faithlifetv.com/media/300027",
    ],
    params => {format => "json"},
    provider => "https://faithlifetv.com",
    url => [
      "https://faithlifetv.com/items/*",
      "https://faithlifetv.com/items/resource/*/*",
      "https://faithlifetv.com/media/*",
      "https://faithlifetv.com/media/assets/*",
      "https://faithlifetv.com/media/resource/*/*",
    ],
  },
  "FITE" => {
    api => "https://www.fite.tv/oembed",
    examples => ["https://www.fite.tv/watch/fite-tv-test-stream/2kmfd/"],
    params => {format => "json"},
    provider => "https://www.fite.tv/",
    url => ["https://www.fite.tv/watch/*"],
  },
  "Flat" => {
    api => "https://flat.io/services/oembed",
    examples => ["https://flat.io/score/56ae21579a127715a02901a6"],
    provider => "https://flat.io",
    url => ["https://flat.io/score/*", "https://*.flat.io/score/*"],
  },
  "Flickr" => {
    api => "https://www.flickr.com/services/oembed/",
    examples => ["http://flickr.com/photos/bees/2362225867/"],
    provider => "https://www.flickr.com/",
    url => [
      "http://*.flickr.com/photos/*", "http://flic.kr/p/*",
      "https://*.flickr.com/photos/*", "https://flic.kr/p/*",
    ],
  },
  "Flourish" => {
    api => "https://app.flourish.studio/api/v1/oembed",
    examples => ["https://public.flourish.studio/visualisation/47988/"],
    provider => "https://flourish.studio/",
    url => [
      "https://public.flourish.studio/visualisation/*",
      "https://public.flourish.studio/story/*",
    ],
  },
  "Fontself" => {
    api => "https://oembed.fontself.com/",
    examples => [
      "https://catapult.fontself.com/MEdLOEq/gilbert-color-bold-preview4",
      "https://catapult.fontself.com/gj8eJaq/welcome-regular",
    ],
    provider => "https://www.fontself.com",
    url => ["https://catapult.fontself.com/*"],
  },
  "FOXSPORTSAustralia" => {
    api => "https://fiso.foxsports.com.au/oembed",
    examples => [
      "http://fiso.foxsports.com.au/isomorphic-widget/scoreboard/1.0.0/scoreboard.html",
      "http://fiso.foxsports.com.au/isomorphic-widget/scoreboard/1.0.0/scoreboard.html",
    ],
    provider => "http://www.foxsports.com.au",
    url => [
      "http://fiso.foxsports.com.au/isomorphic-widget/*",
      "https://fiso.foxsports.com.au/isomorphic-widget/*",
    ],
  },
  "FrameBuzz" => {
    api => "https://framebuzz.com/oembed/",
    examples => ["https://framebuzz.com/v/tJjtJ3rN1usuqAeY/"],
    provider => "https://framebuzz.com/",
    url => ["http://framebuzz.com/v/*", "https://framebuzz.com/v/*"],
  },
  "FunnyOrDie" => {
    api => "http://www.funnyordie.com/oembed.{format}",
    examples => [
      "http://www.funnyordie.com/videos/a7311134ac/patton-oswalt-in-heavy-metal",
    ],
    provider => "http://www.funnyordie.com/",
    url => ["http://www.funnyordie.com/videos/*"],
  },
  "GeographBritainandIreland" => {
    api => "http://api.geograph.org.uk/api/oembed",
    examples => [
      "http://www.geograph.org.uk/photo/2928776",
      "http://s0.geograph.org.uk/geophotos/02/92/87/2928776_72cdbeab.jpg",
    ],
    params => {format => "json"},
    provider => "https://www.geograph.org.uk/",
    url => [
      "http://*.geograph.org.uk/*",
      "http://*.geograph.co.uk/*",
      "http://*.geograph.ie/*",
      "http://*.wikimedia.org/*_geograph.org.uk_*",
    ],
  },
  "GeographChannelIslands" => {
    api => "http://www.geograph.org.gg/api/oembed",
    examples => [
      "http://www.geograph.org.gg/photo/773",
      "http://s1.channel.geographs.org/photos/00/07/000773_e1e23765_120x120.jpg",
    ],
    params => {format => "json"},
    provider => "http://channel-islands.geograph.org/",
    url => [
      "http://*.geograph.org.gg/*",
      "http://*.geograph.org.je/*",
      "http://channel-islands.geograph.org/*",
      "http://channel-islands.geographs.org/*",
      "http://*.channel.geographs.org/*",
    ],
  },
  "GeographGermany" => {
    api => "http://geo.hlipp.de/restapi.php/api/oembed",
    examples => [
      "http://geo.hlipp.de/photo/20260",
      "http://geo.hlipp.de/photos/02/02/020260_dcfdbf8e.jpg",
    ],
    params => {format => "json"},
    provider => "http://geo-en.hlipp.de/",
    url => [
      "http://geo-en.hlipp.de/*", "http://geo.hlipp.de/*",
      "http://germany.geograph.org/*",
    ],
  },
  "GettyImages" => {
    api => "http://embed.gettyimages.com/oembed",
    examples => ["http://gty.im/74917285"],
    provider => "http://www.gettyimages.com/",
    url => ["http://gty.im/*"],
  },
  "Gfycat" => {
    api => "https://api.gfycat.com/v1/oembed",
    examples => ["http://www.gfycat.com/RichPepperyFerret"],
    provider => "https://gfycat.com/",
    url => [
      "http://gfycat.com/*", "http://www.gfycat.com/*",
      "https://gfycat.com/*", "https://www.gfycat.com/*",
    ],
  },
  "Gifnote" => {
    api => "https://www.gifnote.com/services/oembed",
    examples => [
      "http://www.gifnote.com/play/237672132731995400",
      "http://www.gifnote.com/play/237672132731995400",
    ],
    params => {format => "json"},
    provider => "https://www.gifnote.com/",
    url => ["https://www.gifnote.com/play/*"],
  },
  "GIPHY" => {
    api => "https://giphy.com/services/oembed",
    examples => ["https://giphy.com/gifs/cant-hardly-wait-kW8mnYSNkUYKc"],
    provider => "https://giphy.com",
    url => [
      "https://giphy.com/gifs/*", "http://gph.is/*",
      "https://media.giphy.com/media/*/giphy.gif",
    ],
  },
  "GloriaTV" => {
    api => "https://gloria.tv/oembed/",
    examples => ["https://gloria.tv/video/FRqEWoz7GfGt1pfhD4krcgyqC"],
    provider => "https://gloria.tv/",
    url => "https://gloria.tv/*",
  },
  "GTChannel" => {
    api => "https://api.luminery.com/oembed",
    examples => ["http://gtchannel.com/watch/4ODiBxivkuTXfsk1tv20Ox"],
    provider => "https://gtchannel.com",
    url => ["https://gtchannel.com/watch/*"],
  },
  "Gyazo" => {
    api => "https://api.gyazo.com/api/oembed",
    examples => ["https://gyazo.com/71e107d77e8495f0e54d2e5b6dc5d326"],
    provider => "https://gyazo.com",
    url => ["https://gyazo.com/*"],
  },
  "hearthis.at" => {
    api => "https://hearthis.at/oembed/",
    examples => [
      "https://hearthis.at/gdsfm/20180922-motherland-soundsystem-im-sender/",
      "https://hearthis.at/gdsfm/20180922-motherland-soundsystem-im-sender/",
    ],
    params => {format => "json"},
    provider => "https://hearthis.at/",
    url => ["https://hearthis.at/*/*/", "https://hearthis.at/*/set/*/"],
  },
  "Homey" => {
    api => "https://homey.app/api/oembed/flow",
    examples => ["https://homey.app/f/abcdef/"],
    provider => "https://homey.app",
    url => ["https://homey.app/f/*", "https://homey.app/*/flow/*"],
  },
  "HuffDuffer" => {
    api => "http://huffduffer.com/oembed",
    examples => ["http://huffduffer.com/jxpx777/125342"],
    params => {format => "json"},
    provider => "http://huffduffer.com",
    url => ["http://huffduffer.com/*/*"],
  },
  "Hulu" => {
    api => "http://www.hulu.com/api/oembed.{format}",
    examples => [
      "http://www.hulu.com/watch/20807/late-night-with-conan-obrien-wed-may-21-2008",
    ],
    provider => "http://www.hulu.com/",
    url => ["http://www.hulu.com/watch/*"],
  },
  "iFixit" => {
    api => "http://www.ifixit.com/Embed",
    examples => ["http://www.ifixit.com/Teardown/iPhone-4-Teardown/3130/1"],
    params => {format => "json"},
    provider => "http://www.iFixit.com",
    url => ["http://www.ifixit.com/Guide/View/*"],
  },
  "IFTTT" => {
    api => "http://www.ifttt.com/oembed/",
    examples => ["https://ifttt.com/recipes/107745"],
    provider => "http://www.ifttt.com/",
    url => ["http://ifttt.com/recipes/*"],
  },
  "Indaco" => {
    api => "https://player.indacolive.com/services/oembed",
    examples => [
      "http://player.indacolive.com/player/jwp/clients/test/2016/9/pallacanestro_reggiana/",
    ],
    provider => "https://player.indacolive.com/",
    url => ["https://player.indacolive.com/player/jwp/clients/*"],
  },
  "Infogram" => {
    api => "https://infogram.com/oembed",
    examples => ["https://infogram.com/amazon-and-the-book-market"],
    provider => "https://infogram.com/",
    url => ["https://infogram.com/*"],
  },
  "Infoveave" => {
    api => "https://infoveave.net/services/oembed/",
    examples => [
      "https://demo.infoveave.net/E/ZGVtb3wxfENIfDU2OTR8MjAxfHRydWV8dHJ1ZQ==|AP25RKrQl0t",
      "https://demo.infoveave.net/E/ZGVtb3wxfElCfDI1Mjh8MjAxfHRydWV8dHJ1ZQ==|fUCXVFSUrLe",
      "https://demo.infoveave.net/E/ZGVtb3wxfENIfDQ5MjV8MjAxfHRydWV8dHJ1ZQ==|3x0P5uN99p3",
    ],
    params => {format => "json"},
    provider => "https://infoveave.net/",
    url => ["https://*.infoveave.net/E/*", "https://*.infoveave.net/P/*"],
  },
  "Injurymap" => {
    api => "https://www.injurymap.com/services/oembed",
    examples => [
      "https://injurymap.com/exercises/ZHSJKssCjIDF",
      "https://injurymap.com/exercises/ZHSJKssCjIDF",
    ],
    params => {format => "json"},
    provider => "https://www.injurymap.com/",
    url => ["https://www.injurymap.com/exercises/*"],
  },
  "Inoreader" => {
    api => "https://www.inoreader.com/oembed/api/",
    examples => [
      "http://www.inoreader.com/article/3a9c6e7f31414b1c-how-to-prevent-spotify-from-wasting-disk-space",
      "http://www.inoreader.com/article/3a9c6e7f31414b1c-how-to-prevent-spotify-from-wasting-disk-space",
    ],
    params => {format => "json"},
    provider => "https://www.inoreader.com",
    url => ["https://www.inoreader.com/oembed/"],
  },
  "inphood" => {
    api => "http://api.inphood.com/oembed",
    examples => [
      "http://www.label.inphood.com/?query&user=test&label=-KeuRz0ubjnQVkJCmGDH",
    ],
    provider => "http://inphood.com/",
    url => ["http://*.inphood.com/*"],
  },
  "Instagram" => {
    api => "https://api.instagram.com/oembed",
    examples => ["http://instagram.com/p/V8UMy0LjpX/"],
    provider => "https://instagram.com",
    url => [
      "http://instagram.com/*/p/*,", "http://www.instagram.com/*/p/*,",
      "https://instagram.com/*/p/*,", "https://www.instagram.com/*/p/*,",
      "http://instagram.com/p/*", "http://instagr.am/p/*",
      "http://www.instagram.com/p/*", "http://www.instagr.am/p/*",
      "https://instagram.com/p/*", "https://instagr.am/p/*",
      "https://www.instagram.com/p/*", "https://www.instagr.am/p/*",
      "http://instagram.com/tv/*", "http://instagr.am/tv/*",
      "http://www.instagram.com/tv/*", "http://www.instagr.am/tv/*",
      "https://instagram.com/tv/*", "https://instagr.am/tv/*",
      "https://www.instagram.com/tv/*", "https://www.instagr.am/tv/*",
    ],
  },
  "iSnareArticles" => {
    api => "https://www.isnare.com/oembed/",
    examples => ["http://www.isnare.com/?aid=1897753&ca=Marketing"],
    provider => "https://www.isnare.com/",
    url => ["https://www.isnare.com/*"],
  },
  "Issuu" => {
    api => "https://issuu.com/oembed",
    examples => ["https://issuu.com/iscience/docs/issue23"],
    params => {format => "json"},
    provider => "https://issuu.com/",
    url => ["https://issuu.com/*/docs/*"],
  },
  "ivlismusic" => {
    api => "https://music.ivlis.kr/oembed",
    examples => [
      "https://music.ivlis.kr/?artist=Justin Bieber&track=Sorry",
      "https://music.ivlis.kr/?artist=Justin Bieber&track=Sorry",
    ],
    params => {format => "json"},
    provider => "https://music.ivlis.kr/",
    url => "https://music.ivlis.kr/*",
  },
  "Jovian" => {
    api => "https://api.jovian.ai/oembed.json",
    examples => [
      "https://jovian.ml/aakashns/movielens-fastai",
      "https://jovian.ml/aakashns/01-pytorch-basics/v/7",
    ],
    provider => "https://jovian.ml/",
    url => [
      "https://jovian.ml/*", "https://jovian.ml/viewer*",
      "https://*.jovian.ml/*",
    ],
  },
  "KakaoTv" => {
    api => "https://tv.kakao.com/oembed",
    examples => [
      "https://tv.kakao.com/channel/2658101/cliplink/300605724",
      "https://tv.kakao.com/channel/2658101/cliplink/300605724",
    ],
    params => {format => "json"},
    provider => "https://tv.kakao.com/",
    url => [
      "https://tv.kakao.com/channel/*/cliplink/*",
      "https://tv.kakao.com/channel/v/*",
      "https://tv.kakao.com/channel/*/livelink/*",
      "https://tv.kakao.com/channel/l/*",
    ],
  },
  "Kickstarter" => {
    api => "http://www.kickstarter.com/services/oembed",
    examples => [
      "http://www.kickstarter.com/projects/1115015686/help-support-the-kiggins-theatre-to-go-digital",
    ],
    provider => "http://www.kickstarter.com",
    url => ["http://www.kickstarter.com/projects/*"],
  },
  "Kidoju" => {
    api => "https://www.kidoju.com/api/oembed",
    examples => [
      "https://www.kidoju.com/en/x/57c1c06430c6681900538352/57c1c06530c6681900538353",
      "https://www.kidoju.com/en/x/57c1c06430c6681900538352/57c1c06530c6681900538353",
    ],
    params => {format => "json"},
    provider => "https://www.kidoju.com/",
    url => [
      "https://www.kidoju.com/en/x/*/*",
      "https://www.kidoju.com/fr/x/*/*",
    ],
  },
  "Kirim.Email" => {
    api => "https://halaman.email/service/oembed",
    examples => [
      "https://halaman.email/form/205c01c4-88d9-4036-a326-20d87a996513",
      "https://halaman.email/form/205c01c4-88d9-4036-a326-20d87a996513",
    ],
    params => {format => "json"},
    provider => "https://kirim.email/",
    url => [
      "https://halaman.email/form/*",
      "https://aplikasi.kirim.email/form/*",
    ],
  },
  "Kit" => {
    api => "https://embed.kit.co/oembed",
    examples => [
      "https://kit.co/MKBHD/video-gear",
      "https://kit.co/YARNutopia/nintendo-nes-controller-pixel-blanket-crochet-supplies-kit",
    ],
    provider => "https://kit.co/",
    url => ["http://kit.co/*/*", "https://kit.co/*/*"],
  },
  "Kitchenbowl" => {
    api => "http://www.kitchenbowl.com/oembed",
    examples => [
      "http://www.kitchenbowl.com/recipe/NVsYg1R8ql/pork-and-shiitake-mushroom-dumplings",
    ],
    provider => "http://www.kitchenbowl.com",
    url => ["http://www.kitchenbowl.com/recipe/*"],
  },
  "Knacki" => {
    api => "https://jdr.knacki.info/oembed",
    examples => ["https://jdr.knacki.info/meuh/desole"],
    params => {format => "json"},
    provider => "http://jdr.knacki.info",
    url =>
        ["http://jdr.knacki.info/meuh/*", "https://jdr.knacki.info/meuh/*",],
  },
  "LearningApps.org" => {
    api => "http://learningapps.org/oembed.php",
    examples => ["http://LearningApps.org/259"],
    params => {format => "json"},
    provider => "http://learningapps.org/",
    url => ["http://learningapps.org/*"],
  },
  "Lille.Pod" => {
    api => "https://pod.univ-lille.fr/oembed",
    examples => [
      "https://pod.univ-lille.fr/video/0001-clip-pod/",
      "https://pod.univ-lille.fr/video/0001-clip-pod/",
    ],
    params => {format => "json"},
    provider => "https://pod.univ-lille.fr/",
    url => ["https://pod.univ-lille.fr/video/*"],
  },
  "Livestream" => {
    api => "https://livestream.com/oembed",
    examples => [
      "https://livestream.com/livestream/3camkit",
      "https://livestream.com/livestream/3camkit/videos/150060311",
    ],
    provider => "https://livestream.com/",
    url => [
      "https://livestream.com/accounts/*/events/*",
      "https://livestream.com/accounts/*/events/*/videos/*",
      "https://livestream.com/*/events/*",
      "https://livestream.com/*/events/*/videos/*",
      "https://livestream.com/*/*",
      "https://livestream.com/*/*/videos/*",
    ],
  },
  "Ludus" => {
    api => "https://app.ludus.one/oembed",
    examples =>
        ["https://app.ludus.one/fd01598e-5ed7-4edb-8d0e-cf75a36e0a07"],
    provider => "https://ludus.one",
    url => ["https://app.ludus.one/*"],
  },
  "MathEmbed" => {
    api => "http://mathembed.com/oembed",
    examples => ["http://mathembed.com/latex?inputText=f(x)"],
    provider => "http://mathembed.com",
    url => [
      "http://mathembed.com/latex?inputText=*",
      "http://mathembed.com/latex?inputText=*",
    ],
  },
  "Matterport" => {
    api => "https://my.matterport.com/api/v1/models/oembed/",
    examples => ["https://my.matterport.com/show/?m=FmDYedjofjo"],
    provider => "https://matterport.com/",
    url => "https://matterport.com/*",
  },
  "me.me" => {
    api => "https://me.me/oembed",
    examples => ["https://me.me/i/3174471", "https://me.me/i/3174471"],
    params => {format => "json"},
    provider => "https://me.me/",
    url => ["https://me.me/i/*"],
  },
  "MedienarchivderK\xFCnste-Z\xFCrcherHochschulederK\xFCnste" => {
    api => "https://medienarchiv.zhdk.ch/oembed.{format}",
    examples => [
      "https://medienarchiv.zhdk.ch/entries/da88e9e6-6b53-447b-8113-637d885f8ab2",
      "https://medienarchiv.zhdk.ch/entries/da88e9e6-6b53-447b-8113-637d885f8ab2",
    ],
    provider => "https://medienarchiv.zhdk.ch/",
    url => ["https://medienarchiv.zhdk.ch/entries/*"],
  },
  "Meetup" => {
    api => "https://api.meetup.com/oembed",
    examples => ["http://www.meetup.com/PHPColMeetup/photos/"],
    params => {format => "json"},
    provider => "http://www.meetup.com",
    url => [
      "http://meetup.com/*", "https://www.meetup.com/*",
      "https://meetup.com/*", "http://meetu.ps/*",
    ],
  },
  'MicrosoftStream' => {
    'api' => 'https://web.microsoftstream.com/oembed',
    'url' => [
      'https://web.microsoftstream.com/video/*',
      'https://web.microsoftstream.com/chanel/*'
    ]
  },
  "MermaidInk" => {
    api => "https://mermaid.ink/services/oembed",
    examples => [
      "https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtBXSAtLT4gQihCKVxuXHRcdCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In19",
    ],
    provider => "https://mermaid.ink",
    url => ["https://mermaid.ink/img/*", "https://mermaid.ink/svg/*"],
  },
  "Microlink" => {
    api => "https://api.microlink.io",
    examples => ["http://www.youtube.com/watch?v=B-m6JDYRFvk"],
    provider => "http://api.microlink.io",
    url => "https://api.microlink.io/*",
  },
  "MixCloud" => {
    api => "https://www.mixcloud.com/oembed/",
    examples => [
      "http://www.mixcloud.com/TechnoLiveSets/jon_rundell-live-electrobeach-festival-benidorm-16-08-2013/",
    ],
    params => {format => "json"},
    provider => "https://mixcloud.com/",
    url => ["http://www.mixcloud.com/*/*/", "https://www.mixcloud.com/*/*/",],
  },
  "MobyPicture" => {
    api => "http://api.mobypicture.com/oEmbed",
    examples => ["http://mobypicture.com/user/Henk_Voermans/view/15880044"],
    params => {format => "json"},
    provider => "http://www.mobypicture.com",
    url => ["http://www.mobypicture.com/user/*/view/*", "http://moby.to/*",],
  },
  "Modelo" => {
    api => "https://portal.modelo.io/oembed",
    examples => [
      "https://beta.modelo.io/embedded/CM89QBlZtp?viewport=false&autoplay=false",
      "https://beta.modelo.io/embedded/PB4PgLTHJq?viewport=false&autoplay=false",
    ],
    params => {
      authorName => "Tian Deng",
      modelName =>
          "JASPER ARCHITECTS - 161012_LISBOA_TODO_CON TERRENO_67_unix",
    },
    provider => "http://modelo.io/",
    url => ["https://beta.modelo.io/embedded/*"],
  },
  "MorphCast" => {
    api => "https://m-roll.morphcast.com/service/oembed",
    examples => [
      "https://m-roll.morphcast.com/mroll/?cameraon=true&hidecontrols=true&m=honda_2#/q=",
    ],
    provider => "https://www.morphcast.com",
    url => ["https://m-roll.morphcast.com/mroll/*"],
  },
  "MusicBoxManiacs" => {
    api => "https://musicboxmaniacs.com/embed/",
    examples => [
      "https://musicboxmaniacs.com/explore/melody/candyman-ost-music-box_1/",
    ],
    provider => "https://musicboxmaniacs.com/",
    url => ["https://musicboxmaniacs.com/explore/melody/*"],
  },
  "myBeweeg" => {
    api => "https://mybeweeg.com/services/oembed",
    examples => ["https://mybeweeg.com/w/NyWxXR7tb"],
    provider => "https://mybeweeg.com",
    url => ["https://mybeweeg.com/w/*"],
  },
  "Namchey" => {
    api => "https://namchey.com/api/oembed",
    examples => ["https://namchey.com/itineraries/tilicho"],
    params => {format => "json"},
    provider => "https://namchey.com",
    url => ["https://namchey.com/embeds/*"],
  },
  "nanoo.tv" => {
    api => "https://www.nanoo.tv/services/oembed",
    examples => [
      "https://nanoo.tv/link/v/zBNqdjLG",
      "https://nanoo.tv/link/v/zBNqdjLG",
      "https://nanoo.tv/link/v/zBNqdjLG",
    ],
    params => {format => "json"},
    provider => "https://www.nanoo.tv/",
    url => [
      "http://*.nanoo.tv/link/*",
      "http://nanoo.tv/link/*",
      "http://*.nanoo.pro/link/*",
      "http://nanoo.pro/link/*",
      "https://*.nanoo.tv/link/*",
      "https://nanoo.tv/link/*",
      "https://*.nanoo.pro/link/*",
      "https://nanoo.pro/link/*",
      "http://media.zhdk.ch/signatur/*",
      "http://new.media.zhdk.ch/signatur/*",
      "https://media.zhdk.ch/signatur/*",
      "https://new.media.zhdk.ch/signatur/*",
    ],
  },
  "Nasjonalbiblioteket" => {
    api => "https://api.nb.no/catalog/v1/oembed",
    examples => [
      "https://www.nb.no/items/68d7a0e64760706052519cc1c900c975",
      "https://www.nb.no/items/512fe10f3e2fae3c6dd08338e47535f6",
    ],
    provider => "https://www.nb.no/",
    url => ["https://www.nb.no/items/*"],
  },
  "NaturalAtlas" => {
    api => "https://naturalatlas.com/oembed.{format}",
    examples => [
      "https://naturalatlas.com/waterfalls/lower-falls-of-the-yellowstone-river-1004042",
    ],
    provider => "https://naturalatlas.com/",
    url => [
      "https://naturalatlas.com/*", "https://naturalatlas.com/*/*",
      "https://naturalatlas.com/*/*/*", "https://naturalatlas.com/*/*/*/*",
    ],
  },
  "nfb.ca" => {
    api => "http://www.nfb.ca/remote/services/oembed/",
    examples => ["http://www.nfb.ca/film/aboriginality"],
    params => {format => "json"},
    provider => "http://www.nfb.ca/",
    url => ["http://*.nfb.ca/film/*"],
  },
  "Odds.com.au" => {
    api => "https://www.odds.com.au/api/oembed/",
    examples => ["https://www.odds.com.au/odds/rugby-league/nrl/"],
    params => {format => "json"},
    provider => "https://www.odds.com.au",
    url => ["https://www.odds.com.au/*", "https://odds.com.au/*"],
  },
  "OfficialFM" => {
    api => "http://official.fm/services/oembed.{format}",
    examples => ["http://official.fm/tracks/npTR"],
    provider => "http://official.fm",
    url => ["http://official.fm/tracks/*", "http://official.fm/playlists/*",],
  },
  "Omniscope" => {
    api => "https://omniscope.me/_global_/oembed/json",
    examples => [
      "https://omniscope.me/internal/Pollution/TarantAir.iox/r/Report/",
      "https://omniscope.me/Demos/Brexit/Brexit Tweets.iox/r/Report/",
      "https://omniscope.me/Demos/Quality of Life/Italy Sole24Ore.iox/",
    ],
    provider => "https://omniscope.me/",
    url => ["https://omniscope.me/*"],
  },
  "OnAol" => {
    api => "http://on.aol.com/api",
    examples => [
      "http://on.aol.com/video/plans-to-clone-john-lennon-using-one-of-his-teeth-517906689",
    ],
    provider => "http://on.aol.com/",
    url => ["http://on.aol.com/video/*"],
  },
  "OraTV" => {
    api => "https://www.ora.tv/oembed/*?format={format}",
    params => {format => "json"},
    provider => "http://www.ora.tv/",
    url => "https://www.ora.tv/*",
  },
  "Orbitvu" => {
    api => "http://orbitvu.co/service/oembed",
    examples => [
      "https://orbitvu.co/001/JJXNutMRq8DvjEQ8Sbv8WH/ov3601/3/view",
      "https://orbitvu.co/001/JJXNutMRq8DvjEQ8Sbv8WH/2/orbittour/61/view",
    ],
    params => {format => "json"},
    provider => "https://orbitvu.co",
    url => [
      "https://orbitvu.co/001/*/ov3601/view",
      "https://orbitvu.co/001/*/ov3601/*/view",
      "https://orbitvu.co/001/*/ov3602/*/view",
      "https://orbitvu.co/001/*/2/orbittour/*/view",
      "https://orbitvu.co/001/*/1/2/orbittour/*/view",
      "http://orbitvu.co/001/*/ov3601/view",
      "http://orbitvu.co/001/*/ov3601/*/view",
      "http://orbitvu.co/001/*/ov3602/*/view",
      "http://orbitvu.co/001/*/2/orbittour/*/view",
      "http://orbitvu.co/001/*/1/2/orbittour/*/view",
    ],
  },
  "Oumy" => {
    api => "https://www.oumy.com/oembed",
    examples => ["https://www.oumy.com/v/0NmY0agdvcA7wlvIXbJaBzA"],
    params => {format => "json"},
    provider => "https://www.oumy.com/",
    url => ["https://www.oumy.com/v/*"],
  },
  "Outplayed.tv" => {
    api => "https://outplayed.tv/oembed",
    examples => ["https://outplayed.tv/media/KwjQG"],
    provider => "https://outplayed.tv/",
    url => ["https://outplayed.tv/media/*"],
  },
  "Overflow" => {
    api => "https://overflow.io/services/oembed",
    examples => [
      "https://overflow.io/s/9ST7SX/",
      "https://overflow.io/embed/9ST7SX/",
    ],
    params => {format => "json"},
    provider => "https://overflow.io",
    url => ["https://overflow.io/s/*", "https://overflow.io/embed/*"],
  },
  "OZ" => {
    api => "https://core.oz.com/oembed",
    examples => [
      "https://www.oz.com/gnarr/video/fc9a8540-6fd5-4dd8-a0d9-daca43bbfb2e",
      "https://www.oz.com/gnarr/video/fc9a8540-6fd5-4dd8-a0d9-daca43bbfb2e",
    ],
    params => {format => "json"},
    provider => "https://www.oz.com/",
    url => ["https://www.oz.com/*/video/*"],
  },
  "Pastery" => {
    api => "https://www.pastery.net/oembed",
    examples =>
        ["https://www.pastery.net/about/", "https://www.pastery.net/api/",],
    params => {format => "json"},
    provider => "https://www.pastery.net",
    url => [
      "http://pastery.net/*", "https://pastery.net/*",
      "http://www.pastery.net/*", "https://www.pastery.net/*",
    ],
  },
  "PingVP" => {
    api => "https://beta.pingvp.com.kpnis.nl/p/oembed.php",
    examples => ["https://beta.pingvp.com.kpnis.nl/v/index.php?v=anxXNrIi31"],
    provider => "https://www.pingvp.com/",
    url => "https://www.pingvp.com/*",
  },
  "Pixdor" => {
    api => "https://store.pixdor.com/oembed",
    examples => [
      "https://store.pixdor.com/place-marker-widget/20/show",
      "https://store.pixdor.com/map/25/show",
      "https://store.pixdor.com/map/10/show",
    ],
    provider => "http://www.pixdor.com/",
    url => [
      "https://store.pixdor.com/place-marker-widget/*/show",
      "https://store.pixdor.com/map/*/show",
    ],
  },
  "Podbean" => {
    api => "https://api.podbean.com/v1/oembed",
    examples => [
      "https://podcast.podbean.com/e/jen-and-vernon-chat-podcast-resolutions-twitter-advice-and-predictions-for-2019/",
    ],
    provider => "http://podbean.com",
    url => ["https://*.podbean.com/e/*", "http://*.podbean.com/e/*"],
  },
  "PolarisShare" => {
    api => "https://api.polarishare.com/rest/api/oembed",
    examples => [
      "https://www.polarishare.com/deandean/decompany-1-0-whitepaper-4usqr4",
      "https://www.polarishare.com/Chris Lee/dive-into-icon-iq2ovh",
      "https://www.polarishare.com/Chris Lee/stress-at-work-tips-to-reduce-and-manage-job-and-workplace-stress-qwv0b3",
    ],
    provider => "https://www.polarishare.com/",
    url => ["https://www.polarishare.com/*/*"],
  },
  "PollDaddy" => {
    api => "http://polldaddy.com/oembed/",
    examples => ["http://polldaddy.com/ratings/39/"],
    params => {format => "json"},
    provider => "http://polldaddy.com",
    url => [
      "http://*.polldaddy.com/s/*", "http://*.polldaddy.com/poll/*",
      "http://*.polldaddy.com/ratings/*",
    ],
  },
  "Port" => {
    api => "https://api.sellwithport.com/v1.0/buyer/oembed",
    provider => "http://www.sellwithport.com/",
    url => ["https://app.sellwithport.com/#/buyer/*"],
  },
  "Portfolium" => {
    api => "https://api.portfolium.com/oembed",
    examples => [
      "https://portfolium.com/entry/american-ninja-warrior-2011",
      "https://portfolium.com/entry/american-ninja-warrior-2011",
    ],
    params => {format => "json"},
    provider => "https://portfolium.com",
    url => ["https://portfolium.com/entry/*"],
  },
  "posiXion" => {
    api => "http://posixion.com/services/oembed/",
    examples => [
      "https://posixion.com/question/Is-There-Anything-I-Should-Do-About-Climate-Change",
    ],
    provider => "https://posixion.com/",
    url => [
      "https://posixion.com/question/*",
      "https://posixion.com/*/question/*",
    ],
  },
  "Quiz.biz" => {
    api => "http://www.quiz.biz/api/oembed",
    examples => ["http://www.quiz.biz/quizz-182015.html"],
    params => {format => "json"},
    provider => "http://www.quiz.biz/",
    url => ["http://www.quiz.biz/quizz-*.html"],
  },
  "Quizz.biz" => {
    api => "http://www.quizz.biz/api/oembed",
    examples => ["http://www.quizz.biz/quizz-339842.html"],
    params => {format => "json"},
    provider => "http://www.quizz.biz/",
    url => ["http://www.quizz.biz/quizz-*.html"],
  },
  "RapidEngage" => {
    api => "https://rapidengage.com/api/oembed",
    examples => [
      "https://rapidengage.com/s/6b1faa05",
      "https://rapidengage.com/s/6b1faa05",
    ],
    params => {format => "json"},
    provider => "https://rapidengage.com",
    url => ["https://rapidengage.com/s/*"],
  },
  "Reddit" => {
    api => "https://www.reddit.com/oembed",
    examples => [
      "https://www.reddit.com/r/aww/comments/4lwccv/someone_came_to_visit_woodchips_for_scale/",
      "https://www.reddit.com/r/aww/comments/4lwccv/someone_came_to_visit_woodchips_for_scale/d3qol9a",
    ],
    provider => "https://reddit.com/",
    url => [
      "https://reddit.com/r/*/comments/*/*",
      "https://www.reddit.com/r/*/comments/*/*",
    ],
  },
  "ReleaseWire" => {
    api => "http://publisher.releasewire.com/oembed/",
    examples => ["http://rwire.com/600742"],
    params => {format => "json"},
    provider => "http://www.releasewire.com/",
    url => ["http://rwire.com/*"],
  },
  "Replit" => {
    api => "https://repl.it/data/oembed",
    examples => ["https://repl.it/\@timmy_i_chen/flask-boilerplate?lite=1"],
    params => {format => "json", outputonly => 1},
    provider => "https://repl.it/",
    url => ["https://repl.it/\@*/*"],
  },
  "RepubHub" => {
    api => "http://repubhub.icopyright.net/oembed.act",
    examples => [
      "http://repubhub.icopyright.net/freePost.act?tag=3.11150?icx_id=918814",
    ],
    params => {format => "json"},
    provider => "http://repubhub.icopyright.net/",
    url => ["http://repubhub.icopyright.net/freePost.act?*"],
  },
  "ReverbNation" => {
    api => "https://www.reverbnation.com/oembed",
    examples => [
      "https://www.reverbnation.com/coralbones",
      "https://www.reverbnation.com/coralbones",
      "https://www.reverbnation.com/coralbones/song/4290057-rising-sand",
      "https://www.reverbnation.com/coralbones/song/4290057-rising-sand",
    ],
    params => {format => "json"},
    provider => "https://www.reverbnation.com/",
    url => [
      "https://www.reverbnation.com/*",
      "https://www.reverbnation.com/*/songs/*",
    ],
  },
  "RiffReporter" => {
    api => "https://www.riffreporter.de/service/oembed",
    examples => [
      "https://www.riffreporter.de/was-ist-riffreporter/",
      "https://www.riffreporter.de/was-ist-riffreporter/",
      "https://www.riffreporter.de/was-ist-riffreporter/",
      "https://www.riffreporter.de/was-ist-riffreporter/",
      "https://www.riffreporter.de/was-ist-riffreporter/",
    ],
    params => {service => "json"},
    provider => "https://www.riffreporter.de/",
    url => "https://www.riffreporter.de/*",
  },
  "Roomshare" => {
    api => "http://roomshare.jp/en/oembed.{format}",
    examples => ["http://roomshare.jp/en/post/137167"],
    provider => "http://roomshare.jp",
    url => ["http://roomshare.jp/post/*", "http://roomshare.jp/en/post/*"],
  },
  "RoosterTeeth" => {
    api => "https://roosterteeth.com/oembed",
    examples =>
        ["https://roosterteeth.com/embed/red-vs-blue-season-15-5-a84jh9",],
    params => {format => "json"},
    provider => "https://roosterteeth.com",
    url => ["https://roosterteeth.com/*"],
  },
  "Rumble" => {
    api => "https://rumble.com/api/Media/oembed.{format}",
    examples => [
      "https://rumble.com/v30jzs-dog-dont-know-where-to-hide-her-bone.html",
      "https://rumble.com/v30jzs-dog-dont-know-where-to-hide-her-bone.html",
    ],
    provider => "https://rumble.com/",
    url => "https://rumble.com/*",
  },
  "SapoVideos" => {
    api => "http://videos.sapo.pt/oembed",
    examples => ["http://videos.sapo.pt/dNbiosGa9YZHfLrhkA88"],
    params => {format => "json"},
    provider => "http://videos.sapo.pt",
    url => ["http://videos.sapo.pt/*"],
  },
  "Screen9" => {
    api => "https://api.screen9.com/oembed",
    examples =>
        ["https://videosite.screen9.tv/media/u6txqFxdedOXiyg2lOUmTQ/crane",],
    provider => "http://www.screen9.com/",
    url => ["https://console.screen9.com/*", "https://*.screen9.tv/*"],
  },
  "Screencast.com" => {
    api => "https://api.screencast.com/external/oembed",
    examples => [
      "http://www.screencast.com/users/TechSmith_Media/folders/Camtasia/media/d89af74a-3a32-4c9f-8a85-ef83fdb5c39c",
      "http://www.screencast.com/t/JR3TiP5Dds",
    ],
    params => {format => "json"},
    provider => "http://www.screencast.com/",
    url => "https://www.screencast.com/*",
  },
  "Screenr" => {
    api => "http://www.screenr.com/api/oembed.{format}",
    examples => ["http://screenr.com/3jns"],
    provider => "http://www.screenr.com/",
    url => ["http://www.screenr.com/*/"],
  },
  "ScribbleMaps" => {
    api => "https://scribblemaps.com/api/services/oembed.{format}",
    examples => [
      "https://scribblemaps.com/maps/view/Saigon/JkFLCgwlGt",
      "https://scribblemaps.com/maps/view/Saigon/JkFLCgwlGt",
    ],
    provider => "https://scribblemaps.com",
    url => [
      "http://www.scribblemaps.com/maps/view/*",
      "https://www.scribblemaps.com/maps/view/*",
      "http://scribblemaps.com/maps/view/*",
      "https://scribblemaps.com/maps/view/*",
    ],
  },
  "Scribd" => {
    api => "http://www.scribd.com/services/oembed/",
    examples => [
      "http://www.scribd.com/doc/110799637/Synthesis-of-Knowledge-Effects-of-Fire-and-Thinning-Treatments-on-Understory-Vegetation-in-Dry-U-S-Forests",
    ],
    params => {format => "json"},
    provider => "http://www.scribd.com/",
    url => ["http://www.scribd.com/doc/*"],
  },
  "SendtoNews" => {
    api => "https://embed.sendtonews.com/services/oembed",
    examples => [
      "http://embed.sendtonews.com/oembed/?SC=IuQTVUQ5ro-133019-5892",
      "http://embed.sendtonews.com/oembed/?SC=IuQTVUQ5ro-133019-5892",
    ],
    params => {format => "json"},
    provider => "http://www.sendtonews.com/",
    url => ["https://embed.sendtonews.com/oembed/*"],
  },
  "ShortNote" => {
    api => "https://www.shortnote.jp/oembed/",
    examples => ["https://www.shortnote.jp/view/notes/ATImFCFE"],
    provider => "https://www.shortnote.jp/",
    url => ["https://www.shortnote.jp/view/notes/*"],
  },
  "Shoudio" => {
    api => "http://shoudio.com/api/oembed",
    examples => ["http://shoudio.com/user/shoister/status/8122"],
    params => {format => "json"},
    provider => "http://shoudio.com",
    url => ["http://shoudio.com/*", "http://shoud.io/*"],
  },
  "ShowtheWay,actionablelocationinfo" => {
    api => "https://showtheway.io/oembed",
    examples => [
      "https://showtheway.io/to/48.85837,2.294481?name=Eiffel Tower",
      "https://showtheway.io/to/48.85837,2.294481?name=Eiffel Tower",
    ],
    params => {format => "json"},
    provider => "https://showtheway.io",
    url => ["https://showtheway.io/to/*"],
  },
  "Simplecast" => {
    api => "https://simplecast.com/oembed",
    examples => ["https://simplecast.com/s/7fe152f4"],
    provider => "https://simplecast.com",
    url => ["https://simplecast.com/s/*"],
  },
  "Sizzle" => {
    api => "https://onsizzle.com/oembed",
    examples => [
      "https://onsizzle.com/i/ten-kingiames-last-night-lebron-james-finally-got-that-ring-3174471",
      "https://onsizzle.com/i/ten-kingiames-last-night-lebron-james-finally-got-that-ring-3174471",
    ],
    params => {format => "json"},
    provider => "https://onsizzle.com/",
    url => ["https://onsizzle.com/i/*"],
  },
  "Sketchfab" => {
    api => "http://sketchfab.com/oembed",
    examples => [
      "https://sketchfab.com/models/e7995659092c4d8c92031b0a03887cfa",
      "https://sketchfab.com/sketchfab/folders/5ae73138e4a1477fb87b6f48d2bfccbe",
    ],
    provider => "http://sketchfab.com",
    url => [
      "http://sketchfab.com/models/*", "https://sketchfab.com/models/*",
      "https://sketchfab.com/*/folders/*",
    ],
  },
  "SlideShare" => {
    api => "https://www.slideshare.net/api/oembed/2",
    examples =>
        ["https://www.slideshare.net/haraldf/business-quotes-for-2011"],
    params => {format => "json"},
    provider => "https://www.slideshare.net/",
    url => [
      "https://www.slideshare.net/*/*", "https://fr.slideshare.net/*/*",
      "https://de.slideshare.net/*/*", "https://es.slideshare.net/*/*",
      "https://pt.slideshare.net/*/*",
    ],
  },
  "SmashNotes" => {
    api => "https://smashnotes.com/services/oembed",
    examples => [
      "https://smashnotes.com/p/below-the-line-with-james-beshara/e/1-justin-kan",
    ],
    params => {format => "json"},
    provider => "https://smashnotes.com",
    url => [
      "https://smashnotes.com/p/*",
      "https://smashnotes.com/p/*/e/* - https://smashnotes.com/p/*/e/*/s/*",
    ],
  },
  "SmugMug" => {
    api => "https://api.smugmug.com/services/oembed/",
    examples => ["https://www.smugmug.com/popular/all#125787395_hQSj9"],
    provider => "https://www.smugmug.com/",
    url => ["http://*.smugmug.com/*", "https://*.smugmug.com/*"],
  },
  "SocialExplorer" => {
    api => "https://www.socialexplorer.com/services/oembed/",
    examples => ["https://www.socialexplorer.com/a9676d974c/explore"],
    params => {format => "json"},
    provider => "https://www.socialexplorer.com/",
    url => [
      "https://www.socialexplorer.com/*/explore",
      "https://www.socialexplorer.com/*/view",
      "https://www.socialexplorer.com/*/edit",
      "https://www.socialexplorer.com/*/embed",
    ],
  },
  "Songlink" => {
    api => "https://song.link/oembed",
    examples => [
      "https://song.link/us/i/1182062656",
      "https://song.link/dpmo",
      "https://song.link/album/s/0K4pIOOsfJ9lK8OjrZfXzd",
    ],
    params => {format => "json"},
    provider => "https://song.link",
    url => ["https://song.link/*"],
  },
  "SoundCloud" => {
    api => "https://soundcloud.com/oembed",
    examples => [
      "https://soundcloud.com/forss/flickermood",
      "https://soundcloud.com/forss/flickermood",
    ],
    params => {format => "json"},
    provider => "http://soundcloud.com/",
    url => ["http://soundcloud.com/*", "https://soundcloud.com/*"],
  },
  "Soundsgood" => {
    api => "https://play.soundsgood.co/oembed",
    examples => [
      "https://play.soundsgood.co/playlist/24h-avec-nuits-fauves",
      "https://play.soundsgood.co/playlist/pour-siffloter-sur-les-routes",
      "https://play.soundsgood.co/playlist/nova-soundclash-or-septembre-2016",
    ],
    params => {format => "json"},
    provider => "https://soundsgood.co",
    url => [
      "https://play.soundsgood.co/playlist/*",
      "https://soundsgood.co/playlist/*",
    ],
  },
  "SpeakerDeck" => {
    api => "https://speakerdeck.com/oembed.json",
    examples => ["https://speakerdeck.com/wallat/why-backbone"],
    provider => "https://speakerdeck.com",
    url => ["http://speakerdeck.com/*/*", "https://speakerdeck.com/*/*"],
  },
  "Spotful" => {
    api => "https://api.bespotful.com/oembed",
    examples => [
      "https://play.bespotful.com/3457", "https://play.bespotful.com/3457",
      "https://play.bespotful.com/3457",
    ],
    params => {format => "json"},
    provider => "https://bespotful.com",
    url => ["http://play.bespotful.com/*"],
  },
  "Spotify" => {
    api => "https://embed.spotify.com/oembed/",
    examples => [
      "https://open.spotify.com/track/2qToAcex0ruZfbEbAy9OhW",
      "spotify:artist:7ae4vgLLhir2MCjyhgbGOQ",
    ],
    provider => "https://spotify.com/",
    url => ["https://*.spotify.com/*"],
  },
  "Spreaker" => {
    api => "https://api.spreaker.com/oembed",
    examples => [
      "https://www.spreaker.com/user/9234049/world-of-warcraft-arthas-rise-of-the-lic",
      "https://www.spreaker.com/user/9234049/world-of-warcraft-arthas-rise-of-the-lic",
    ],
    params => {format => "json"},
    provider => "https://www.spreaker.com/",
    url => ["http://*.spreaker.com/*", "https://*.spreaker.com/*"],
  },
  "StanfordDigitalRepository" => {
    api => "https://purl.stanford.edu/embed.{format}",
    examples => [
      "https://purl.stanford.edu/fx361mt5433",
      "https://purl.stanford.edu/fw090jw3474",
      "https://purl.stanford.edu/ky226pt1201",
      "https://purl.stanford.edu/kd948pq9705",
      "https://purl.stanford.edu/cz128vq0535",
    ],
    provider => "https://purl.stanford.edu/",
    url => ["https://purl.stanford.edu/*"],
  },
  "Streamable" => {
    api => "https://api.streamable.com/oembed.json",
    examples => ["http://streamable.com/ifjh"],
    provider => "https://streamable.com/",
    url => ["http://streamable.com/*", "https://streamable.com/*"],
  },
  "StreamOneCloud" => {
    api => "https://content.streamonecloud.net/oembed",
    examples => [
      "https://content.streamonecloud.net/embed/account=2zhpQ4DUe5oB/item=OB5psqlNP0MR/tears-of-steel.html",
    ],
    params => {format => "json"},
    provider => "https://www.streamone.nl",
    url => ["https://content.streamonecloud.net/embed/*"],
  },
  "Sutori" => {
    api => "https://www.sutori.com/api/oembed",
    examples => ["https://www.sutori.com/story/our-story-8362"],
    provider => "https://www.sutori.com/",
    url => ["https://www.sutori.com/story/*"],
  },
  "Sway" => {
    api => "https://sway.com/api/v1.0/oembed",
    examples => [
      "https://sway.com/making_of_wildcat_sculpture",
      "https://sway.com/nLa7rrYhdCmzRyQd",
    ],
    params => {format => "json"},
    provider => "https://www.sway.com",
    url => ["https://sway.com/*", "https://www.sway.com/*"],
  },
  "TED" => {
    api => "https://www.ted.com/services/v1/oembed.{format}",
    examples => [
      "https://www.ted.com/talks/jill_bolte_taylor_s_powerful_stroke_of_insight",
      "https://www.ted.com/talks/jill_bolte_taylor_s_powerful_stroke_of_insight",
    ],
    provider => "https://www.ted.com",
    url => [
      "http://ted.com/talks/*", "https://ted.com/talks/*",
      "https://www.ted.com/talks/*",
    ],
  },
  "TheNewYorkTimes" => {
    api => "https://www.nytimes.com/svc/oembed/json/",
    examples => [
      "http://www.nytimes.com/2016/03/10/us/politics/how-to-watch-democratic-debate.html",
      "https://www.nytimes.com/2017/02/14/business/dealbook/bundling-online-services.html",
    ],
    provider => "https://www.nytimes.com",
    url => [
      "https://www.nytimes.com/svc/oembed", "https://nytimes.com/*",
      "https://*.nytimes.com/*",
    ],
  },
  "TheySaidSo" => {
    api => "https://theysaidso.com/extensions/oembed/",
    examples => ["https://theysaidso.com/i/13IGilhK08STqiDI5xGk_geF"],
    params => {format => "json"},
    provider => "https://theysaidso.com/",
    url => ["https://theysaidso.com/image/*"],
  },
  "TickCounter" => {
    api => "https://www.tickcounter.com/oembed",
    examples => [
      "https://www.tickcounter.com/countdown/1/my-countdown",
      "https://www.tickcounter.com/countdown/1/my-countdown",
    ],
    params => {format => "json"},
    provider => "https://www.tickcounter.com",
    url => [
      "http://www.tickcounter.com/countdown/*",
      "http://www.tickcounter.com/countup/*",
      "http://www.tickcounter.com/ticker/*",
      "http://www.tickcounter.com/worldclock/*",
      "https://www.tickcounter.com/countdown/*",
      "https://www.tickcounter.com/countup/*",
      "https://www.tickcounter.com/ticker/*",
      "https://www.tickcounter.com/worldclock/*",
    ],
  },
  "Toornament" => {
    api => "https://widget.toornament.com/oembed",
    examples => [
      "https://www.toornament.com/tournaments/435927046347886201/information",
    ],
    provider => "https://www.toornament.com/",
    url => [
      "https://www.toornament.com/tournaments/*/information",
      "https://www.toornament.com/tournaments/*/registration/",
      "https://www.toornament.com/tournaments/*/matches/schedule",
      "https://www.toornament.com/tournaments/*/stages/*/",
    ],
  },
  "Topy" => {
    api => "http://www.topy.se/oembed/",
    examples => ["http://topy.se/image/X9&format=json"],
    provider => "http://www.topy.se/",
    url => ["http://www.topy.se/image/*"],
  },
  "Tuxx" => {
    api => "https://www.tuxx.be/services/oembed",
    examples => ["http://www.tuxx.be/nl/feestdagen_en_gedenkdagen/"],
    params => {format => "json"},
    provider => "https://www.tuxx.be/",
    url => ["https://www.tuxx.be/*"],
  },
  "tvcf" => {
    api => "https://play.tvcf.co.kr/rest/oembed",
    examples => ["https://play.tvcf.co.kr/739477"],
    params => {format => "json"},
    provider => "http://tvcf.co.kr",
    url => ["https://play.tvcf.co.kr/*", "https://*.tvcf.co.kr/*"],
  },
  "Twitch" => {
    api => "https://api.twitch.tv/v5/oembed",
    examples => ["https://www.twitch.tv/riotgames/v/72749628"],
    provider => "https://www.twitch.tv",
    url => [
      "http://clips.twitch.tv/*", "https://clips.twitch.tv/*",
      "http://www.twitch.tv/*", "https://www.twitch.tv/*",
      "http://twitch.tv/*", "https://twitch.tv/*",
    ],
  },
  "Twitter" => {
    api => "https://publish.twitter.com/oembed",
    examples => ["https://twitter.com/Interior/status/507185938620219395"],
    provider => "http://www.twitter.com/",
    url => [
      "https://twitter.com/*/status/*",
      "https://*.twitter.com/*/status/*",
    ],
  },
  "TypeCast" => {
    api => "https://play.typecast.ai/oembed",
    examples => [
      "https://play.typecast.ai/s/5cdd8da6f3a83a0007b80b17",
      "https://play.typecast.ai/s/5cdd8da6f3a83a0007b80b17",
    ],
    params => {format => "json"},
    provider => "https://typecast.ai",
    url => [
      "https://play.typecast.ai/s/*", "https://play.typecast.ai/e/*",
      "https://play.typecast.ai/*",
    ],
  },
  "Typlog" => {
    api => "https://typlog.com/oembed",
    examples => ["https://fourgifts.typlog.io/episodes/11"],
    provider => "https://typlog.com",
    url => "https://typlog.com/*",
  },
  "Ubideo" => {
    api => "https://player.ubideo.com/api/oembed.json",
    examples => ["https://player.ubideo.com/myownusername"],
    provider => "https://player.ubideo.com/",
    url => ["https://player.ubideo.com/*"],
  },
  "UniversityofCambridgeMap" => {
    api => "https://map.cam.ac.uk/oembed/",
    examples => ["https://map.cam.ac.uk/Department+of+Geography"],
    provider => "https://map.cam.ac.uk",
    url => ["https://map.cam.ac.uk/*"],
  },
  "UnivParis1.Pod" => {
    api => "https://mediatheque.univ-paris1.fr/oembed",
    examples => [
      "https://mediatheque.univ-paris1.fr/video/1839-revue-1257-n1-eclairages-sur-le-cinema/",
      "https://mediatheque.univ-paris1.fr/video/1839-revue-1257-n1-eclairages-sur-le-cinema/",
    ],
    params => {format => "json"},
    provider => "https://mediatheque.univ-paris1.fr/",
    url => ["https://mediatheque.univ-paris1.fr/video/*"],
  },
  "UOL" => {
    api => "https://mais.uol.com.br/apiuol/v3/oembed/view",
    examples => [
      "https://mais.uol.com.br/view/qf3ks0vlifm7/15697800?types=A",
      "https://tvuol.uol.com.br/video/whatsapp-dos-astros-valdivia-messi-e-neymar-na-resenha-das-eliminatorias-04024E1A3762DC896326",
      "https://videos.bol.uol.com.br/video/filha-do-datena-na-playboy-e-silvio-platinado-veja-quem-deu-o-que-falar-0402CD1B3064DC896326",
    ],
    params => {format => "json"},
    provider => "https://mais.uol.com.br/",
    url => ["https://*.uol.com.br/view/*", "https://*.uol.com.br/video/*"],
  },
  "Ustream" => {
    api => "http://www.ustream.tv/oembed",
    examples => ["http://www.ustream.tv/channel/americatv2oficial"],
    provider => "http://www.ustream.tv",
    url => ["http://*.ustream.tv/*", "http://*.ustream.com/*"],
  },
  "uStudio,Inc." => {
    api => "https://app.ustudio.com/api/v2/oembed",
    examples => [
      "https://embed.ustudio.com/embed/DhExfAxGHFYz/U8X71S93cklU",
      "https://embed.ustudio.com/embed/DgOC4s9QYIag",
      "https://authorized-embed.ustudio.com/embed/DgwP33zqbPXD/U8X71S93cklU",
      "https://authorized-embed.ustudio.com/embed/DWe7KApmMXBZ",
    ],
    params => {share => "false"},
    provider => "https://www.ustudio.com",
    url =>
        ["https://*.ustudio.com/embed/*", "https://*.ustudio.com/embed/*/*",],
  },
  "Utposts" => {
    api => "https://www.utposts.com/api/oembed",
    examples => ["https://utposts.com/products/1"],
    provider => "https://www.utposts.com/",
    url => [
      "https://www.utposts.com/products/*",
      "http://www.utposts.com/products/*",
      "https://utposts.com/products/*",
      "http://utposts.com/products/*",
    ],
  },
  "Uttles" => {
    api => "http://uttles.com/api/reply/oembed",
    examples => [
      "http://uttles.com/uttle/56b760264daebfd94ef293a2",
      "http://uttles.com/uttle/56b760264daebfd94ef293a2",
    ],
    params => {format => "json"},
    provider => "http://uttles.com",
    url => ["http://uttles.com/uttle/*"],
  },
  "VeeRVR" => {
    api => "https://api.veer.tv/oembed",
    examples => [
      "http://veer.tv/videos/fuzzy-beard-360-7514",
      "http://veer.tv/videos/fuzzy-beard-360-7514",
    ],
    params => {format => "json"},
    provider => "http://veer.tv/",
    url => ["http://veer.tv/videos/*"],
  },
  "Verse" => {
    api => "http://verse.com/services/oembed/",
    examples => [
      "http://verse.com/embed/#/stories/112-connected-to-the-top",
      "http://verse.com/embed/#/stories/112-connected-to-the-top",
    ],
    params => {format => "json"},
    provider => "http://verse.com/",
    url => "https://verse.com/*",
  },
  "VEVO" => {
    api => "https://www.vevo.com/oembed",
    examples =>
        ["http://www.vevo.com/watch/katy-perry/Firework/USCA31000112"],
    provider => "http://www.vevo.com/",
    url => ["http://www.vevo.com/*", "https://www.vevo.com/*"],
  },
  "VideoJug" => {
    api => "http://www.videojug.com/oembed.{format}",
    examples => ["http://www.videojug.com/film/how-to-tie-a-knot-braid"],
    provider => "http://www.videojug.com",
    url => [
      "http://www.videojug.com/film/*",
      "http://www.videojug.com/interview/*",
    ],
  },
  "Vidlit" => {
    api => "https://api.vidl.it/oembed",
    examples => ["https://vidl.it/mBPb4A", "https://vidl.it/mBPb4A"],
    params => {format => "json"},
    provider => "https://vidl.it/",
    url => ["https://vidl.it/*"],
  },
  "Vidmizer" => {
    api => "https://app-v2.vidmizer.com/api/oembed",
    examples => [
      "https://players.vidmizer.com/8582f97e-7c4f-49c7-be85-d61a95f4d8b3",
    ],
    provider => "https://www.vidmizer.com/",
    url => ["https://players.vidmizer.com/*"],
  },
  "Vidyard" => {
    api => "https://api.vidyard.com/dashboard/v1.1/oembed",
    examples => ["http://play.vidyard.com/watch/3DiwGFalTRHDA"],
    provider => "http://www.vidyard.com",
    url => [
      "http://embed.vidyard.com/*", "http://play.vidyard.com/*",
      "http://share.vidyard.com/*", "http://*.hubs.vidyard.com/*",
    ],
  },
  "Vimeo" => {
    api => "https://vimeo.com/api/oembed.{format}",
    examples => ["http://vimeo.com/76979871", "http://vimeo.com/76979871"],
    provider => "https://vimeo.com/",
    url => [
      "https://vimeo.com/*",
      "https://vimeo.com/album/*/video/*",
      "https://vimeo.com/channels/*/*",
      "https://vimeo.com/groups/*/videos/*",
      "https://vimeo.com/ondemand/*/*",
      "https://player.vimeo.com/video/*",
    ],
  },
  "Viziosphere" => {
    api => "http://viziosphere.com/services/oembed/",
    examples => ["http://viziosphere.com/3dphoto?ref=VZP0002"],
    provider => "http://www.viziosphere.com",
    url => ["http://viziosphere.com/3dphoto*"],
  },
  "Vizydrop" => {
    api => "https://vizydrop.com/oembed",
    examples => [
      "https://vizydrop.com/shared/drop/5ca750de3ce84f0016033c19?authkey=b60edc7affeb3a046e50",
    ],
    provider => "https://vizydrop.com",
    url => ["https://vizydrop.com/shared/*"],
  },
  "Vlipsy" => {
    api => "https://vlipsy.com/oembed",
    examples => [
      "https://vlipsy.com/vlip/elf-i-love-you-i1ZZELDO",
      "https://vlipsy.com/vlip/elf-i-love-you-i1ZZELDO",
    ],
    params => {format => "json"},
    provider => "https://vlipsy.com/",
    url => ["https://vlipsy.com/*"],
  },
  "VLIVE" => {
    api => "https://www.vlive.tv/oembed",
    examples => ["https://www.vlive.tv/video/81492"],
    provider => "https://www.vlive.tv",
    url => ["https://www.vlive.tv/video/*"],
  },
  "Vlurb" => {
    api => "https://vlurb.co/oembed.json",
    examples => ["https://vlurb.co/video/c0xphu"],
    provider => "https://www.vlurb.co/",
    url => ["http://vlurb.co/video/*", "https://vlurb.co/video/*"],
  },
  "VoxSnap" => {
    api => "https://data.voxsnap.com/oembed",
    examples => [
      "https://article.voxsnap.com/nirandfar/the-psychology-of-a-billion-dollar-enterprise-app",
    ],
    provider => "https://voxsnap.com/",
    url => ["https://article.voxsnap.com/*/*"],
  },
  "wecandeo" => {
    api => "http://play.wecandeo.com/oembed",
    params => {format => "json"},
    provider => "http://www.wecandeo.com/",
    url => "https://www.wecandeo.com/*",
  },
  "Wiredrive" => {
    api => "http://*.wiredrive.com/present-oembed/",
    examples =>
        ["deckers.wiredrive.com/363254/851732644105a5a8b3fa14fe164452df",],
    provider => "https://www.wiredrive.com/",
    url => ["https://*.wiredrive.com/*"],
  },
  "Wistia,Inc." => {
    api => "https://fast.wistia.com/oembed.{format}",
    examples => [
      "https://home.wistia.com/medias/xfepf8u5c4",
      "https://home.wistia.com/medias/xfepf8u5c4",
      "https://fast.wistia.com/embed/iframe/xfepf8u5c4",
      "https://fast.wistia.com/embed/iframe/xfepf8u5c4",
    ],
    provider => "https://wistia.com/",
    url => [
      "https://fast.wistia.com/embed/iframe/*",
      "https://fast.wistia.com/embed/playlists/*",
      "https://*.wistia.com/medias/*",
    ],
  },
  "wizer.me" => {
    api => "http://app.wizer.me/api/oembed.{format}",
    examples => [
      "https://app.wizer.me/preview/K6EKW",
      "https://app.wizer.me/preview/K6EKW",
    ],
    provider => "http://www.wizer.me/",
    url => [
      "http://*.wizer.me/learn/*", "https://*.wizer.me/learn/*",
      "http://*.wizer.me/preview/*", "https://*.wizer.me/preview/*",
    ],
  },
  "Wootled" => {
    api => "http://www.wootled.com/oembed",
    examples => ["http://www.wootled.com/wg/0SbDvPCAzpWEstt"],
    provider => "http://www.wootled.com/",
    url => "https://www.wootled.com/*",
  },
  "WordPress.com" => {
    api => "http://public-api.wordpress.com/oembed/",
    examples =>
        ["http://matt.wordpress.com/2011/07/14/clouds-over-new-york/"],
    params => {format => "json"},
    provider => "http://wordpress.com/",
    url => "https://wordpress.com/*",
  },
  "Xpression" => {
    api => "https://web.xpression.jp/api/oembed",
    examples => [
      "https://web.xpression.jp/video/pr-12-12",
      "https://web.xpression.jp/video/pr-12-12",
    ],
    params => {format => "json"},
    provider => "https://web.xpression.jp",
    url => ["https://web.xpression.jp/video/*"],
  },
  "Yes,IKnowIT!" => {
    api => "http://yesik.it/s/oembed",
    examples => ["http://yesik.it/EP15"],
    provider => "http://yesik.it",
    url => ["http://yesik.it/*", "http://www.yesik.it/*"],
  },
  "YFrog" => {
    api => "http://www.yfrog.com/api/oembed",
    examples => ["http://yfrog.com/jukynnj"],
    provider => "http://yfrog.com/",
    url => ["http://*.yfrog.com/*", "http://yfrog.us/*"],
  },
  "YouTube" => {
    api => "https://www.youtube.com/oembed",
    examples => [
      "http://www.youtube.com/watch?v=iwGFalTRHDA",
      "http://www.youtube.com/watch?v=iwGFalTRHDA",
    ],
    params => {format => "json"},
    provider => "https://www.youtube.com/",
    url => [
      "https://*.youtube.com/watch*", "https://*.youtube.com/v/*",
      "https://youtu.be/*",
    ],
  },
  "ZingSoft" => {
    api => "https://app.zingsoft.com/oembed",
    examples => [
      "https://app.zingsoft.com/oembed?url=https://app.zingsoft.com/demos/view/1PFW8TP3",
    ],
    provider => "https://app.zingsoft.com",
    url => [
      "https://app.zingsoft.com/embed/*",
      "https://app.zingsoft.com/view/*",
    ],
  },
  "ZnipeTV" => {
    api => "https://api.znipe.tv/v3/oembed/",
    examples => [
      "https://beta.znipe.tv/esl-genting-2018/stage?v=-L8UwcDwy8BFKXR6lLdj",
    ],
    provider => "https://www.znipe.tv/",
    url => ["https://*.znipe.tv/*"],
  },
};

1;
