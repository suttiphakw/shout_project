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

function showPreview_2(event) {
  if(event.target.files.length > 0) {
    const src = URL.createObjectURL(event.target.files[0]);
    const upload_box = document.getElementById("upload_box_2");
    const preview_box = document.getElementById("preview_box_2");
    const preview = document.getElementById("preview_photo_2");
    upload_box.style.display = "none";
    preview.src = src;
    preview_box.style.display = "block";
  }
}


function check_brief() {
  return $('#brief').val() !== '';
}

function check_brief_caption() {
  return $('#brief_caption').val() !== ''
}

function check_brief_ref_photo() {
  return $('#brief_ref_photo').val() !== ''
}

$(document).ready(function(){
  $('.campaign__create__content').on('change', function() {
    if(check_brief() && check_brief_caption() && check_brief_ref_photo()) {
      $("#submit_button").removeClass("btn__grey");
      $("#submit_button").removeAttr("disabled", true);
    }
  });
});