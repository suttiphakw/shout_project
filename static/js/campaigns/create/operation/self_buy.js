function showPreview_1(event) {
  if(event.target.files.length > 0) {
    const src = URL.createObjectURL(event.target.files[0]);
    const upload_box = document.getElementById("upload_box_1");
    const preview_box = document.getElementById("preview_box_1");
    const preview = document.getElementById("preview_photo_1");
    upload_box.style.display = "none";
    preview.src = src;
    preview_box.style.display = "block";
  }
}


function check_operation_photo() {
  return $('#operation_photo').val() !== '';
}

function check_service_name() {
  return $('#service_name').val() !== ''
}

function check_service_price() {
  return $('#service_price').val() !== ''
}

function check_service_place() {
  return $('#service_place').val() !== ''
}

function check_shouter_post_date() {
  return $('#shouter_post_date').val() !== ''
}


autofill_date = (shouter_post_date, element, day) => {
  element.valueAsDate = new Date(shouter_post_date.getFullYear(), shouter_post_date.getMonth(), shouter_post_date.getDate() - day)
}

function set_date() {
  // Get element by id
  const campaign_launch_date = document.getElementById("campaign_launch_date")
  const shouter_accept_date = document.getElementById("shouter_accept_date")
  const shouter_sent_draft_date = document.getElementById("shouter_sent_draft_date")
  const campaign_end_date = document.getElementById("campaign_end_date")

  // remove disabled
  campaign_launch_date.removeAttribute("disabled")
  shouter_accept_date.removeAttribute("disabled")
  shouter_sent_draft_date.removeAttribute("disabled")
  campaign_end_date.removeAttribute("disabled")

  // get shouter_post_date
  const shouter_post_date = new Date($("#shouter_post_date").val());

  // set new date
  autofill_date(shouter_post_date, campaign_launch_date, 14);
  autofill_date(shouter_post_date, shouter_accept_date, 10);
  autofill_date(shouter_post_date, shouter_sent_draft_date, 7);
  autofill_date(shouter_post_date, campaign_end_date, -2);

  // remove circle
  $("#circle1").css("display", "none");
  $("#circle2").css("display", "none");
  $("#circle3").css("display", "none");
  $("#circle4").css("display", "none");

  // show image
  $("#img_1").css("display", "block");
  $("#img_2").css("display", "block");
  $("#img_3").css("display", "block");
  $("#img_4").css("display", "block");

}

$(document).ready(function(){
  $('.campaign__create__content').on('change', function() {
    if(check_shouter_post_date()) {
      set_date();
    }
    if(check_operation_photo() && check_service_name() && check_service_price() && check_service_place() && check_shouter_post_date()) {
      $("#submit_button").removeClass("btn__grey");
      $("#submit_button").removeAttr("disabled", true);
    }
  });
});