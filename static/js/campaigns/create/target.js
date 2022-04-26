function check_gender() {
  return $("input[type='radio'][name='gender']:checked").val() !== undefined
}

function check_age() {
  return $("input[type='checkbox'][name='age']:checked").val() !== undefined
}

function check_province() {
  return $("input[type='radio'][name='province']:checked").val() !== undefined
}

function check_product_link() {
  return $("input[type='checkbox'][name='interest']:checked").val() !== undefined
}

function check_shouter_gender() {
  return $("input[type='checkbox'][name='shouter_gender']:checked").val() !== undefined
}

function show_modal() {
  const modal = document.getElementById("modal");
  modal.style.display = "block"
}

function close_modal() {
  const modal = document.getElementById("modal");
  modal.style.display = "none"
}

$(document).ready(function(){
  $('.campaign__create__content__target').on('change', function() {
    if(check_gender() && check_age() && check_province() && check_product_link()) {
      $("#next_button").removeClass("btn__grey");
      $("#next_button").removeAttr("disabled", true);
    }
  });
  $('.campaign__create__content__target__modal').on('change', function() {
    if(check_shouter_gender()) {
      $("#submit_button").removeClass("btn__grey");
      $("#submit_button").removeAttr("disabled", true);
    }
  });
});