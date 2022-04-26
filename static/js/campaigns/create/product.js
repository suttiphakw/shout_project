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

function showPreview_3(event) {
  if(event.target.files.length > 0) {
    const src = URL.createObjectURL(event.target.files[0]);
    const upload_box = document.getElementById("upload_box_3");
    const preview_box = document.getElementById("preview_box_3");
    const preview = document.getElementById("preview_photo_3");
    upload_box.style.display = "none";
    preview.src = src;
    preview_box.style.display = "block";
  }
}

function check_product_name() {
  return $('#product_name').val() !== ''
}

function check_product_photo() {
  return $('#product_photo_1').val() !== '' || $('#product_photo_2').val() !== '' || $('#product_photo_3').val() !== ''
}

function check_product_detail() {
  return $('#product_detail').val() !== ''
}

function check_product_link() {
  return $('#product_link').val() !== ''
}

$(document).ready(function(){
  $('.campaign__create__content__product').on('change', function() {
    if(check_product_name() && check_product_photo() && check_product_detail() && check_product_link()) {
      $("#submit_button").removeClass("btn__grey");
      $("#submit_button").removeAttr("disabled", true);
    }
  });
});