// nationalitySection visibility
$(".nationalitySection").hide();
$("#namibianIdSection").show();
$("#id_nationality").on("change", function () {
  console.log("id_nationality");
  if ($(this).val() == "NA") {
    $(".nationalitySection").hide();
    $("#namibianIdSection").show();
  } else {
    $(".nationalitySection").show();
    $("#namibianIdSection").hide();
  }
});
// medical_information visibility
$(".medical_information").hide();
$("#id_has_medical_condition").change(function () {
  if ($("#id_has_medical_condition_0").is(":checked")) {
    console.log("checked");
    $(".medical_information").hide();
  }
  if ($("#id_has_medical_condition_1").is(":checked")) {
    console.log("unchecked");

    $(".medical_information").show();
  }
});

$("#section1Form").on("submit", function () {
  console.log("submitted");
});

//form agreement acceptance
$("#id_application_form_acknowledgement").prop("disabled", true);
$("#term-and-condition-scroll").on("scroll", function () {
  console.log("scroll");

  if ($(this).scrollTop() + $(this).innerHeight() >= $(this)[0].scrollHeight) {
    $("#id_application_form_acknowledgement").prop("disabled", false);
    $("#id_application_form_acknowledgement").prop("checked", true);
  } else {
    //$("#id_application_form_acknowledgement").prop("disabled", true);
    $("#id_application_form_acknowledgement").prop("checked", false);
  }
});

//modall message logic
$("#submitBtn").on("click", function () {
  if (
    $("#id_application_form_acknowledgement").prop("disabled") == false &&
    $("#id_application_form_acknowledgement").prop("checked") == true
  ) {
    $("#modal-body-message").html(
      " Your Form Has Been Submitted Successfully!"
    );
    $("#modal-footer-procced-button").show();

    $("#modal-dismissal").hide();
    $("#staticBackdrop_application_form_success").modal("show");
  } else {
    $("#modal-body-message").html(
      "Please read the terms and condition and accept it, in order to submit your form."
    );
    $("#modal-footer-procced-button").hide();
    $("#modal-dismissal").show();
    $("#staticBackdrop_application_form_success").modal("show");
  }
});

/*
    On submiting the form, send the POST ajax
    request to server and after successfull submission
    display the object.
*/

$(document).ready(function () {
  $("#id_course_first_choice").on("change", function () {
    console.log($(this).val() + " selected");
    var course = $(this).val();
    // const url = "{% url 'portal-registration-form-shortcourse-update' %}";
    $.ajax({
      // url: url,
      type: "GET",
      dataType: "json",
      contentType: false,
      // processData: false,
      data: { course: parseInt(course) },
      success: (data) => {
        console.log(data);
        $("#mode_of_study").html(data);
        // var instance = JSON.parse(data);
        console.log(data);
      },
      error: (error) => {
        $("#mode_of_study").html(error);
        console.log(error);
      },
    });
  });

  //save the form every time a submit button is pressed
  $("#section1Form").on("submit", function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    // var serializedData = $(this).serialize();
    var formData = new FormData(this);
    console.log(formData);
    // make POST ajax call
    $.ajax({
      type: "POST",
      data: formData,
      dataType: "json",
      mimeType: "multipart/form-data",
      success: function (response) {
        // on successfull creating object
        console.log("JSON: " + response);
      },
      error: function (response) {
        // //alert the error if any error occured
        // alert(response["responseJSON"]["error"]);
        // alert(response);
        // console.log("ERROR: " + response);
      },
      cache: false,
      contentType: false,
      processData: false,
    });
  });
});

/*THIS WILL AUTOMATICALLY SAVE THE DATA IN THE FORM
                            EVERYTIME THAT THE VALUE OF THE FORM FIELDS CHANGES*/
$(document).ready(function () {
  $(".save_changes").on("input", function (e) {
    e.preventDefault();
    const form = document.getElementById("section1Form");
    var formData = new FormData(form);
    console.log(formData);
    // make POST ajax call
    $.ajax({
      type: "POST",
      data: formData,
      dataType: "json",
      mimeType: "multipart/form-data",
      success: function (response) {
        // on successfull creating object
        console.log("JSON: " + response);
      },
      cache: false,
      contentType: false,
      processData: false,
    });
  });
});
