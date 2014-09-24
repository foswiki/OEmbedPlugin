jQuery(function($) {
  $(document).on("click", ".oEmbedYouTube", function() {
    var $this = $(this),
      $img = $this.find("img").first(),
      src = $img.attr("src"),
      rx = new RegExp("(?:img.youtube.com|i.ytimg.com)/vi/(.*)/"),
      match = rx.exec(src),
      width = $img.width(),
      height = $img.height(),
      vid;

    if (match) {
      vid = match[1];
      $this.html('<iframe width="' + width +
        '" height="' + height +
        '" id="' + vid +
        '" src="//www.youtube.com/embed/' + vid + '?autoplay=1"' +
        '" frameborder="0" allowfullscreen="1" style="border:none;"></iframe>');
      $this.addClass("active");
    }
  });
});
