function show_modal(modal_id) {
  const modal = document.getElementById(modal_id);
  modal.style.display = "block";
}

function close_modal(modal_id) {
  const modal = document.getElementById(modal_id);
  modal.style.display = "none";
}

function show_confirm_modal() {
  const modal = document.getElementById("confirm_modal");
  modal.style.display = "block";
}

function close_confirm_modal() {
  const modal = document.getElementById("confirm_modal");
  modal.style.display = "none";
}


function count_shouter() {
  let checkboxes = $("div.shouter__card :checkbox:checked").map(function() {
    return this.value;
  }).get();
  $("#shouter_count").html(checkboxes.length + ' คน');
  $("#shouter_count_2").html(checkboxes.length);
}

let total_reach = 0
let total_cpr = 0
let total_follower = 0
let total_engagement = 0
let total_price = 0

const numberWithCommas = x => x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");


const set_value = (total_reach, total_cpr, total_follower, total_engagement, total_price) => {
  $("#total_reach").html(numberWithCommas(total_reach) + ' Reach');
  $("#total_cpr").html(total_cpr + ' บาท');
  $("#total_follower").html(numberWithCommas(total_follower) + ' Followers');
  $("#total_engagement").html(total_engagement);
  $("#total_price").html(numberWithCommas(total_price));
}

const round_2_decimal = value => Math.round(value *100) / 100

function set_result_bar(id, reach, cpr, follower, engagement, price) {
  let checkboxes = $("div.shouter__card :checkbox:checked").map(function() {
    return this.value;
  }).get();

  let card = document.getElementById(id);

  // Check is_checkbox
  let is_check = card.checked;

  if (is_check) {
    total_reach += reach
    if (checkboxes.length !== 0) {
      total_cpr = round_2_decimal(((total_cpr * (checkboxes.length-1)) + cpr) / checkboxes.length)
    } else {
      total_cpr = 0
    }
    total_follower += follower
    if (checkboxes.length !== 0) {
      total_engagement = round_2_decimal(((total_engagement * (checkboxes.length-1)) + engagement) / checkboxes.length)
    } else {
      total_engagement = 0
    }
    total_price += price
  } else {
    total_reach -= reach
    if (checkboxes.length !== 0) {
      total_cpr = round_2_decimal(((total_cpr * (checkboxes.length+1)) - cpr) / checkboxes.length)
    } else {
      total_cpr = 0
    }
    total_follower -= follower
    if (checkboxes.length !== 0) {
      total_engagement = round_2_decimal(((total_engagement * (checkboxes.length+1)) - engagement) / checkboxes.length)
    } else {
      total_engagement = 0
    }
    total_price -= price
  }

  set_value(total_reach, total_cpr, total_follower, total_engagement, total_price)
}

///////////////////////////////////////////////////////////////////
// Document Ready Function
///////////////////////////////////////////////////////////////////
$(document).ready(function(){
  $('.campaign__create__content__shouter__section').on('change', function() {
    count_shouter();
  });
});
///////////////////////////////////////////////////////////////////