(function ($) {
  "use strict";
  /*==================================================================
        [ Daterangepicker ]*/
  try {
    $(".js-datepicker").daterangepicker({
      singleDatePicker: true,
      showDropdowns: true,
      autoUpdateInput: false,
      locale: {
        // format: "DD/MM/YYYY",
        format: "YYYY-MM-DD",
      },
    });

    var myCalendar = $(".js-datepicker");
    var isClick = 0;

    $(window).on("click", function () {
      isClick = 0;
    });

    $(myCalendar).on("apply.daterangepicker", function (ev, picker) {
      isClick = 0;
      // $(this).val(picker.startDate.format("DD/MM/YYYY"));
      $(this).val(picker.startDate.format("YYYY-MM-DD"));
    });

    $(".js-btn-calendar").on("click", function (e) {
      e.stopPropagation();

      if (isClick === 1) isClick = 0;
      else if (isClick === 0) isClick = 1;

      if (isClick === 1) {
        myCalendar.focus();
      }
    });

    $(myCalendar).on("click", function (e) {
      e.stopPropagation();
      isClick = 1;
    });

    $(".daterangepicker").on("click", function (e) {
      e.stopPropagation();
    });
  } catch (er) {
    console.log(er);
  }
  /*[ Select 2 Config ]
        ===========================================================*/

  try {
    var selectSimple = $(".js-select-simple");

    selectSimple.each(function () {
      var that = $(this);
      var selectBox = that.find("select");
      var selectDropdown = that.find(".select-dropdown");
      selectBox.select2({
        dropdownParent: selectDropdown,
      });
    });
  } catch (err) {
    console.log(err);
  }
})(jQuery);

/*YEAR DATE PICKER
        ===========================================================*/
$(".datepicker").datepicker({
  format: "yyyy",
  viewMode: "years",
  minViewMode: "years",
  autoclose: true, //to close picker once year is selected
});

/*fILE UPLOAD
        ===========================================================*/
$(document).on("change", ".file-input", function () {
  var filesCount = $(this)[0].files.length;

  var textbox = $(this).prev();

  if (filesCount === 1) {
    var fileName = $(this).val().split("\\").pop();
    textbox.text(fileName);
  } else {
    textbox.text(filesCount + " files selected");
  }
});
