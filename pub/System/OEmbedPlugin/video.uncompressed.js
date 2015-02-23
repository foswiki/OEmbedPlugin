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
      src: opts.src,
      frameborder: 0,
      allowfullscreen: 1,
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

