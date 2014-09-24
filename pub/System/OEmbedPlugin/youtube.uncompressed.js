jQuery(function($) {
  $(document).on("click", ".oEmbedYouTube", function() {
    var $this = $(this),
      $img = $this.find("img").first(),
      vid = $this.data("vid"),
      $iframe;

    $this.addClass("loading");

    $iframe = $('<iframe />', {
      width: $img.width(),
      height: $img.height(),
      id: vid,
      src: '//www.youtube.com/embed/' + vid + '?autoplay=1',
      frameborder: 0,
      allowfullscreen: 1,
      load: function() {
        $this.removeClass("loading").addClass("active");
      }
    });

    $this.html($iframe);

  });
});
