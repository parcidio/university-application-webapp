(function ($) {
  "use strict";
  $(function () {
    $('[data-toggle="offcanvas"]').on("click", function () {
      $(".sidebar-offcanvas").toggleClass("active");
      $(".main-panel").css("margin-left", 0);
    });
  });
})(jQuery);
