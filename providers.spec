$Foswiki::cfg{OEmbedPlugin}{Providers} = { 
  "23HQ" => {
    api => "http://www.23hq.com/23/oembed",
    examples => ["http://www.23hq.com/mprove/photo/13297717"],
    provider => "http://www.23hq.com",
    url => ["http://www.23hq.com/*/photo/*"],
  },
  "3Q" => {
    api => "https://playout.3qsdn.com/oembed",
    examples => ["f03b2c43-fa42-47f6-8106-8f39cbf8661b"],
    params => {format => "json"},
    provider => "https://3q.video/",
    url => ["https://playout.3qsdn.com/embed/*"],
  },
  "Abraia" => {
    api => "https://api.abraia.me/oembed",
    examples => ["https://store.abraia.me/demo/videos/sample/index.html"],
    provider => "https://abraia.me",
    url => ["https://store.abraia.me/*"],
  },
  "Acast" => {
    api => "https://oembed.acast.com/v1/embed-player",
    examples => [
      "https://play.acast.com/s/go-off-sis/keepthatsameenergyfeat.kekepalmer",
    ],
    provider => "https://embed.acast.com",
    url => ["https://play.acast.com/s/*"],
  },
  "ActBlue" => {
    api => "https://secure.actblue.com/cf/oembed",
    examples => ["https://secure.actblue.com/donate/actblue-1-embed"],
    provider => "https://secure.actblue.com",
    url => ["https://secure.actblue.com/donate/*"],
  },
  "Adilo" => {
    api => "https://adilo.bigcommand.com/web/oembed",
    examples => ["https://adilo.bigcommand.com/watch/7DmeLyjk"],
    params => {format => "json"},
    provider => "https://adilo.bigcommand.com",
    url => ["https://adilo.bigcommand.com/watch/*"],
  },
  "afreecaTV" => {
    api => "https://openapi.afreecatv.com/oembed/embedinfo",
    examples => [
      "https://vod.afreecatv.com/player/71021072",
      "https://play.afreecatv.com/afstar1/237663862",
    ],
    provider => "https://www.afreecatv.com",
    url => [
      "https://vod.afreecatv.com/player/",
      "https://v.afree.ca/ST/",
      "https://vod.afreecatv.com/ST/",
      "https://vod.afreecatv.com/PLAYER/STATION/",
      "https://play.afreecatv.com/",
    ],
  },
  "AltiumLLC" => {
    api => "https://viewer.altium.com/shell/oembed",
    examples => ["https://altium.com/viewer/vN8in6nli06imztWoTol4w=="],
    provider => "https://altium.com",
    url => ["https://altium.com/viewer/*"],
  },
  "Altru" => {
    api => "https://api.altrulabs.com/api/v1/social/oembed",
    examples => [
      "https://app.altrulabs.com/talentbrand/feed?answer_id=2059",
      "https://app.altrulabs.com/player/41329",
    ],
    provider => "https://www.altrulabs.com",
    url => [
      "https://app.altrulabs.com/*/*?answer_id=*",
      "https://app.altrulabs.com/player/*",
    ],
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
  "Amtraker" => {
    api => "https://api.amtraker.com/v3/oembed",
    examples => [
      "https://amtraker.com/trains/9999",
      "https://amtraker.com/trains/9999/22",
      "https://amtraker.com/trains/9999",
      "https://amtraker.com/trains/9999/22",
    ],
    params => {format => "json"},
    provider => "https://amtraker.com",
    url => [
      "https://amtraker.com/trains/*",
      "https://amtraker.com/trains/*/*",
      "https://*.amtraker.com/trains/*",
      "https://*.amtraker.com/trains/*/*",
    ],
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
  "AnnieMusic" => {
    api => "https://api.anniemusic.app/api/v1/oembed",
    examples => ["https://anniemusic.app/t/XDSOYMAnVG"],
    provider => "https://anniemusic.app",
    url => ["https://anniemusic.app/t/*", "https://anniemusic.app/p/*"],
  },
  "ArcGISStoryMaps" => {
    api => "https://storymaps.arcgis.com/oembed",
    examples => [
      "https://storymaps.arcgis.com/stories/ffdd1f0589434e8c8cf0dddbb1edd364",
      "https://storymaps.arcgis.com/stories/ffdd1f0589434e8c8cf0dddbb1edd364",
    ],
    params => {format => "json"},
    provider => "https://storymaps.arcgis.com",
    url => ["https://storymaps.arcgis.com/stories/*"],
  },
  "Archivos" => {
    api => "https://app.archivos.digital/oembed/",
    examples => ["https://app.archivos.digital/app/view/709/?embed"],
    provider => "https://app.archivos.digital",
    url => ["https://app.archivos.digital/app/view/*"],
  },
  "AssemblrWorld" => {
    api => "https://studio.assemblrworld.com/api/oembed",
    examples => [
      "https://localhost:3003/Embed/-9ZYparJxjTEbQZwxYXU?info=false&hideCloseBtn=true",
    ],
    provider => "https://assemblrworld.com/",
    url => [
      "http://*.studio.assemblrworld.com/creation/*",
      "http://studio.assemblrworld.com/creation/*",
      "http://*.app-edu.assemblrworld.com/Creation/*",
      "http://app-edu.assemblrworld.com/Creation/*",
      "http://assemblr.world/*",
      "http://editor.assemblrworld.com/*",
      "http://*.assemblrworld.com/creation/*",
      "http://*.assemblrworld.com/Creation/*",
      "https://*.studio.assemblrworld.com/creation/*",
      "https://studio.assemblrworld.com/creation/*",
      "https://*.app-edu.assemblrworld.com/Creation/*",
      "https://app-edu.assemblrworld.com/Creation/*",
      "https://assemblr.world/*",
      "https://editor.assemblrworld.com/*",
      "https://*.assemblrworld.com/creation/*",
      "https://*.assemblrworld.com/Creation/*",
    ],
  },
  "audio.com" => {
    api => "https://api.audio.com/oembed",
    examples => [
      "https://audio.com/embed/audio/1760622602932096?theme=image",
      "https://audio.com/audio-com/collections/ambient-focus",
    ],
    params => {format => "json"},
    provider => "https://audio.com/",
    url => [
      "https://audio.com/*", "https://www.audio.com/*",
      "http://audio.com/*", "http://www.audio.com/*",
    ],
  },
  "Audioboom" => {
    api => "https://audioboom.com/publishing/oembed.{format}",
    examples => [
      "https://audioboom.com/channels/4971939",
      "https://audioboom.com/channels/4971939",
      "https://audioboom.com/channel/casefile-true-crime",
      "https://audioboom.com/channel/casefile-true-crime",
      "https://audioboom.com/posts/7193185-stephen-merchant",
      "https://audioboom.com/posts/7193185-stephen-merchant",
    ],
    provider => "https://audioboom.com",
    url => [
      "https://audioboom.com/channels/*",
      "https://audioboom.com/channel/*",
      "https://audioboom.com/playlists/*",
      "https://audioboom.com/podcasts/*",
      "https://audioboom.com/podcast/*",
      "https://audioboom.com/posts/*",
      "https://audioboom.com/episodes/*",
    ],
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
    api => "https://audiomack.com/oembed",
    examples => ["https://audiomack.com/audiomack/playlist/just-chillin"],
    params => {format => "json"},
    provider => "https://audiomack.com",
    url => [
      "https://audiomack.com/*/song/*",
      "https://audiomack.com/*/album/*",
      "https://audiomack.com/*/playlist/*",
    ],
  },
  "Audiomeans" => {
    api => "https://podcasts.audiomeans.fr/services/oembed",
    examples => [
      "https://podcasts.audiomeans.fr/player-v2/anti-brouillard-6340b48dedde/episodes/4e490cb9-41fe-48f2-9781-ee0354917c74?color=871f78",
    ],
    provider => "https://audiomeans.fr",
    url => ["https://podcasts.audiomeans.fr/*"],
  },
  "Audius" => {
    api => "https://audius.co/oembed",
    examples => ["https://audius.co/Skrillex/kliptown-empyrean-98562"],
    provider => "https://audius.co",
    url => ["https://audius.co/*"],
  },
  "Backtracks" => {
    api => "https://backtracks.fm/oembed",
    examples => [
      "https://backtracks.fm/ycombinator/ycombinator/e/4-elon-musk-on-how-to-build-the-future",
      "https://backtracks.fm/discover/s/the-joe-rogan-experience/6b8581415e041967/e/1411-robert-downey-jr/77d2d79586e78c01?oref=btdatadir",
    ],
    params => {format => "json"},
    provider => "https://backtracks.fm",
    url => [
      "https://backtracks.fm/*/*/e/*",
      "https://backtracks.fm/*/s/*/*",
      "https://backtracks.fm/*/*/*/*/e/*/*",
      "https://backtracks.fm/*",
      "http://backtracks.fm/*",
    ],
  },
  "BalsamiqCloud" => {
    api => "https://balsamiq.cloud/oembed",
    examples => ["https://balsamiq.cloud/s2ow8jo/po58uiw"],
    params => {format => "json"},
    provider => "https://balsamiq.cloud/",
    url => ["https://balsamiq.cloud/*"],
  },
  "Beams.fm" => {
    api => "https://api.beams.fm/oEmbed",
    examples =>
        ["https://beams.fm/chamberlaincoffee/kIxlbOMMQqSaer90DDOYF6w"],
    provider => "http://beams.fm",
    url => ["https://beams.fm/*"],
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
  "Behance" => {
    api => "https://www.behance.net/services/oembed",
    examples => [
      "https://www.behance.net/gallery/183422265/ydhy",
      "https://www.behance.net/imjessicatr/services/63797/I-will-design-your-brand-s-social-media",
    ],
    provider => "https://www.behance.net",
    url => [
      "https://www.behance.net/gallery/*/*",
      "https://www.behance.net/*/services/*/*",
    ],
  },
  "BetaQuellenSuche" => {
    api => "http://beta.quellensuche.de/api/oembed",
    examples =>
        ["https://beta.quellensuche.de/quelle/6868f92ffd285c6f1e3e9f22",],
    params => {format => "json"},
    provider => "http://beta.quellensuche.de",
    url => ["http://beta.quellensuche.de/*"],
  },
  "biqnetwork" => {
    api => "https://biqapp.com/api/v1/video/oembed",
    examples => [
      "https://cloud.biqapp.com/387214522072432640/Valorant_03-22-2024_23-3-21-702.mp4",
    ],
    params => {format => "json"},
    provider => "https://biqapp.com/",
    url => ["https://cloud.biqapp.com/*"],
  },
  "Bitchute" => {
    api => "https://api.bitchute.com/oembed/",
    examples => ["https://www.bitchute.com/video/ApixlwN8WoA/"],
    params => {format => "json"},
    provider => "https://bitchute.com/",
    url => "https://bitchute.com/*",
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
  "BlueskySocial" => {
    api => "https://embed.bsky.app/oembed",
    examples => [
      "https://bsky.app/profile/did:plc:vjug55kidv6sye7ykr5faxxn/post/3jzn6g7ixgq2y",
      "https://bsky.app/profile/emilyliu.me/post/3jzn6g7ixgq2y",
    ],
    params => {format => "json"},
    provider => "https://bsky.app",
    url => ["https://bsky.app/profile/*/post/*"],
  },
  "Bookingmood" => {
    api => "https://bookingmood.com/api/oembed",
    examples => [
      "https://www.bookingmood.com/embed/search/cb8ea5f0-c766-4dd4-913e-fa2ec0db4dee",
      "https://www.bookingmood.com/embed/search/cb8ea5f0-c766-4dd4-913e-fa2ec0db4dee",
    ],
    params => {format => "json"},
    provider => "https://www.bookingmood.com",
    url => ["https://www.bookingmood.com/embed/*/*"],
  },
  "Bornetube" => {
    api => "https://www.bornetube.dk/media/lasync/oembed/",
    examples => [
      "https://www.bornetube.dk/media/1345406/91hxqgvbcdn32niy9d4hq8r4dxyg8xvb1ebm719f",
      "https://www.bornetube.dk/media/1345406/91hxqgvbcdn32niy9d4hq8r4dxyg8xvb1ebm719f",
    ],
    params => {format => "json"},
    provider => "https://www.bornetube.dk/",
    url => [
      "https://www.bornetube.dk/media/*",
      "https://www.bornetube.dk/video/*",
    ],
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
  "Bumper" => {
    api => "https://www.bumper.com/oembed/bumper",
    examples => [
      "https://www.bumper.com/marketplace-s/pr-286/indexhtml#/listing/222618920",
    ],
    params => {format => "json"},
    provider => "http://www.bumper.com",
    url => [
      "https://www.bumper.com/oembed/bumper",
      "https://www.bumper.com/oembed-s/bumper",
    ],
  },
  "Bunny" => {
    api => "https://video.bunnycdn.com/OEmbed",
    examples => [
      "https://iframe.mediadelivery.net/embed/51808/68d791f4-510a-4928-9f5a-4526e82d1336",
    ],
    provider => "https://bunny.net/",
    url => [
      "https://iframe.mediadelivery.net/*",
      "http://iframe.mediadelivery.net/*",
      "https://video.bunnycdn.com/*",
      "http://video.bunnycdn.com/*",
    ],
  },
  "Buttondown" => {
    api => "https://buttondown.email/embed",
    examples => ["https://buttondown.email/jmduke"],
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
  "Canva" => {
    api => "https://www.canva.com/_oembed",
    examples => ["https://www.canva.com/design/DACHZTlgWkU/view"],
    provider => "https://www.canva.com",
    url => ["https://www.canva.com/design/*/view"],
  },
  "Carbon" => {
    api => "https://carbon.music/oembed",
    examples =>
        ["https://carbon.music/track/db76bcc5-56e8-407c-bedd-7b74d4e7b066",],
    provider => "https://carbon.music/",
    url => ["https://carbon.music/*", "https://www.carbon.music/*"],
  },
  "CardinalBlue" => {
    api => "https://minesweeper.today/api/oembed",
    examples => ["https://minesweeper.today/"],
    params => {format => "json"},
    provider => "https://minesweeper.today/",
    url => ["http://minesweeper.today/*", "https://minesweeper.today/*"],
  },
  "castmake" => {
    api => "http://castmake-ai.com/api/embed",
    examples => [
      "https://www.castmake-ai.com/c/YnEibJ16Y4D4Be5vdmZ5/episodes/N3R5cypdRi6kwRTD86jy",
    ],
    provider => "https://www.castmake-ai.com",
    url => ["https://www.castmake-ai.com/c/*/episodes/*"],
  },
  "CatBoat" => {
    api => "http://img.catbo.at/oembed.json",
    examples =>
        ["http://img.catbo.at/3fb93c1b7891aedb18aa41fb325cbc92e82e58a1.jpg",],
    params => {format => "json"},
    provider => "http://img.catbo.at/",
    url => ["http://img.catbo.at/*"],
  },
  "Celero" => {
    api => "https://api.celero.io/api/oembed",
    examples => ["https://embeds.celero.io/s/7b9ee071"],
    params => {format => "json"},
    provider => "https://www.celero.io",
    url => ["https://embeds.celero.io/*"],
  },
  "Ceros" => {
    api => "http://view.ceros.com/oembed",
    examples => [
      "https://view.ceros.com/ceros/new-experience-3",
      "https://view.ceros.com/ceros-inspire/fendi-desktop-4",
      "https://view.ceros.com/creative-services/sdk",
    ],
    provider => "http://www.ceros.com/",
    url => ["http://view.ceros.com/*", "https://view.ceros.com/*"],
  },
  "Chainflix" => {
    api => "https://www.chainflix.net/video/oembed",
    examples => [
      "https://www.chainflix.net/video/?contentId=1310",
      "https://www.chainflix.net/video/?contentId=1310",
      "https://www.chainflix.net/video/?contentId=1310",
    ],
    params => {format => "json"},
    provider => "https://chainflix.net",
    url => [
      "https://chainflix.net/video/*",
      "https://chainflix.net/video/embed/*",
      "https://*.chainflix.net/video/*",
      "https://*.chainflix.net/video/embed/*",
    ],
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
  "CHROCO" => {
    api => "https://chroco.ooo/embed",
    examples =>
        ["https://chroco.ooo/story/ee261faa-2127-4a30-bd12-8656bb0786f0",],
    provider => "https://chroco.ooo/",
    url => ["https://chroco.ooo/mypage/*", "https://chroco.ooo/story/*"],
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
  "CoCoCorp" => {
    api => "https://app.ilovecoco.video/api/oembed.{format}",
    examples => [
      "https://app.ilovecoco.video/m4p4YNGyKR9fmNpgwozX/embed",
      "https://app.ilovecoco.video/m4p4YNGyKR9fmNpgwozX/embed",
    ],
    provider => "https://ilovecoco.video",
    url => ["https://app.ilovecoco.video/*/embed"],
  },
  "CodeHS" => {
    api => "https://codehs.com/api/sharedprogram/1/oembed/",
    examples =>
        ["https://codehs.com/editor/share_abacus/xtOPDik2wNFjSDUoyl2T",],
    provider => "http://www.codehs.com",
    url => ["https://codehs.com/editor/share_abacus/*"],
  },
  "CodePen" => {
    api => "https://codepen.io/api/oembed",
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
  "Crumb.sh" => {
    api => "https://crumb.sh/oembed/",
    examples => ["https://crumb.sh/QdrfCWZeXKu"],
    params => {format => "json"},
    provider => "https://crumb.sh",
    url => ["https://crumb.sh/*"],
  },
  "CueupDJBooking" => {
    api => "https://gql.cueup.io/oembed",
    examples => [
      "https://cueup.io/user/spinso/sounds/111_housie-bousie",
      "https://cueup.io/user/spinso/sounds/soundcloud-215863477_house-mixtape",
    ],
    params => {format => "json"},
    provider => "https://cueup.io",
    url => ["https://cueup.io/user/*/sounds/*"],
  },
  "Curated" => {
    api => "https://api.curated.co/oembed",
    examples => ["https://optinweekly.curated.co"],
    provider => "https://curated.co/",
    url => ["https://*.curated.co/*"],
  },
  "CustomerDB" => {
    api => "https://app.customerdb.com/embed",
    examples => ["https://app.customerdb.com/share/e7f70c84a1f64557"],
    provider => "http://customerdb.com/",
    url => ["https://app.customerdb.com/share/*"],
  },
  "dadan" => {
    api => "https://app.dadan.io/api/video/oembed",
    examples => [
      "https://app.dadan.io/video/share/N8Hcbu0F1Du3ugmI",
      "https://app.dadan.io/video/share/N8Hcbu0F1Du3ugmI",
    ],
    params => {format => "json"},
    provider => "https://www.dadan.io",
    url => ["https://app.dadan.io/*", "https://stage.dadan.io/*"],
  },
  "Dailymotion" => {
    api => "https://www.dailymotion.com/services/oembed",
    examples =>
        ["http://www.dailymotion.com/video/xoxulz_babysitter_animals"],
    params => {format => "json"},
    provider => "https://www.dailymotion.com",
    url => [
      "https://www.dailymotion.com/video/*",
      "https://geo.dailymotion.com/player.html?video=*",
    ],
  },
  "DALEXNI" => {
    api => "https://dalexni.com/oembed/",
    examples => [
      "https://dalexni.com/i/costa-rica.DT0",
      "https://dalexni.com/i/costa-rica.DT0",
    ],
    params => {format => "json"},
    provider => "https://dalexni.com/",
    url => ["https://dalexni.com/i/*"],
  },
  "Datawrapper" => {
    api => "https://api.datawrapper.de/v3/oembed/",
    examples => ["https://datawrapper.dwcdn.net/RnWgL/9/"],
    provider => "http://www.datawrapper.de",
    url => ["https://datawrapper.dwcdn.net/*"],
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
      "https://sta.sh/*", "https://*.deviantart.com/*#/d*",
    ],
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
  "DocDroid" => {
    api => "https://www.docdroid.net/api/oembed",
    examples =>
        ["https://www.docdroid.net/hptvUCe/example-document.docx.html",],
    provider => "https://www.docdroid.net/",
    url => [
      "https://*.docdroid.net/*", "http://*.docdroid.net/*",
      "https://docdro.id/*", "http://docdro.id/*",
      "https://*.docdroid.com/*", "http://*.docdroid.com/*",
    ],
  },
  "Docswell" => {
    api => "https://www.docswell.com/service/oembed",
    examples => ["https://www.docswell.com/s/ku-suke/LK7J5V-hello-docswell"],
    provider => "https://docswell.com",
    url => [
      "http://docswell.com/s/*/*", "https://docswell.com/s/*/*",
      "http://www.docswell.com/s/*/*", "https://www.docswell.com/s/*/*",
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
  "DreamBroker" => {
    api => "https://dreambroker.com/channel/oembed",
    examples => ["https://www.dreambroker.com/channel/lelk6szy/pt429u1j"],
    provider => "https://dreambroker.com",
    url => ["https://www.dreambroker.com/channel/*/*"],
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
  "EchoesHQ" => {
    api => "https://api.echoeshq.com/oembed",
    examples => [
      "https://app.echoeshq.com/embed/delivery/score-card?tid=c9e1d942-eafd-4496-9849-f964701c8944&p=r4w",
      "https://app.echoeshq.com/embed/delivery/score-card?tid=c9e1d942-eafd-4496-9849-f964701c8944&p=r4w",
    ],
    params => {format => "json"},
    provider => "https://echoeshq.com",
    url => ["http://app.echoeshq.com/embed/*"],
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
  "ElevenLabs" => {
    api => "https://elevenlabs.io/next/oembed",
    examples => [
      "https://elevenlabs.io/music/songs/icz6HAmzkcw2dHMdzaAC",
      "https://elevenlabs.io/music/songs/FGuqsn7mM2ZeFec4uBpp",
    ],
    provider => "https://elevenlabs.io/",
    url => ["https://elevenlabs.io/*"],
  },
  "Embedery" => {
    api => "https://embedery.com/api/oembed",
    examples => ["https://embedery.com/widget/SzjWkZdPCPYb9iQ0FfwA"],
    provider => "https://embedery.com/",
    url => ["https://embedery.com/widget/*"],
  },
  "Ethfiddle" => {
    api => "https://ethfiddle.com/services/oembed/",
    examples => ["https://ethfiddle.com/Y8Iy49zDJ0"],
    params => {format => "json"},
    provider => "https://www.ethfiddle.com/",
    url => ["https://ethfiddle.com/*"],
  },
  "EventLive" => {
    api => "https://evt.live/api/oembed",
    examples => ["https://evt.live/mail8099/wedding-sample"],
    params => {format => "json"},
    provider => "https://eventlive.pro",
    url => [
      "https://evt.live/*", "https://evt.live/*/*",
      "https://live.eventlive.pro/*", "https://live.eventlive.pro/*/*",
    ],
  },
  "everviz" => {
    api => "https://api.everviz.com/oembed",
    examples => ["https://app.everviz.com/embed/R8jhGkYT5"],
    provider => "https://everviz.com",
    url => [
      "https://app.everviz.com/embed/*", "http://app.everviz.com/embed/*",
    ],
  },
  "Everwall" => {
    api => "https://cdn.everwall.com/hubs/oembed",
    examples => ["https://cdn.everwall.com/hubs/iframe/bkvlmdck/tcruu1cpb9/"],
    provider => "https://everwall.com",
    url => ["https://cdn.everwall.com/hubs/iframe/*"],
  },
  "Ex.Co" => {
    api => "https://oembed.ex.co/item",
    examples => [
      "https://app.ex.co/stories/item/8fb2343f-fa5d-48d4-8723-f8b5d51cc1a9",
      "https://app.ex.co/stories/paolagarcia10/remembering-september-11th-flash-back-to-images-we-will-never-forget",
      "https://www.playbuzz.com/paolagarcia10/remembering-september-11th-flash-back-to-images-we-will-never-forget",
    ],
    provider => "https://ex.co",
    url => ["https://app.ex.co/stories/*", "https://www.playbuzz.com/*"],
  },
  "Eyrie" => {
    api => "https://eyrie.io/v1/oembed",
    examples => ["https://eyrie.io/board/747d351c00bc4f91ae7b95635942e685"],
    params => {format => "json"},
    provider => "https://eyrie.io/",
    url => ["https://eyrie.io/board/*", "https://eyrie.io/sparkfun/*"],
  },
  "Facebook" => {
    api => "https://graph.facebook.com/v16.0/oembed_post",
    examples => ["https://www.facebook.com/CDC"],
    params => {access_token => 96481},
    provider => "https://www.facebook.com/",
    url => [
      "https://www.facebook.com/*/posts/*",
      "https://www.facebook.com/*/activity/*",
      "https://www.facebook.com/*/photos/*",
      "https://www.facebook.com/photo.php?fbid=*",
      "https://www.facebook.com/photos/*",
      "https://www.facebook.com/permalink.php?story_fbid=*",
      "https://www.facebook.com/media/set?set=*",
      "https://www.facebook.com/questions/*",
      "https://www.facebook.com/notes/*/*/*",
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
  "Figma" => {
    api => "https://www.figma.com/api/oembed",
    examples => [
      "https://www.figma.com/file/2oGA2ADNXOYWnlBI47UN3R/Safe-Return-(Community)",
    ],
    provider => "https://www.figma.com",
    url => ["https://www.figma.com/file/*"],
  },
  "Filestage" => {
    api => "https://app.filestage.io/oembed",
    provider => "https://filestage.io/",
    url => ["https://app.filestage.io/step/**"],
  },
  "Firework" => {
    api => "https://www.fireworktv.com/oembed",
    examples => [
      "http://www.fireworktv.com/embed/LoA05R/v/vr2Oee",
      "http://www.fireworktv.com/embed/LoA05R/v/vr2Oee",
    ],
    params => {format => "json"},
    provider => "https://fireworktv.com/",
    url => [
      "https://*.fireworktv.com/*", "https://*.fireworktv.com/embed/*/v/*",
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
      "http://flic.kr/s/*", "https://*.flickr.com/photos/*",
      "https://flic.kr/p/*", "https://flic.kr/s/*",
      "https://*.*.flickr.com/*/*", "http://*.*.flickr.com/*/*",
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
  "FlowHubOrg" => {
    api => "https://flowhub.org/o/embed",
    examples => [
      "https://flowhub.org/f/390ee0021ded4910",
      "https://flowhub.org/f/f21aed28a04a7fd0",
    ],
    provider => "https://flows.flowhub.org",
    url => ["https://flowhub.org/f/*", "https://flowhub.org/s/*"],
  },
  "Fooday" => {
    api => "https://fooday.app/oembed",
    examples => ["https://fooday.app/en/reviews/229sej9vN5xv9uHYpYJLyF"],
    params => {format => "json"},
    provider => "https://fooday.app",
    url =>
        ["https://fooday.app/*/reviews/*", "https://fooday.app/*/spots/*",],
  },
  "Form-Data" => {
    api => "https://forms.form-data.com/api/oembed",
    examples => ["https://forms.form-data.com/kzunrnvqj61zmnru2wz6b"],
    provider => "https://form-data.com",
    url => ["https://forms.form-data.com/*"],
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
  "Framatube" => {
    api => "https://framatube.org/services/oembed",
    provider => "https://framatube.org/",
    url => ["https://framatube.org/w/*"],
  },
  "FrameBuzz" => {
    api => "https://framebuzz.com/oembed/",
    examples => ["https://framebuzz.com/v/tJjtJ3rN1usuqAeY/"],
    provider => "https://framebuzz.com/",
    url => ["http://framebuzz.com/v/*", "https://framebuzz.com/v/*"],
  },
  "Framer" => {
    api => "https://api.framer.com/web/oembed",
    examples =>
        ["https://framer.com/share/Music-Player--s0uS6VxvZ30W2IabDqOC",],
    provider => "https://www.framer.com",
    url => ["https://framer.com/share/*", "https://framer.com/embed/*"],
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
      "https://giphy.com/gifs/*",
      "https://giphy.com/clips/*",
      "http://gph.is/*",
      "https://media.giphy.com/media/*/giphy.gif",
    ],
  },
  "GloriaTV" => {
    api => "https://gloria.tv/oembed/",
    examples => ["https://gloria.tv/video/FRqEWoz7GfGt1pfhD4krcgyqC"],
    provider => "https://gloria.tv/",
    url => "https://gloria.tv/*",
  },
  "GMetri" => {
    api => "https://embed.gmetri.com/oembed/",
    examples => [
      "https://game.gmetri.com/safehands_v2&format=json",
      "https://view.gmetri.com/v5/ijafwv/raji_covid_game",
    ],
    provider => "https://www.gmetri.com/",
    url => ["https://view.gmetri.com/*", "https://*.gmetri.com/*"],
  },
  "Gong" => {
    api => "https://app.gong.io/oembed",
    examples => ["https://app.gong.io:8080/call?id=1111111111111111111"],
    provider => "https://www.gong.io/",
    url => ["https://app.gong.io/call?id=*"],
  },
  "GOODFORJOB" => {
    api => "https://www.good-for-job.jp/api/oembed",
    examples => [
      "https://www.good-for-job.jp/slides/0e81c8f7-1e21-478f-9fe8-e60076cc8f61",
      "https://www.good-for-job.jp/slides/31d3ccd1-e6e2-4903-90ca-ab73a57a98c7",
    ],
    provider => "https://www.good-for-job.jp",
    url => ["https://www.good-for-job.jp/slides/*"],
  },
  "Grain" => {
    api => "https://api.grain.com/_/api/oembed",
    examples => [
      "https://grain.com/share/highlight/tZUKIxcZAPaqa0Gzkgw1glKRfBPjcVo5",
    ],
    provider => "https://grain.com",
    url => [
      "https://grain.co/highlight/*", "https://grain.co/share/*",
      "https://grain.com/share/*",
    ],
  },
  "GTChannel" => {
    api => "https://api.luminery.com/oembed",
    examples => ["http://gtchannel.com/watch/4ODiBxivkuTXfsk1tv20Ox"],
    provider => "https://gtchannel.com",
    url => ["https://gtchannel.com/watch/*"],
  },
  "Gumlet" => {
    api => "https://api.gumlet.com/v1/oembed",
    examples => [
      "https://gumlet.tv/watch/6221db301c8b821b0519fba0",
      "https://gumlet.tv/watch/6221db301c8b821b0519fba0",
    ],
    params => {format => "json"},
    provider => "https://www.gumlet.com/",
    url => ["https://gumlet.tv/watch/*", "https://play.gumlet.io/embed/*"],
  },
  "GW2Fashions" => {
    api => "https://gw2fashions.com/fashion/oembed",
    examples => [
      "https://gw2fashions.com/fashion/2b",
      "https://gw2fashions.com/fashion/test saul",
      "https://gw2fashions.com/fashion/cute condi virt",
    ],
    provider => "https://gw2fashions.com/",
    url => ["https://gw2fashions.com/fashion/*"],
  },
  "Gyazo" => {
    api => "https://api.gyazo.com/api/oembed",
    examples => ["https://gyazo.com/71e107d77e8495f0e54d2e5b6dc5d326"],
    provider => "https://gyazo.com",
    url => ["https://gyazo.com/*"],
  },
  "HASH" => {
    api => "https://api.hash.ai/oembed",
    examples => [
      "https://core.hash.ai/\@hash/wildfires-regrowth/stable",
      "https://core.hash.ai/\@hash/warehouse-logistics/stable",
      "https://core.hash.ai/\@hash/traffic-intersection/stable",
    ],
    provider => "https://hash.ai",
    url => ["https://core.hash.ai/\@*"],
  },
  "hearthis.at" => {
    api => "https://hearthis.at/oembed/?format=json",
    examples => [
      "https://hearthis.at/gdsfm/20180922-motherland-soundsystem-im-sender/",
      "https://hearthis.at/gdsfm/20180922-motherland-soundsystem-im-sender/",
    ],
    params => {format => "json"},
    provider => "https://hearthis.at/",
    url => ["https://hearthis.at/*/*/", "https://hearthis.at/*/set/*/"],
  },
  "helenenglish_education" => {
    api => "https://helenenglish.education/embed",
    examples => [
      "https://helenenglish.education/widget?v=1234",
      "https://helenenglish.education/widget?v=456789g",
    ],
    provider => "https://helenenglish.education/",
    url => ["https://helenenglish.education/widget*"],
  },
  "Heyzine" => {
    api => "https://heyzine.com/api1/oembed",
    provider => "https://heyzine.com",
    url => [
      "https://heyzine.com/flip-book/*", "https://*.hflip.co/*",
      "https://*.aflip.in/*",
    ],
  },
  "hihaho" => {
    api => "https://player.hihaho.com/services/oembed",
    examples =>
        ["https://player.hihaho.com/448f6b34-7c12-48f5-952f-23316f93ec5c",],
    params => {format => "json"},
    provider => "https://www.hihaho.com",
    url => ["https://player.hihaho.com/*"],
  },
  "HippoVideo" => {
    api => "https://www.hippovideo.io/services/oembed",
    examples =>
        ["https://www.hippovideo.io/video/play/jzzYRcktQ6JP8xP_49jaaw",],
    params => {format => "json"},
    provider => "https://hippovideo.io",
    url => ["http://*.hippovideo.io/*", "https://*.hippovideo.io/*"],
  },
  "Homey" => {
    api => "https://homey.app/api/oembed/flow",
    examples => ["https://homey.app/f/abcdef/"],
    provider => "https://homey.app",
    url => ["https://homey.app/f/*", "https://homey.app/*/flow/*"],
  },
  "Hopvue" => {
    api => "https://portal.hopvue.com/api/oembed/",
    examples => [
      "https://www.hopvue.com/videos/robots/44c66c71-7735-4e34-c25f-08d8eff1659e",
    ],
    provider => "https://www.hopvue.com",
    url => ["https://*.hopvue.com/*"],
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
  "IcosaGallery" => {
    api => "https://api.icosa.gallery/v1/oembed",
    examples => ["/view/9L2Lt-sxzdp/embed"],
    params => {format => "json"},
    provider => "https://icosa.gallery",
    url => ["https://icosa.gallery/view/*"],
  },
  "Ideamapper" => {
    api => "https://oembed.ideamapper.com/oembed",
    provider => "https://ideamapper.com/",
    url => ["https://oembed.ideamapper.com/*"],
  },
  "Idomoo" => {
    api => "https://oembed.idomoo.com/oembed",
    examples => ["http://liv.idomoo.com/1234/0000/abcdef.mp4"],
    provider => "https://idomoo.com/",
    url => ["https://*.idomoo.com/*"],
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
  "Ignite" => {
    api => "https://app.ignitevideo.cloud/api/oembed",
    examples => [
      "https://videotest.ignite.video/player/index.html?id=67e5788d77aa6e48db64d9db",
    ],
    params => {format => "{format}"},
    provider => "https://ignite.video/",
    url => [
      "https://*.videocdn.net/player/*",
      "https://*.euvideocdn.com/player/*",
    ],
  },
  "iHeartRadio" => {
    api => "https://www.iheart.com/oembed",
    examples => [
      "https://www.iheart.com/podcast/105-stuff-you-should-know-26940277/",
      "https://www.iheart.com/podcast/105-stuff-you-should-know-26940277/",
      "https://www.iheart.com/podcast/105-stuff-you-should-know-26940277/episode/short-stuff-why-does-time-speed-54953593/",
      "https://www.iheart.com/podcast/105-stuff-you-should-know-26940277/episode/short-stuff-why-does-time-speed-54953593/",
    ],
    params => {format => "json"},
    provider => "https://www.iheart.com",
    url => ["https://www.iheart.com/podcast/*/*"],
  },
  "iMenuPro" => {
    api => "https://qr.imenupro.com/api/oembed",
    examples => ["https://qr.imenupro.com/4m-h9"],
    params => {format => "json"},
    provider => "https://imenupro.com",
    url => ["http://qr.imenupro.com/*", "https://qr.imenupro.com/*"],
  },
  "Incredible" => {
    api => "https://oembed.incredible.dev/oembed",
    examples => ["https://incredible.dev/watch/md-to-video"],
    provider => "https://incredible.dev",
    url => ["https://incredible.dev/watch/*"],
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
  "InsightTimer" => {
    api => "https://widgets.insighttimer.com/services/oembed",
    examples =>
        ["https://insighttimer.com/davidji/guided-meditations/deep-healing",],
    provider => "https://insighttimer.com/",
    url => ["https://insighttimer.com/*"],
  },
  "Instagram" => {
    api => "https://graph.facebook.com/v16.0/instagram_oembed",
    examples => ["https://instagram.com/p/V8UMy0LjpX/"],
    provider => "https://instagram.com",
    url => [
      "http://instagram.com/*/p/*", "http://www.instagram.com/*/p/*",
      "https://instagram.com/*/p/*", "https://www.instagram.com/*/p/*",
      "http://instagram.com/p/*", "http://instagr.am/p/*",
      "http://www.instagram.com/p/*", "http://www.instagr.am/p/*",
      "https://instagram.com/p/*", "https://instagr.am/p/*",
      "https://www.instagram.com/p/*", "https://www.instagr.am/p/*",
      "http://instagram.com/tv/*", "http://instagr.am/tv/*",
      "http://www.instagram.com/tv/*", "http://www.instagr.am/tv/*",
      "https://instagram.com/tv/*", "https://instagr.am/tv/*",
      "https://www.instagram.com/tv/*", "https://www.instagr.am/tv/*",
      "http://www.instagram.com/reel/*", "https://www.instagram.com/reel/*",
      "http://instagram.com/reel/*", "https://instagram.com/reel/*",
      "http://instagr.am/reel/*", "https://instagr.am/reel/*",
    ],
  },
  "InsticatorInc" => {
    api => "https://www.insticator.com/oembed",
    examples => [
      "https://ppa.insticator.com/embed-unit/b4a63625-f223-4d97-9385-a34f734c98dc",
      "https://ppa.insticator.com/embed-unit/6b5eac07-18e8-4ecb-90e1-a76091b56d10",
    ],
    params => {format => "json"},
    provider => "https://www.insticator.com/",
    url => ["https://ppa.insticator.com/embed-unit/*"],
  },
  "Issuu" => {
    api => "https://issuu.com/oembed",
    examples => ["https://issuu.com/iscience/docs/issue23"],
    params => {format => "json"},
    provider => "https://issuu.com/",
    url => ["https://issuu.com/*/docs/*"],
  },
  "Itabtechinfosys" => {
    api => "https://samay.itabtechinfosys.com/oembed/",
    examples => ["https://samay.itabtechinfosys.com/thank-you-image.png"],
    provider => "https://samay.itabtechinfosys.com/",
    url => ["https://samay.itabtechinfosys.com/*"],
  },
  "itemisCREATE" => {
    api => "https://create.storage.api.itemis.io/api/embed",
    examples => [
      "https://play.itemis.io/?model=58efe58d-9fd7-4192-8281-935d28eca7ff",
    ],
    provider => "https://play.itemis.io",
    url => ["https://play.itemis.io/*"],
  },
  "Jovian" => {
    api => "https://api.jovian.com/oembed.json",
    examples => [
      "https://jovian.ml/aakashns/movielens-fastai",
      "https://jovian.ml/aakashns/01-pytorch-basics/v/7",
      "https://jovian.ai/aakashns/01-pytorch-basics/v/7",
      "https://jovian.com/aakashns/01-pytorch-basics/v/7",
    ],
    provider => "https://jovian.com/",
    url => [
      "https://jovian.ml/*", "https://jovian.ml/viewer*",
      "https://*.jovian.ml/*", "https://jovian.ai/*",
      "https://jovian.ai/viewer*", "https://*.jovian.ai/*",
      "https://jovian.com/*", "https://jovian.com/viewer*",
      "https://*.jovian.com/*",
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
      "https://tv.kakao.com/m/channel/*/cliplink/*",
      "https://tv.kakao.com/channel/v/*",
      "https://tv.kakao.com/channel/*/livelink/*",
      "https://tv.kakao.com/m/channel/*/livelink/*",
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
  "kmdr" => {
    api => "https://api.kmdr.sh/services/oembed",
    examples =>
        ["https://app.kmdr.sh/history/7f3df902-129d-4af0-bc20-b0f0bc5869dd",],
    params => {format => "json"},
    provider => "https://kmdr.sh",
    url => ["https://app.kmdr.sh/h/*", "https://app.kmdr.sh/history/*"],
  },
  "Knacki" => {
    api => "https://jdr.knacki.info/oembed",
    examples => ["https://jdr.knacki.info/meuh/desole"],
    params => {format => "json"},
    provider => "http://jdr.knacki.info",
    url =>
        ["http://jdr.knacki.info/meuh/*", "https://jdr.knacki.info/meuh/*",],
  },
  "KnowledgePad" => {
    api => "https://api.spoonacular.com/knowledge/oembed",
    examples => [
      "https://knowledgepad.co/", "https://knowledgepad.co/",
      "https://knowledgepad.co/",
    ],
    provider => "https://knowledgepad.co/",
    url => ["https://knowledgepad.co/#/knowledge/*"],
  },
  "Kooapp" => {
    api => "https://embed.kooapp.com/services/oembed",
    examples => [
      "https://www.kooapp.com/koo/Dev_Fadnavis/5b9dded4-02ce-47af-a9fc-6ab8272f67d8",
    ],
    provider => "https://kooapp.com",
    url => ["https://*.kooapp.com/koo/*", "http://*.kooapp.com/koo/*"],
  },
  "Kubit" => {
    api => "https://kubit.ai/services/oembed",
    examples => ["https://kubit.ai", "https://kubit.kubit.ai"],
    params => {format => "json"},
    provider => "https://kubit.ai",
    url => ["https://kubit.ai/*", "https://*.kubit.ai/*"],
  },
  "Kurozora" => {
    api => "https://kurozora.app/oembed",
    examples => [
      "https://kurozora.app/episodes/1",
      "https://kurozora.app/episodes/1",
      "https://kurozora.app/songs/16779",
      "https://kurozora.app/songs/16779",
    ],
    params => {format => "json"},
    provider => "https://kurozora.app/",
    url =>
        ["https://kurozora.app/episodes/*", "https://kurozora.app/songs/*",],
  },
  "LearningApps.org" => {
    api => "http://learningapps.org/oembed.php",
    examples => ["http://LearningApps.org/259"],
    params => {format => "json"},
    provider => "http://learningapps.org/",
    url => ["http://learningapps.org/*"],
  },
  "LeMans.Pod" => {
    api => "https://umotion-test.univ-lemans.fr/oembed",
    examples => [
      "https://umotion-test.univ-lemans.fr/video/0001-test-video-1/",
      "https://umotion-test.univ-lemans.fr/video/0001-test-video-1/",
    ],
    params => {format => "json"},
    provider => "https://umotion-test.univ-lemans.fr/",
    url => ["https://umotion-test.univ-lemans.fr/video/*"],
  },
  "Lille.Pod" => {
    api => "https://pod.univ-lille.fr/video/oembed",
    examples => [
      "https://pod.univ-lille.fr/video/0001-clip-pod/",
      "https://pod.univ-lille.fr/video/0001-clip-pod/",
    ],
    params => {format => "json"},
    provider => "https://pod.univ-lille.fr/",
    url => ["https://pod.univ-lille.fr/video/*"],
  },
  "LinePlace" => {
    api => "https://place.line.me/oembed",
    examples => ["https://place.line.me/businesses/202385697"],
    provider => "https://place.line.me",
    url => ["https://place.line.me/businesses/*"],
  },
  "Linkstackz" => {
    api => "https://api.linkstackz.com/oembed",
    examples => [
      "https://linkstackz.com/irf/26.mp4",
      "https://linkstackz.com/irf/26.mp4",
    ],
    params => {format => "json"},
    provider => "https://www.linkstackz.com/",
    url => ["https://linkstackz.com/irf/*", "https://linkstackz.com/post/*",],
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
  "Loom" => {
    api => "https://www.loom.com/v1/oembed",
    examples => [
      "https://www.loom.com/share/123", "https://www.loom.com/share/123",
      "https://www.loom.com/share/123", "https://www.loom.com/i/123",
      "https://www.loom.com/i/123", "https://www.loom.com/i/123",
    ],
    params => {format => "json"},
    provider => "https://www.loom.com/",
    url => ["https://loom.com/i/*", "https://loom.com/share/*"],
  },
  "LottieFiles" => {
    api => "https://embed.lottiefiles.com/oembed",
    examples => [
      "https://lottiefiles.com/860-maldives-flag",
      "https://lottie.host/embed/34ce41ac-7f9f-4a08-82b2-f86cbf3353a0/lykvZiXpso.json",
    ],
    provider => "https://lottiefiles.com/",
    url => [
      "https://lottiefiles.com/*", "https://*.lottiefiles.com/*",
      "https://*.lottie.host/*", "https://lottie.host/*",
    ],
  },
  "Ludus" => {
    api => "https://app.ludus.one/oembed",
    examples =>
        ["https://app.ludus.one/fd01598e-5ed7-4edb-8d0e-cf75a36e0a07"],
    provider => "https://ludus.one",
    url => ["https://app.ludus.one/*"],
  },
  "Lumiere" => {
    api => "https://admin.lumiere.is/api/services/oembed",
    examples => ["https://p.lumiere.is/v/TQ41w_jVk2"],
    params => {format => "json"},
    provider => "https://latd.com",
    url => ["https://*.lumiere.is/v/*"],
  },
  "marimo" => {
    api => "https://marimo.app/oembed",
    examples => [
      "https://marimo.app/l/d4og6r", "https://marimo.app/l/d4og6r?mode=read",
    ],
    provider => "https://marimo.io/",
    url => ["https://marimo.app/*"],
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
  "Mediastream" => {
    api => "https://mdstrm.com/oembed",
    examples => [
      "https://mdstrm.com/embed/6266eda4a18ad20185e0d3b4",
      "https://mdstrm.com/live-stream/630e029aef211f08502f0815",
      "https://mdstrm.com/image/62c30bd7cace843827c6f6c7",
    ],
    provider => "https://mdstrm.com/",
    url => [
      "https://mdstrm.com/embed/*", "https://mdstrm.com/live-stream/*",
      "https://mdstrm.com/image/*",
    ],
  },
  "MedienarchivderK\xFCnste-Z\xFCrcherHochschulederK\xFCnste" => {
    api => "https://medienarchiv.zhdk.ch/oembed.{format}",
    examples => [
      "https://medienarchiv.zhdk.ch/entries/da88e9e6-6b53-447b-8113-637d885f8ab2",
      "https://medienarchiv.zhdk.ch/entries/da88e9e6-6b53-447b-8113-637d885f8ab2",
    ],
    provider => "https://medienarchiv.zhdk.ch/",
    url => [
      "https://medienarchiv.zhdk.ch/entries/*",
      "https://zhdk.medienarchiv.ch/entries/*",
    ],
  },
  "MermaidInk" => {
    api => "https://mermaid.ink/services/oembed",
    examples => [
      "https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtBXSAtLT4gQihCKVxuXHRcdCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In19",
    ],
    provider => "https://mermaid.ink",
    url => ["https://mermaid.ink/img/*", "https://mermaid.ink/svg/*"],
  },
  "MicrosoftStream" => {
    api => "https://web.microsoftstream.com/oembed",
    examples => [
      "https://web.microsoftstream.com/video/f6df81b2-9438-4154-b32c-c023ebb2a4e3",
    ],
    params => {preload => "none"},
    provider => "https://stream.microsoft.com",
    url => [
      "https://*.microsoftstream.com/video/*",
      "https://*.microsoftstream.com/channel/*",
    ],
  },
  "Minerva" => {
    api => "https://oembed.minervaknows.com",
    examples => [
      "https://app.minervaknows.com/recipes/1d44cafd-946c-4607-b571-26220fd437ee/follow",
    ],
    provider => "https://www.minervaknows.com",
    url => [
      "https://www.minervaknows.com/featured-recipes/*",
      "https://www.minervaknows.com/themes/*",
      "https://www.minervaknows.com/themes/*/recipes/*",
      "https://app.minervaknows.com/recipes/*",
      "https://app.minervaknows.com/recipes/*/follow",
    ],
  },
  "Miro" => {
    api => "https://miro.com/api/v1/oembed",
    examples => ["https://miro.com/app/board/uXjVPZH3NrA=/"],
    provider => "https://miro.com/",
    url => ["https://miro.com/app/board/*"],
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
  "Mixpanel" => {
    api => "https://mixpanel.com/api/app/embed/oembed/",
    examples => [
      "https://mixpanel.com/s/4mEW4a",
      "https://in.mixpanel.com/s/1nGsfj",
      "https://mixpanel.com/project/2195193/view/139237/app/dashboards#id=685944&editor-card-id=\"report-link-4409611\"'",
    ],
    params => {format => "json"},
    provider => "https://mixpanel.com/",
    url => ["https://mixpanel.com/*", "https://*.mixpanel.com/*"],
  },
  "MobyPicture" => {
    api => "http://api.mobypicture.com/oEmbed",
    examples => ["http://mobypicture.com/user/Henk_Voermans/view/15880044"],
    params => {format => "json"},
    provider => "http://www.mobypicture.com",
    url => ["http://www.mobypicture.com/user/*/view/*", "http://moby.to/*",],
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
  "MySQLVisualExplain" => {
    api => "https://api.mysqlexplain.com/v2/oembed.json",
    examples =>
        ["https://mysqlexplain.com/explain/01j2ef1bj7efr97m5v140rnxyz",],
    provider => "https://mysqlexplain.com",
    url => [
      "https://mysqlexplain.com/explain/*",
      "https://embed.mysqlexplain.com/explain/*",
    ],
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
  "NaverClip" => {
    api => "https://m.naver.com/shorts/oEmbed",
    examples => ["https://naver.me/GtUHzqs8"],
    provider => "https://m.naver.com/shorts",
    url => ["https://naver.me/*", "https://m.naver.com/shorts/*"],
  },
  "NDLA-NorwegianDigitalLearningArena" => {
    api => "https://ndla.no/oembed",
    examples => [
      "https://ndla.no/subject:20/topic:1:186732/topic:1:187167/resource:1:176616",
      "https://ndla.no/article/123",
      "https://ndla.no/audio/123",
      "https://ndla.no/concept/123",
      "https://ndla.no/image/123",
      "https://ndla.no/video/6289964283001",
    ],
    provider => "https://ndla.no",
    url => [
      "https://ndla.no/*", "https://ndla.no/article/*",
      "https://ndla.no/audio/*", "https://ndla.no/concept/*",
      "https://ndla.no/image/*", "https://ndla.no/video/*",
    ],
  },
  "Nebula" => {
    api => "https://nebula.tv/api/oembed",
    examples => [
      "https://nebula.tv/videos/jetlag-season-seven-trailer",
      "https://nebula.tv/videos/patrickhwillems-night-of-the-coconut",
    ],
    provider => "https://nebula.tv",
    url => ["https://nebula.tv/videos/*"],
  },
  "NebulaBeta" => {
    api => "https://beta.nebula.tv/api/oembed",
    examples => [
      "https://beta.nebula.tv/videos/jetlag-season-seven-trailer",
      "https://beta.nebula.tv/videos/patrickhwillems-night-of-the-coconut",
    ],
    provider => "https://beta.nebula.tv",
    url => ["https://beta.nebula.tv/videos/*"],
  },
  "NeedleCloud" => {
    api => "https://cloud.needle.tools/oembed",
    examples => [
      "Z23hmXBZ1Y5yHp-Z1Y5yHp-world", "Z23hmXBZ13e102-Z13e102-product",
      "Z23hmXBZ2dSgFy-Z2dSgFy-optimized",
    ],
    provider => "https://cloud.needle.tools",
    url => [
      "https://cloud.needle.tools/-/assets/*/file",
      "https://cloud.needle.tools/view?file=*",
      "https://*.needle.run/*",
    ],
  },
  "neetoRecord" => {
    api => "https://api.neetorecord.com/api/v1/oembed",
    examples => [
      "https://spinkart.neetorecord.com/watch/ade154fb-bff3-4347-b2fa-be77db58e792",
    ],
    params => {format => "json"},
    provider => "https://neetorecord.com",
    url => ["https://*.neetorecord.com/watch/*"],
  },
  "nfb.ca" => {
    api => "http://www.nfb.ca/remote/services/oembed/",
    examples => ["http://www.nfb.ca/film/aboriginality"],
    params => {format => "json"},
    provider => "http://www.nfb.ca/",
    url => ["http://*.nfb.ca/film/*"],
  },
  "NoPaste" => {
    api => "https://oembed.nopaste.ml",
    examples => [
      "https://nopaste.ml/?l=js#XQAAAQAfAAAAAAAAAAAfCAjn2eXL/EQkHNwvz5ZUMLv7U6V3VDuE5C733AY6VA17Vf//8KnAAA==",
    ],
    provider => "https://nopaste.ml",
    url => ["https://nopaste.ml/*"],
  },
  "Observable" => {
    api => "https://api.observablehq.com/oembed",
    examples => ["https://observablehq.com/\@d3/stacked-to-grouped-bars"],
    params => {format => "json"},
    provider => "https://observablehq.com",
    url => [
      "https://observablehq.com/\@*/*", "https://observablehq.com/d/*",
      "https://observablehq.com/embed/*",
    ],
  },
  "Odds.com.au" => {
    api => "https://www.odds.com.au/api/oembed/",
    examples => ["https://www.odds.com.au/odds/rugby-league/nrl/"],
    params => {format => "json"},
    provider => "https://www.odds.com.au",
    url => ["https://www.odds.com.au/*", "https://odds.com.au/*"],
  },
  "Odesli(formerlySonglink)" => {
    api => "https://song.link/oembed",
    examples => [
      "https://song.link/us/i/1182062656",
      "https://song.link/dpmo",
      "https://song.link/album/s/0K4pIOOsfJ9lK8OjrZfXzd",
      "https://artist.link/mars",
    ],
    params => {format => "json"},
    provider => "https://odesli.co",
    url => [
      "https://song.link/*", "https://album.link/*",
      "https://artist.link/*", "https://playlist.link/*",
      "https://pods.link/*", "https://mylink.page/*",
      "https://odesli.co/*",
    ],
  },
  "Odysee" => {
    api => "https://odysee.com/\$/oembed",
    examples => [
      "https://odysee.com/\@veritasium:f/we-built-an-unrideable-bike-to-show-how:b",
      "https://odysee.com/\@veritasium:f/we-built-an-unrideable-bike-to-show-how:b",
      "https://odysee.com/we-built-an-unrideable-bike-to-show-how:b",
    ],
    params => {format => "json"},
    provider => "https://odysee.com",
    url => ["https://odysee.com/*/*", "https://odysee.com/*"],
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
  "OmnyStudio" => {
    api => "https://omny.fm/oembed",
    examples => ["https://omny.fm/shows/adapting/derek-guille"],
    provider => "https://omnystudio.com",
    url => ["https://omny.fm/shows/*"],
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
  "Origits" => {
    api => "https://origits.net/oembed",
    examples => [
      "https://origits.com/v/2ca6a37b-1036579d",
      "https://origits.com/v/2ca6a37b-1036579d",
      "https://origits.com/v/2ca6a37b-1036579d",
    ],
    params => {format => "json"},
    provider => "https://origits.com/",
    url => ["https://origits.com/v/*"],
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
  "Padlet" => {
    api => "https://padlet.com/oembed/",
    examples => ["https://padlet.com/cogdogblog/aos9fosbbwk4"],
    params => {format => "json"},
    provider => "https://padlet.com/",
    url => ["https://padlet.com/*"],
  },
  "PandaVideo" => {
    api => "https://api-v2.pandavideo.com.br/oembed",
    examples => [
      "https://player-vz-ded14ebd-85a.tv.pandavideo.com.br/embed/?v=3b101f05-84aa-4de0-9b64-71f1855388af",
    ],
    provider => "https://pandavideo.com/",
    url => [
      "https://*.tv.pandavideo.com.br/embed/?v=*",
      "https://*.tv.pandavideo.com.br/*/playlist.m3u8",
      "https://dashboard.pandavideo.com.br/#/videos/*",
    ],
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
  "PeerTube.TV" => {
    api => "https://peertube.tv/services/oembed",
    provider => "https://peertube.tv/",
    url => ["https://peertube.tv/w/*"],
  },
  "Picturelfy" => {
    api => "https://api.picturelfy.com/service/oembed/",
    examples => ["https://picturelfy.com/p/b4QFo0MWl2lu1sm"],
    provider => "https://www.picturelfy.com/",
    url =>
        ["http://www.picturelfy.com/p/*", "https://www.picturelfy.com/p/*",],
  },
  "Piggy" => {
    api => "https://piggy.to/oembed",
    examples => ["https://piggy.to/\@magic/ldm92f"],
    provider => "https://piggy.to",
    url => ["https://piggy.to/\@*/*", "https://piggy.to/view/*"],
  },
  "Pikasso" => {
    api => "https://builder.pikasso.xyz/api/oembed",
    examples => [
      "https://builder.pikasso.xyz/embed/button/5f5c5b5b-1b1a-4b1a-9b1a-5b5b5b5b5b5b",
    ],
    provider => "https://builder.pikasso.xyz",
    url => ["https://*.builder.pikasso.xyz/embed/*"],
  },
  "PingVP" => {
    api => "https://beta.pingvp.com.kpnis.nl/p/oembed.php",
    examples => ["https://beta.pingvp.com.kpnis.nl/v/index.php?v=anxXNrIi31"],
    provider => "https://www.pingvp.com/",
    url => "https://www.pingvp.com/*",
  },
  "Pinpoll" => {
    api => "https://tools.pinpoll.com/oembed",
    examples => [
      "https://tools.pinpoll.com/embed/1",
      "https://tools.pinpoll.com/embed/answer/5",
      "https://tools.pinpoll.com/embed/collection/2",
      "https://tools.pinpoll.com/embed/quiz/1",
    ],
    provider => "https://www.pinpoll.com/products/tools",
    url => ["https://tools.pinpoll.com/embed/*"],
  },
  "Pinterest" => {
    api => "https://www.pinterest.com/oembed.json",
    examples => [
      "https://www.pinterest.com/pin/99360735500167749/",
      "https://www.pinterest.com/kentbrew/",
      "https://www.pinterest.com/kentbrew/art-i-wish-i-d-made/",
    ],
    provider => "https://www.pinterest.com",
    url => ["https://www.pinterest.com/*"],
  },
  "PitchHub" => {
    api => "https://player.pitchhub.com/en/public/oembed",
    examples => [
      "https://player.pitchhub.com/en/public/player/296599c9ff2a945eb33d403929e92f35",
    ],
    params => {format => "json"},
    provider => "https://www.pitchhub.com/",
    url => ["https://player.pitchhub.com/en/public/player/*"],
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
  "Plusdocs" => {
    api => "https://app.plusdocs.com/oembed",
    examples => [
      "https://app.plusdocs.com/test/snapshot/cl283huj1094009l1wmdxnzcf",
      "https://app.plusdocs.com/test/pages/edit/cl283huj1094009l1wmdxnzcf",
      "https://app.plusdocs.com/test/pages/share/cl283huj1094009l1wmdxnzcf",
    ],
    provider => "http://plusdocs.com",
    url => [
      "https://app.plusdocs.com/*/snapshots/*",
      "https://app.plusdocs.com/*/pages/edit/*",
      "https://app.plusdocs.com/*/pages/share/*",
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
  "Present" => {
    api => "https://gateway.cobalt.run/present/decks/oembed",
    examples => [
      "https://present.do/decks/60d20b8dffff3c06649f7a18",
      "https://present.do/decks/60c560548ae5e6673633c424",
      "https://present.do/decks/60e2a2203a59f57771f15789",
    ],
    provider => "https://present.do",
    url => ["https://present.do/decks/*"],
  },
  "PreziVideo" => {
    api => "https://prezi.com/v/oembed",
    examples => [
      "https://prezi.com/v/zrmitn0impxx/",
      "https://prezi.com/v/zrmitn0impxx/",
    ],
    params => {format => "json"},
    provider => "https://prezi.com/",
    url => ["https://prezi.com/v/*", "https://*.prezi.com/v/*"],
  },
  "QTpi" => {
    api => "https://qtpi.gg/fashion/oembed",
    examples => [
      "https://qtpi.gg/fashion/2b",
      "https://qtpi.gg/fashion/test saul",
      "https://qtpi.gg/fashion/cute condi virt",
    ],
    provider => "https://qtpi.gg/",
    url => ["https://qtpi.gg/fashion/*"],
  },
  "Quartr" => {
    api => "https://web.quartr.com/api/oembed",
    examples => [
      "https://web.quartr.com/companies/3706/events/215125/",
      "https://web.quartr.com/companies/3706/events/215125/",
    ],
    params => {format => "json"},
    provider => "http://quartr.com",
    url => ["https://quartr.com/*", "https://web.quartr.com/*"],
  },
  "QuellenSuche" => {
    api => "http://quellensuche.de/api/oembed",
    examples => ["https://quellensuche.de/quelle/6868f92ffd285c6f1e3e9f22"],
    params => {format => "json"},
    provider => "http://quellensuche.de",
    url => ["http://quellensuche.de/*"],
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
  "RadioPublic" => {
    api => "https://oembed.radiopublic.com/oembed",
    examples => [
      "https://radiopublic.com/the-bucket-podcast-WD03oE:RXhwbG9yZQ",
      "https://radiopublic.com/PodSaveAmerica:dHJlbmRpbmctaW4tc2VhcmNo",
    ],
    params => {format => "json"},
    provider => "https://radiopublic.com",
    url => [
      "https://play.radiopublic.com/*", "https://radiopublic.com/*",
      "https://www.radiopublic.com/*", "http://play.radiopublic.com/*",
      "http://radiopublic.com/*", "http://www.radiopublic.com/*",
      "https://*.radiopublic.com/*",
    ],
  },
  "Raindrop" => {
    api => "https://pub.raindrop.io/api/oembed",
    examples => ["https://raindrop.io/exentrich/design-66"],
    provider => "https://raindrop.io",
    url => [
      "https://raindrop.io/*", "https://raindrop.io/*/*",
      "https://raindrop.io/*/*/*", "https://raindrop.io/*/*/*/*",
    ],
  },
  "rcvis" => {
    api => "https://animatron.com/oembed",
    examples => [
      "https://rcvis.com/vo/macomb-multiwinner-surplusjson-3/barchart-interactive",
      "https://rcvis.com/vo/opavote2json/barchart-interactive",
      "https://rcvis.com/vo/2018_maine_gov_primary_demjson/barchart-interactive",
    ],
    provider => "https://www.rcvis.com/",
    url => [
      "https://www.rcvis.com/v/*",
      "https://www.rcvis.com/visualize=*",
      "https://www.rcvis.com/ve/*",
      "https://www.rcvis.com/visualizeEmbedded=*",
    ],
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
  "Redlof-Medien" => {
    api => "https://redlof-medien.de/wp-json/oembed/1.0/embed",
    examples => [
      "https://redlof-medien.de/agentur/",
      "https://redlof-medien.de/agentur/",
    ],
    params => {format => "json"},
    provider => "https://redlof-medien.de",
    url => ["https://redlof-medien.de/*", "https://www.redlof-medien.de/*",],
  },
  "ReleaseWire" => {
    api => "http://publisher.releasewire.com/oembed/",
    examples => ["http://rwire.com/600742"],
    params => {format => "json"},
    provider => "http://www.releasewire.com/",
    url => ["http://rwire.com/*"],
  },
  "Replit" => {
    api => "https://replit.com/data/oembed",
    examples => ["https://replit.com/\@replitfaris/python-hello-world"],
    provider => "https://replit.com/",
    url => ["https://repl.it/\@*/*", "https://replit.com/\@*/*"],
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
  "Runkit" => {
    api => "https://embed.runkit.com/oembed",
    examples => ["https://runkit.com/runkit/welcome"],
    provider => "https://runkit.com",
    url => ["http://embed.runkit.com/*,", "https://embed.runkit.com/*,"],
  },
  "Saooti" => {
    api => "https://octopus.saooti.com/oembed",
    examples => ["https://octopus.saooti.com/main/pub/podcast/2525"],
    provider => "https://octopus.saooti.com",
    url => ["https://octopus.saooti.com/main/pub/podcast/*"],
  },
  "SapoVideos" => {
    api => "http://videos.sapo.pt/oembed",
    examples => ["http://videos.sapo.pt/dNbiosGa9YZHfLrhkA88"],
    params => {format => "json"},
    provider => "http://videos.sapo.pt",
    url => ["http://videos.sapo.pt/*"],
  },
  "Satcat" => {
    api => "https://www.satcat.com/api/sats/oembed",
    examples => [
      "https://www.satcat.com/sats/25544",
      "https://www.satcat.com/sats/58651",
      "https://www.satcat.com/sats/62430",
    ],
    provider => "https://www.satcat.com/",
    url => ["https://www.satcat.com/sats/*"],
  },
  "sbedit" => {
    api => "https://sbedit.net/oembed/",
    examples => [
      "https://sbedit.net/oembed/2f155fdea48d15b90f9230867a396a501dd24ec2",
      "https://sbedit.net/oembed/2820edac35dd5035904ca2bf60518d1c3a79d359",
      "https://sbedit.net/oembed/073a35f83fc4f16e597f56208573d29b3dbd55ce",
      "https://sbedit.net/oembed/1e64b476676f6f945af94f278a392aba642d135c",
    ],
    provider => "https://sbedit.net",
    url => ["https://sbedit.net/*"],
  },
  "Scenes" => {
    api => "https://getscenes.com/oembed",
    examples => [
      "https://getscenes.com/e/8a07afbb-0a7c-4314-b027-15a19e25c51a",
      "https://getscenes.com/event/8a07afbb-0a7c-4314-b027-15a19e25c51a",
    ],
    params => {format => "json"},
    provider => "https://getscenes.com",
    url => ["https://getscenes.com/e/*", "https://getscenes.com/event/*"],
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
    url => ["http://www.screencast.com/*"],
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
  "SharedFile" => {
    api => "https://shared-file-kappa.vercel.app/file/api/oembed",
    examples => [
      "https://shared-file-kappa.vercel.app/file/oembed/aac97ee0-9d43-43d0-9376-d419b66d544c",
    ],
    provider => "https://shared-file-kappa.vercel.app/file/",
    url => ["https://shared-file-kappa.vercel.app/file/*"],
  },
  "Shopshare" => {
    api => "https://shopshare.tv/api/shopcast/oembed",
    examples => [
      "https://shopshare.tv/shopcast/U2hvcGNhc3Q6NzExNA==",
      "https://shopshare.tv/shopboard/TG9va2Jvb2s6ODQwOQ==",
    ],
    provider => "https://shopshare.tv",
    url => [
      "https://shopshare.tv/shopboard/*",
      "https://shopshare.tv/shopcast/*",
    ],
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
  "ShowbyAnimaker" => {
    api => "https://api.getshow.io/oembed.{format}",
    examples => [
      "https://present.getshow.io/share/Mcm3a3YBgj8xrtrWURYz",
      "https://present.getshow.io/share/Mcm3a3YBgj8xrtrWURYz",
      "https://app.getshow.io/embed/iframe/?media=Mcm3a3YBgj8xrtrWURYz",
      "https://app.getshow.io/embed/iframe/?media=Mcm3a3YBgj8xrtrWURYz",
    ],
    provider => "https://getshow.io/",
    url =>
        ["https://app.getshow.io/iframe/*", "https://*.getshow.io/share/*",],
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
      "https://sketchfab.com/3d-models/loring-tweet-power-line-9a48434e545f44d08801c8ce2a72e41b",
    ],
    provider => "http://sketchfab.com",
    url => [
      "http://sketchfab.com/*models/*",
      "https://sketchfab.com/*models/*",
      "https://sketchfab.com/*/folders/*",
    ],
  },
  "Skoletube" => {
    api => "https://www.skoletube.dk/media/lasync/oembed/",
    examples => [
      "https://www.skoletube.dk/media/9488982/1gaxieybl2mw5necqt8f0aewjm6n0blctkfi4soz",
      "https://www.skoletube.dk/media/9488982/1gaxieybl2mw5necqt8f0aewjm6n0blctkfi4soz",
    ],
    params => {format => "json"},
    provider => "https://www.skoletube.dk/",
    url => [
      "https://www.skoletube.dk/media/*",
      "https://www.skoletube.dk/video/*",
      "https://www.studietube.dk/media/*",
      "https://www.studietube.dk/video/*",
    ],
  },
  "SlideShare" => {
    api => "https://www.slideshare.net/api/oembed/2",
    examples =>
        ["https://www.slideshare.net/haraldf/business-quotes-for-2011",],
    params => {format => "json"},
    provider => "http://www.slideshare.net/",
    url => [
      "https://www.slideshare.net/*/*", "http://www.slideshare.net/*/*",
      "https://fr.slideshare.net/*/*", "http://fr.slideshare.net/*/*",
      "https://de.slideshare.net/*/*", "http://de.slideshare.net/*/*",
      "https://es.slideshare.net/*/*", "http://es.slideshare.net/*/*",
      "https://pt.slideshare.net/*/*", "http://pt.slideshare.net/*/*",
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
  "Smeme" => {
    api => "https://open.smeme.com/api/oembed",
    examples => [
      "https://open.smeme.com/embed/2ac17338-f447-4c99-b578-bd145c09c60b",
    ],
    provider => "https://smeme.com",
    url => ["https://open.smeme.com/*"],
  },
  "Smrthi" => {
    api => "https://www.smrthi.com/api/oembed",
    examples => [
      "https://www.smrthi.com/book/RigVeda/1.1.1",
      "https://www.smrthi.com/book/RigVeda/1.5.3",
    ],
    provider => "https://www.smrthi.com",
    url => ["https://www.smrthi.com/book/*"],
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
  "SOOP" => {
    api => "https://openapi.sooplive.co.kr/oembed/embedinfo",
    examples => [
      "https://vod.sooplive.co.kr/player/71021072",
      "https://play.sooplive.co.kr/afstar1/237663862",
    ],
    provider => "https://www.sooplive.co.kr",
    url => [
      "https://vod.sooplive.co.kr/player/",
      "https://v.afree.ca/ST/",
      "https://vod.sooplive.co.kr/ST/",
      "https://vod.sooplive.co.kr/PLAYER/STATION/",
      "https://play.sooplive.co.kr/",
    ],
  },
  "SoundCloud" => {
    api => "https://soundcloud.com/oembed",
    examples => [
      "https://soundcloud.com/forss/flickermood",
      "https://soundcloud.com/forss/flickermood",
    ],
    params => {format => "json"},
    provider => "http://soundcloud.com/",
    url => [
      "http://soundcloud.com/*", "https://soundcloud.com/*",
      "https://on.soundcloud.com/*", "https://soundcloud.app.goog.gl/*",
    ],
  },
  "SpeakerDeck" => {
    api => "https://speakerdeck.com/oembed.json",
    examples => ["https://speakerdeck.com/wallat/why-backbone"],
    provider => "https://speakerdeck.com",
    url => ["http://speakerdeck.com/*/*", "https://speakerdeck.com/*/*"],
  },
  "Spotify" => {
    api => "https://open.spotify.com/oembed",
    examples => [
      "https://open.spotify.com/track/2qToAcex0ruZfbEbAy9OhW",
      "spotify:artist:7ae4vgLLhir2MCjyhgbGOQ",
    ],
    provider => "https://spotify.com/",
    url => ["https://open.spotify.com/*", "https://spotify.link/*"],
  },
  "Spotlightr" => {
    api => "https://api.spotlightr.com/getOEmbed",
    examples => [
      "https://0.cdn.spotlightr.com/watch/MTI4NTg5MA==",
      "https://0.cdn.spotlightr.com/watch/MTI4NTg5MA==",
    ],
    params => {format => "json"},
    provider => "https://spotlightr.com",
    url => [
      "https://*.spotlightr.com/watch/*",
      "https://*.spotlightr.com/publish/*",
      "https://*.cdn.spotlightr.com/watch/*",
      "https://*.cdn.spotlightr.com/publish/*",
    ],
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
  "SproutVideo" => {
    api => "http://sproutvideo.com/oembed.{format}",
    examples => [
      "http://sproutvideo.com/videos/709adcb31f19e5c6f8",
      "http://sproutvideo.com/videos/709adcb31f19e5c6f8",
      "https://sproutvideo-example.vids.io/videos/709adcb31f19e5c6f8/sproutvideo-superheroes",
      "https://sproutvideo-example.vids.io/videos/709adcb31f19e5c6f8/sproutvideo-superheroes",
    ],
    provider => "https://sproutvideo.com",
    url =>
        ["https://sproutvideo.com/videos/*", "https://*.vids.io/videos/*",],
  },
  "Spyke" => {
    api => "https://api.spyke.social/embed/oembed",
    examples => ["https://spyke.social/p/01HDH1QH9RX705JE1YJS2225MW"],
    provider => "https://spyke.social",
    url => [
      "http://spyke.social/p/*", "http://spyke.social/u/*",
      "http://spyke.social/g/*", "http://spyke.social/c/*",
      "https://spyke.social/p/*", "https://spyke.social/u/*",
      "https://spyke.social/g/*", "https://spyke.social/c/*",
      "http://www.spyke.social/p/*", "http://www.spyke.social/u/*",
      "http://www.spyke.social/g/*", "http://www.spyke.social/c/*",
      "https://www.spyke.social/p/*", "https://www.spyke.social/u/*",
      "https://www.spyke.social/g/*", "https://www.spyke.social/c/*",
    ],
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
  "Streamio" => {
    api => "https://streamio.com/api/v1/oembed",
    examples => [
      "https://23m.io/yDa7W", "https://s3m.io/rCNma",
      "https://23m.io/HkJfp",
    ],
    provider => "https://www.streamio.com",
    url => ["https://s3m.io/*", "https://23m.io/*"],
  },
  "Subscribi" => {
    api => "https://subscribi.io/api/oembed",
    examples => ["https://subscribi.io/subscribe/5f63b2b306cb71c069272c47"],
    provider => "https://subscribi.io/",
    url => ["https://subscribi.io/api/oembed*"],
  },
  "Sudomemo" => {
    api => "https://www.sudomemo.net/oembed",
    examples => [
      "https://flipnot.es/8UYNV9",
      "https://www.sudomemo.net/watch/75D7C9_135509C9F1AA8_000",
      "https://archive.sudomemo.net/watch/mbwciwgtrf0ehxvtoarwvozbwngc",
    ],
    params => {format => "json"},
    provider => "https://www.sudomemo.net/",
    url => [
      "https://www.sudomemo.net/watch/*",
      "http://www.sudomemo.net/watch/*",
      "https://archive.sudomemo.net/watch/*",
      "http://archive.sudomemo.net/watch/*",
      "https://flipnot.es/*",
      "http://flipnot.es/*",
    ],
  },
  "Supercut" => {
    api => "https://supercut.ai/oembed",
    examples => [
      "https://supercut.ai/share/acmecorp/abcDEF-123",
      "https://supercut.ai/share/acmecorp/abcDEF-123",
      "https://supercut.ai/share/acmecorp/abcDEF-123",
    ],
    params => {format => "json"},
    provider => "https://supercut.ai/",
    url => ["https://supercut.ai/share/*"],
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
  "SwayOffice" => {
    api => "https://sway.office.com/api/v1.0/oembed",
    examples => ["https://sway.office.com/ZCftQ83K9iHgOCH0"],
    params => {format => "json"},
    provider => "https://sway.office.com",
    url => ["https://sway.office.com/*"],
  },
  "Synthesia" => {
    api =>
        "https://69jr5v75rc.execute-api.eu-west-1.amazonaws.com/prod/v2/oembed",
    examples => [
      "https://share.synthesia.io/bcd7bafb-3614-4ab4-8644-75b73bec25de",
      "https://share.synthesia.io/bcd7bafb-3614-4ab4-8644-75b73bec25de",
      "https://share.synthesia.io/bcd7bafb-3614-4ab4-8644-75b73bec25de",
      "https://share.synthesia.io/bcd7bafb-3614-4ab4-8644-75b73bec25de",
    ],
    params => {format => "json"},
    provider => "https://www.synthesia.io/",
    url => ["https://share.synthesia.io/*"],
  },
  "TechPostCast" => {
    api => "https://techpostcast.com/oembed/",
    examples => [
      "https://techpostcast.com/headline-topic-programs/cm7mginv70000js10hzli74q9",
    ],
    provider => "https://techpostcast.com",
    url => ["https://techpostcast.com/headline-topic-programs/*"],
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
  "TheDAMconsultants" => {
    api => "https://hubspot-media-bridge.thedamconsultants.com/oembed/",
    examples => [""],
    provider => "https://hubspot-media-bridge.thedamconsultants.com/",
    url => ["https://hubspot-media-bridge.thedamconsultants.com/*"],
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
      "http://www.tickcounter.com/widget/*",
      "http://www.tickcounter.com/countdown/*",
      "http://www.tickcounter.com/countup/*",
      "http://www.tickcounter.com/ticker/*",
      "http://www.tickcounter.com/clock/*",
      "http://www.tickcounter.com/worldclock/*",
      "http://www.tickcounter.com/embed/*",
      "http://www.tickcounter.com/full/*",
      "https://www.tickcounter.com/widget/*",
      "https://www.tickcounter.com/countdown/*",
      "https://www.tickcounter.com/countup/*",
      "https://www.tickcounter.com/ticker/*",
      "https://www.tickcounter.com/clock/*",
      "https://www.tickcounter.com/worldclock/*",
      "https://www.tickcounter.com/embed/*",
      "https://www.tickcounter.com/full/*",
    ],
  },
  "TikTok" => {
    api => "https://www.tiktok.com/oembed",
    examples => [
      "https://www.tiktok.com/\@scout2015/video/6718335390845095173",
      "https://www.tiktok.com/\@scout2015",
    ],
    provider => "http://www.tiktok.com/",
    url => ["https://www.tiktok.com/*", "https://www.tiktok.com/*/video/*",],
  },
  "tksn-me" => {
    api => "https://tksn.me/api/oembed/",
    examples => [
      "https://tksn.me/oembed-sample/", "https://tksn.me/oembed-sample/",
      "https://tksn.me/oembed-sample/",
    ],
    params => {format => "json"},
    provider => "https://tksn.me",
    url => ["https://tksn.me/*", "https://*.tksn.me/*"],
  },
  "TonicAudio" => {
    api => "https://tonicaudio.com/oembed",
    examples => [
      "https://tnic.io/song/YsiaUAFouw",
      "https://tnic.io/take/h4QIxVnhLL",
    ],
    provider => "https://tonicaudio.com/",
    url => [
      "https://tonicaudio.com/take/*", "https://tonicaudio.com/song/*",
      "https://tnic.io/song/*", "https://tnic.io/take/*",
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
  "Totango" => {
    api => "https://app-test.totango.com/oembed",
    provider => "https://totango.com",
    url => ["https://app-test.totango.com/*"],
  },
  "Trackspace" => {
    api => "https://trackspace.upitup.com/oembed",
    examples => [
      "https://trackspace.upitup.com/track/17",
      "https://trackspace.upitup.com/track/17",
    ],
    params => {format => "json"},
    provider => "http://trackspace.upitup.com/",
    url => ["http://trackspace.upitup.com/*"],
  },
  "TrinityAudio" => {
    api => "https://trinitymedia.ai/services/oembed",
    examples => [
      "https://trinitymedia.ai/player/trinity/12345/?pageURL=https://example.com/page-1",
    ],
    provider => "https://trinityaudio.ai",
    url => [
      "https://trinitymedia.ai/player/*",
      "https://trinitymedia.ai/player/*/*",
      "https://trinitymedia.ai/player/*/*/*",
    ],
  },
  "Tumblr" => {
    api => "https://www.tumblr.com/oembed/1.0",
    examples => [
      "https://staff.tumblr.com/post/619193383820410880/have-a-post-youre-particularly-proud-of",
    ],
    provider => "https://www.tumblr.com",
    url => ["https://*.tumblr.com/post/*"],
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
  "Twinmotion" => {
    api => "https://twinmotion.unrealengine.com/oembed",
    examples => [
      "https://twinmotion.unrealengine.com/presentation/0zxkXymuqH5He0mY",
      "https://twinmotion.unrealengine.com/presentation/bD5qPeTaDGWhpUUq",
      "https://twinmotion.unrealengine.com/panorama/Spp2t_okp3potEeE",
      "https://twinmotion.unrealengine.com/panorama/0UDyotn1HfhAbfv0",
    ],
    provider => "https://twinmotion.unrealengine.com",
    url => [
      "https://twinmotion.unrealengine.com/presentation/*",
      "https://twinmotion.unrealengine.com/panorama/*",
    ],
  },
  "Twitter" => {
    api => "https://publish.twitter.com/oembed",
    examples => [
      "https://twitter.com/Interior/status/463440424141459456",
      "https://twitter.com/Interior/status/463440424141459456",
    ],
    provider => "http://www.twitter.com/",
    url => [
      "https://twitter.com/*", "https://twitter.com/*/status/*",
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
  "UAPod" => {
    api => "https://uapod.univ-antilles.fr/oembed",
    examples => [
      "https://uapod.univ-lille.fr/video/0001-clip-pod/",
      "https://uapod.univ-lille.fr/video/0001-clip-pod/",
    ],
    params => {format => "json"},
    provider => "https://uapod.univ-antilles.fr/",
    url => ["https://uapod.univ-antilles.fr/video/*"],
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
  "Upec.Pod" => {
    api => "https://pod.u-pec.fr/oembed",
    examples => [
      "https://pod.u-pec.fr/video/0268-prammics-presentation/",
      "https://pod.u-pec.fr/video/0268-prammics-presentation/",
    ],
    params => {format => "json"},
    provider => "https://pod.u-pec.fr/",
    url => ["https://pod.u-pec.fr/video/*"],
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
  "VEVO" => {
    api => "https://www.vevo.com/oembed",
    examples =>
        ["http://www.vevo.com/watch/katy-perry/Firework/USCA31000112"],
    provider => "http://www.vevo.com/",
    url => ["http://www.vevo.com/*", "https://www.vevo.com/*"],
  },
  "Videfit" => {
    api => "https://videfit.com/oembed",
    examples => ["https://videfit.com/videos/651"],
    provider => "https://videfit.com/",
    url => ["https://videfit.com/videos/*"],
  },
  "VidMount" => {
    api => "https://vidmount.com/oembed",
    examples => [
      "https://vidmount.com/watch/16186fb990298f",
      "https://vidmount.com/watch/16186fb990298f",
    ],
    params => {format => "json"},
    provider => "https://vidmount.com/",
    url => ["https://vidmount.com/*"],
  },
  "Vidyard" => {
    api => "https://api.vidyard.com/dashboard/v1.1/oembed",
    examples => ["https://video.vidyard.com/watch/njifKy4aJ5PgdYMf9GRNjU"],
    params => {format => "json"},
    provider => "https://vidyard.com",
    url => [
      "http://*.vidyard.com/*", "https://*.vidyard.com/*",
      "http://*.hubs.vidyard.com/*", "https://*.hubs.vidyard.com/*",
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
      "https://vimeo.com/event/*/*",
    ],
  },
  "Viostream" => {
    api => "https://play.viostream.com/oembed",
    examples => ["https://share.viostream.com/nhedxond6q9w41"],
    provider => "https://www.viostream.com",
    url => ["https://share.viostream.com/*"],
  },
  "Viously" => {
    api => "https://www.viously.com/oembed",
    examples => [
      "https://www.viously.com/positivr/gw2jTFu7Lsr",
      "https://www.viously.com/positivr/gw2jTFu7Lsr",
    ],
    params => {format => "json"},
    provider => "https://www.viously.com",
    url => ["https://www.viously.com/*/*"],
  },
  "Vizdom" => {
    api => "https://vizdom.dev/api/v1/oembed",
    examples => [
      "https://vizdom.dev/link/9ec12219-93a6-4c01-a6bb-c0b48d1ef505",
      "https://vizdom.dev/link/9ec12219-93a6-4c01-a6bb-c0b48d1ef505",
      "https://vizdom.dev/link/c8bb315c-55e8-433a-905d-e438318d90ca",
      "https://vizdom.dev/link/c8bb315c-55e8-433a-905d-e438318d90ca",
      "https://vizdom.dev/link/ce8e27a2-cf41-48c2-a110-e860950ca277",
      "https://vizdom.dev/link/ce8e27a2-cf41-48c2-a110-e860950ca277",
    ],
    params => {format => "json"},
    provider => "https://vizdom.dev",
    url => ["https://vizdom.dev/link/*"],
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
  "Vouch" => {
    api => "https://embed.vouchfor.com/v1/oembed",
    examples => [
      "https://app.vouchfor.com/pBjPDICb83",
      "https://app.vouchfor.com/pBjPDICb83",
    ],
    params => {format => "json"},
    provider => "https://www.vouchfor.com/",
    url => ["https://*.vouchfor.com/*"],
  },
  "VoxSnap" => {
    api => "https://data.voxsnap.com/oembed",
    examples => [
      "https://article.voxsnap.com/nirandfar/the-psychology-of-a-billion-dollar-enterprise-app",
    ],
    provider => "https://voxsnap.com/",
    url => ["https://article.voxsnap.com/*/*"],
  },
  "Waltrack" => {
    api => "https://waltrack.net/oembed",
    examples => ["https://waltrack.net/product/532025814"],
    provider => "https://waltrack/net",
    url => ["https://waltrack.net/product/*"],
  },
  "Wave.video" => {
    api => "https://embed.wave.video/oembed",
    examples => ["https://embed.wave.video/382c2d5bbb3949858a0c3f2f"],
    params => {format => "json"},
    provider => "https://wave.video",
    url => ["https://watch.wave.video/*", "https://embed.wave.video/*"],
  },
  "Web3isGoingJustGreat" => {
    api => "https://www.web3isgoinggreat.com/api/oembed",
    examples => [
      "https://www.web3isgoinggreat.com/single/2023-11-21-1",
      "https://www.web3isgoinggreat.com/single/2023-11-21-1",
      "https://www.web3isgoinggreat.com/single/binance-legal-action",
      "https://www.web3isgoinggreat.com/?id=binance-legal-action",
      "https://www.web3isgoinggreat.com/embed/binance-legal-action",
    ],
    params => {format => "json"},
    provider => "https://www.web3isgoinggreat.com/",
    url => [
      "https://www.web3isgoinggreat.com/?id=*",
      "https://www.web3isgoinggreat.com/single/*",
      "https://www.web3isgoinggreat.com/embed/*",
    ],
  },
  "Webcrumbs" => {
    api => "https://webcrumbs.dev/oembed",
    examples => [
      "https://plugins.webcrumbs.dev/demo-component",
      "https://plugins.webcrumbs.dev/demo-component",
    ],
    params => {format => "json"},
    provider => "https://webcrumbs.org/",
    url => ["https://plugins.webcrumbs.dev/*"],
  },
  "wecandeo" => {
    api => "https://play.wecandeo.com/oembed/",
    examples => [
      "https://play.wecandeo.com/video/v/?key=BOKNS9AQWrHDOWXC7DUr6tHd023xknvmIii8SOulPCMtAT1KxqmfHySho4pqLKNis4ZCy4IG7kZTQ431147TteoAieie",
      "https://play.wecandeo.com/video/v/?key=BOKNS9AQWrHDOWXC7DUr6tHd023xknvmIii8SOulPCMtAT1KxqmfHySho4pqLKNis4ZCy4IG7kZTQ431147TteoAieie",
    ],
    params => {format => "json"},
    provider => "https://www.wecandeo.com/",
    url => ["https://play.wecandeo.com/video/v/*"],
  },
  "Whimsical" => {
    api => "https://whimsical.com/api/oembed",
    examples => [
      "https://whimsical.com/how-oembed-works-7wvH66hEVUugCDkpPDbcuc",
      "https://whimsical.com/wine-and-cheese-pairing-mind-map-AFLejp4xXDtAjWLHjVCeyi",
      "https://whimsical.com/how-we-built-whimsical-Q5patpyGV3RDvkvkx1f6Ck",
    ],
    params => {format => "json"},
    provider => "https://www.whimsical.com",
    url => ["https://whimsical.com/*"],
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
    api => "https://app.wizer.me/api/oembed.{format}",
    examples => [
      "https://app.wizer.me/preview/K6EKW",
      "https://app.wizer.me/preview/K6EKW",
    ],
    provider => "https://www.wizer.me/",
    url => ["https://*.wizer.me/learn/*", "https://*.wizer.me/preview/*"],
  },
  "Wokwi" => {
    api => "https://wokwi.com/api/oembed",
    examples => ["https://wokwi.com/share/iq7UORC5aVcFKNdwy9sF"],
    params => {format => "json"},
    provider => "https://wokwi.com",
    url => ["https://wokwi.com/share/*"],
  },
  "WolframCloud" => {
    api => "https://www.wolframcloud.com/oembed",
    examples => [
      "https://www.wolframcloud.com/obj/b9e9ecd9-b523-4da8-a7da-948ecfc228a9",
      "https://www.wolframcloud.com/obj/b9e9ecd9-b523-4da8-a7da-948ecfc228a9",
      "https://www.wolframcloud.com/obj/b9e9ecd9-b523-4da8-a7da-948ecfc228a9",
    ],
    params => {format => "json"},
    provider => "https://www.wolframcloud.com",
    url => ["https://*.wolframcloud.com/*"],
  },
  "WordPress.com" => {
    api => "http://public-api.wordpress.com/oembed/",
    examples =>
        ["http://matt.wordpress.com/2011/07/14/clouds-over-new-york/"],
    params => {format => "json"},
    provider => "https://wordpress.com/",
    url => [
      "https://wordpress.com/*", "http://wordpress.com/*",
      "https://*.wordpress.com/*", "http://*.wordpress.com/*",
      "https://*.*.wordpress.com/*", "http://*.*.wordpress.com/*",
      "https://wp.me/*", "http://wp.me/*",
    ],
  },
  "X" => {
    api => "https://publish.x.com/oembed",
    examples => [
      "https://twitter.com/Interior/status/463440424141459456",
      "https://twitter.com/Interior/status/463440424141459456",
    ],
    provider => "http://www.x.com/",
    url => [
      "https://x.com/*", "https://x.com/*/status/*",
      "https://*.x.com/*/status/*",
    ],
  },
  "YouTube" => {
    api => "https://www.youtube.com/oembed",
    examples => [
      "http://www.youtube.com/watch?v=iwGFalTRHDA",
      "http://www.youtube.com/watch?v=iwGFalTRHDA",
      "http://www.youtube.com/playlist?list=PLSL0f2Dh_snCsLgQ3J319RYQyctRlfJFc",
      "https://youtube.com/playlist?list=PLpeDXSh4nHjRmry7-h62UHfo86evvMK7E",
      "https://www.youtube.com/shorts/a12CpYea0i4",
    ],
    params => {format => "json"},
    provider => "https://www.youtube.com/",
    url => [
      "https://*.youtube.com/watch*",
      "https://*.youtube.com/v/*",
      "https://youtu.be/*",
      "https://*.youtube.com/playlist?list=*",
      "https://youtube.com/playlist?list=*",
      "https://*.youtube.com/shorts*",
      "https://youtube.com/shorts*",
      "https://*.youtube.com/embed/*",
      "https://*.youtube.com/live*",
      "https://youtube.com/live*",
    ],
  },
  "YUMPU" => {
    api => "https://www.yumpu.com/services/oembed",
    examples => [
      "https://www.yumpu.com/xx/document/view/59632036/yumpu-jobs",
      "https://www.yumpu.com/xx/document/view/59632036/yumpu-jobs",
    ],
    params => {format => "json"},
    provider => "https://www.yumpu.com/",
    url => ["https://www.yumpu.com/*/document/view/*/*"],
  },
  "Zeplin" => {
    api => "https://app.zeplin.io/embed",
    examples => [
      "https://app.zeplin.io/project/5cdb386641eeab347e3f4d06/screen/5cdb3876201cf7684bbeebb9",
      "https://app.zeplin.io/project/5cdb386641eeab347e3f4d06/screen/5cdb3876201cf7684bbeebb9/version/5cdb3876201cf7684bbeebba",
      "https://app.zeplin.io/project/5cdb386641eeab347e3f4d06/styleguide/components?coid=5cd3731e20f8ff5736db476b",
      "https://app.zeplin.io/styleguide/5cd36efbc6c39a038ad38c79/components?coid=5cd3731e20f8ff5736db476b",
    ],
    provider => "https://zeplin.io",
    url => [
      "https://app.zeplin.io/project/*/screen/*",
      "https://app.zeplin.io/project/*/screen/*/version/*",
      "https://app.zeplin.io/project/*/styleguide/components?coid=*",
      "https://app.zeplin.io/styleguide/*/components?coid=*",
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
  "Zoomable" => {
    api => "https://srv2.zoomable.ca/oembed",
    examples => [
      "https://srv2.zoomable.ca/viewer.php?i=img3665da501a53181f_lucas-benjamin-wQLAGv4_OYs-unsplash",
    ],
    provider => "https://zoomable.ca/",
    url => ["https://srv2.zoomable.ca/viewer.php*"],
  },
}
;
