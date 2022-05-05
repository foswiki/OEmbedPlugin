/*
 * video.js
 *
 * (c)opyright 2013-2022 Michael Daum http://michaeldaumconsulting.com
 *
 * Licensed under the GPL license http://www.gnu.org/licenses/gpl.html
 *
 */
"use strict";

jQuery(function($) {
  $(document).on("click", ".oEmbedVideo", function() {
    var $this = $(this),
      opts = $this.data(),
      $iframe;

    $this.addClass("loading");

    $iframe = $('<iframe />', {
      width: $this.width(),
      height: $this.height(),
      id: opts.vid,
      allowfullscreen: 1,
      src: opts.src,
      load: function() {
        $this.removeClass("loading").addClass("active");
      }
    });

    $this.html($iframe);
    $this.bind("stop.oembed", function() {
      $this.removeClass("active loading").empty();
    });
  });
});
