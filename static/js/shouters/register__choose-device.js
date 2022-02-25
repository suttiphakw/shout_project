function ios_device() {
  const android_info = document.getElementById("android-info");
  android_info.style.display = "none";
  $("#nextPage").removeClass("register__choose-device__button-disable");
  $('input[type="checkbox"]').prop('checked', false);
}

function android_device() {
  const android_info = document.getElementById("android-info");
  android_info.style.display = "flex";
  $("#nextPage").addClass("register__choose-device__button-disable");
}

$(document).ready(function(){
  $('input[type="checkbox"]').click(function(){
    if($(this).is(":checked")){
      $("#nextPage").removeClass("register__choose-device__button-disable");
    }
    else if($(this).is(":not(:checked)")){
      $("#nextPage").addClass("register__choose-device__button-disable");
    }
  });
});