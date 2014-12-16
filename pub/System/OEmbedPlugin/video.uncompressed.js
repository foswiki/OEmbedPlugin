jQuery(function($) {
  $(document).on("click", ".oEmbedVideo", function() {
    var $this = $(this),
      $img = $this.find("img").first(),
      opts = $this.data(),
      $iframe;

    $this.addClass("loading");

    $iframe = $('<iframe />', {
      width: $img.width(),
      height: $img.height(),
      id: opts.vid,
      src: opts.src,
      frameborder: 0,
      allowfullscreen: 1,
      load: function() {
        $this.removeClass("loading").addClass("active");
      }
    });

    $this.html($iframe);

  });
});

