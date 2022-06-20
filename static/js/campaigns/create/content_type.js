function get_content_type() {
  return {
    'story': $('input[name="story_type"]:checked').val(),
    'post': $('input[name="post_type"]:checked').val(),
  }
}

function show_modal() {
  const modal = document.getElementById("modal");
  modal.style.display = "block"
}

function close_modal() {
  const modal = document.getElementById("modal");
  modal.style.display = "none"
}

function story_selected(type) {
  const story_pc_button = document.getElementById("story_pc_button");
  const story_pc_button_selected = document.getElementById("story_pc_button_selected");
  const story_ugc_button = document.getElementById("story_ugc_button");
  const story_ugc_button_selected = document.getElementById("story_ugc_button_selected");

  if(type === 'pc') {
    $('#pc_box').addClass('activate');
    $('#ugc_box').removeClass('activate');

    story_pc_button.style.display = "none";
    story_pc_button_selected.style.display = "flex";

    story_ugc_button.style.display = "flex";
    story_ugc_button_selected.style.display = "none";
  }

  if(type === 'ugc') {
    $('#pc_box').removeClass('activate');
    $('#ugc_box').addClass('activate');

    story_pc_button.style.display = "flex";
    story_pc_button_selected.style.display = "none";

    story_ugc_button.style.display = "none";
    story_ugc_button_selected.style.display = "flex";
  }
}

function post_selected(type) {
  const post_single_button = document.getElementById("post_single_button");
  const post_single_button_selected = document.getElementById("post_single_button_selected");
  const post_multi_button = document.getElementById("post_multi_button");
  const post_multi_button_selected = document.getElementById("post_multi_button_selected");

  if(type === 'single') {
    $('#single_box').addClass('activate');
    $('#multi_box').removeClass('activate');

    post_single_button.style.display = "none";
    post_single_button_selected.style.display = "flex";

    post_multi_button.style.display = "flex";
    post_multi_button_selected.style.display = "none";
  }

  if(type === 'multi') {
    $('#single_box').removeClass('activate');
    $('#multi_box').addClass('activate');

    post_single_button.style.display = "flex";
    post_single_button_selected.style.display = "none";

    post_multi_button.style.display = "none";
    post_multi_button_selected.style.display = "flex";
  }
}
///////////////////////////////////////////////////////////////////
// Checking
///////////////////////////////////////////////////////////////////
function check_fb() {
  return document.getElementById("is_fb");
}

function check_is_story() {
  return document.getElementById("story");
}

function check_is_post() {
  return document.getElementById("post");
}

function check_pc() {
  return $('#pc').is(":checked");
}

function check_ugc() {
  return $('#ugc').is(":checked");
}

function check_single() {
  return $('#single').is(":checked");
}

function check_multi() {
  return $('#multi').is(":checked");
}

function check_pc_single() {
  return $('#pc').is(":checked") && $('#single').is(":checked");
}

function check_pc_multi() {
  return $('#pc').is(":checked") && $('#multi').is(":checked");
}

function check_ugc_single() {
  return $('#ugc').is(":checked") && $('#single').is(":checked");
}

function check_ugc_multi() {
  return $('#ugc').is(":checked") && $('#multi').is(":checked");
}
///////////////////////////////////////////////////////////////////
// Function
///////////////////////////////////////////////////////////////////
function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function get_factor(price_per_shouter, avg_reach_1_shouter) {
  return price_per_shouter / avg_reach_1_shouter
}

function get_reach(budget, factor) {
  return Math.round((budget / factor) / 100) * 100
}

function get_shouter(reach, avg_reach_1_shouter) {
  return Math.round(reach / avg_reach_1_shouter)
}

function get_cpr(budget, reach) {
  return Math.round((budget / reach ) * 100) / 100
}

function fb(number) {
  return Math.round(number / 1.1)
}

function fb_100(number) {
  return Math.round((number / 1.1) / 100) * 100
}

function fb_2de(number) {
  return Math.round((number / 1.1) * 100) / 100
}
///////////////////////////////////////////////////////////////////
// Constant
///////////////////////////////////////////////////////////////////
// Constant AVG. Reach
const min_avg_story_reach_per_shouter = 621
const max_avg_story_reach_per_shouter = 2300
const min_avg_post_reach_per_shouter = 3000
const max_avg_post_reach_per_shouter = 7250

// Constant Story FC
const min_fc_price_per_shouter = 500
const max_fc_price_per_shouter = 1458

// Constant Story UGC
const min_ugc_price_per_shouter = 783
const max_ugc_price_per_shouter = 2333

// Constant Post Single
const min_single_price_per_shouter = 2000
const max_single_price_per_shouter = 3667

// Constant Post Single
const min_multi_price_per_shouter = 2500
const max_multi_price_per_shouter = 4400
///////////////////////////////////////////////////////////////////
// Cal
///////////////////////////////////////////////////////////////////
function cal_story(check_fb, budget) {
  // Reach
  let min_fc_story_reach = get_reach(budget, get_factor(min_fc_price_per_shouter, min_avg_story_reach_per_shouter))
  let max_fc_story_reach = get_reach(budget, get_factor(max_fc_price_per_shouter, max_avg_story_reach_per_shouter))
  let min_ugc_story_reach = get_reach(budget, get_factor(min_ugc_price_per_shouter, min_avg_story_reach_per_shouter))
  let max_ugc_story_reach = get_reach(budget, get_factor(max_ugc_price_per_shouter, max_avg_story_reach_per_shouter))
  // Shouter
  let min_fc_story_shouter = get_shouter(min_fc_story_reach, min_avg_story_reach_per_shouter)
  let max_fc_story_shouter = get_shouter(max_fc_story_reach, max_avg_story_reach_per_shouter)
  let min_ugc_story_shouter = get_shouter(min_ugc_story_reach, min_avg_story_reach_per_shouter)
  let max_ugc_story_shouter = get_shouter(max_ugc_story_reach, max_avg_story_reach_per_shouter)
  // CPR
  let min_fc_story_cpr = get_cpr(budget, min_fc_story_reach)
  let max_fc_story_cpr = get_cpr(budget, max_fc_story_reach)
  let min_ugc_story_cpr = get_cpr(budget, min_ugc_story_reach)
  let max_ugc_story_cpr = get_cpr(budget, max_ugc_story_reach)
  if (check_fb) {
    // Reach
    min_fc_story_reach = fb_100(min_fc_story_reach)
    max_fc_story_reach = fb_100(max_fc_story_reach)
    min_ugc_story_reach = fb_100(min_ugc_story_reach)
    max_ugc_story_reach = fb_100(max_ugc_story_reach)
    // Shouter
    min_fc_story_shouter = fb(min_fc_story_shouter)
    max_fc_story_shouter = fb(max_fc_story_shouter)
    min_ugc_story_shouter = fb(min_ugc_story_shouter)
    max_ugc_story_shouter = fb(max_ugc_story_shouter)
    // CPR
    min_fc_story_cpr = fb_2de(min_fc_story_cpr)
    max_fc_story_cpr = fb_2de(max_fc_story_cpr)
    min_ugc_story_cpr = fb_2de(min_ugc_story_cpr)
    max_ugc_story_cpr = fb_2de(max_ugc_story_cpr)
  }
  return {
    // Reach
    "min_fc_story_reach": Math.min(min_fc_story_reach, max_fc_story_reach),
    "max_fc_story_reach": Math.max(min_fc_story_reach, max_fc_story_reach),
    "min_ugc_story_reach": Math.min(min_ugc_story_reach, max_ugc_story_reach),
    "max_ugc_story_reach": Math.max(min_ugc_story_reach, max_ugc_story_reach),
    // Shouter
    "min_fc_story_shouter": Math.min(min_fc_story_shouter, max_fc_story_shouter),
    "max_fc_story_shouter": Math.max(min_fc_story_shouter, max_fc_story_shouter),
    "min_ugc_story_shouter": Math.min(min_ugc_story_shouter, max_ugc_story_shouter),
    "max_ugc_story_shouter": Math.max(min_ugc_story_shouter, max_ugc_story_shouter),
    // CPR
    "min_fc_story_cpr": Math.min(min_fc_story_cpr, max_fc_story_cpr),
    "max_fc_story_cpr": Math.max(min_fc_story_cpr, max_fc_story_cpr),
    "min_ugc_story_cpr": Math.min(min_ugc_story_cpr, max_ugc_story_cpr),
    "max_ugc_story_cpr": Math.max(min_ugc_story_cpr, max_ugc_story_cpr)
  }
}

function cal_post(check_fb, budget) {
  // Reach
  let min_single_post_reach = get_reach(budget, get_factor(min_single_price_per_shouter, min_avg_post_reach_per_shouter))
  let max_single_post_reach = get_reach(budget, get_factor(max_single_price_per_shouter, max_avg_post_reach_per_shouter))
  let min_multi_post_reach = get_reach(budget, get_factor(min_multi_price_per_shouter, min_avg_post_reach_per_shouter))
  let max_multi_post_reach = get_reach(budget, get_factor(max_multi_price_per_shouter, max_avg_post_reach_per_shouter))
  // Shouter
  let min_single_post_shouter = get_shouter(min_single_post_reach, min_avg_post_reach_per_shouter)
  let max_single_post_shouter = get_shouter(max_single_post_reach, max_avg_post_reach_per_shouter)
  let min_multi_post_shouter = get_shouter(min_multi_post_reach, min_avg_post_reach_per_shouter)
  let max_multi_post_shouter = get_shouter(max_multi_post_reach, max_avg_post_reach_per_shouter)
  // CPR
  let min_single_post_cpr = get_cpr(budget, min_single_post_reach)
  let max_single_post_cpr = get_cpr(budget, max_single_post_reach)
  let min_multi_post_cpr = get_cpr(budget, min_multi_post_reach)
  let max_multi_post_cpr = get_cpr(budget, max_multi_post_reach)
  if (check_fb) {
    // Reach
    min_single_post_reach = fb_100(min_single_post_reach)
    max_single_post_reach = fb_100(max_single_post_reach)
    min_multi_post_reach = fb_100(min_multi_post_reach)
    max_multi_post_reach = fb_100(max_multi_post_reach)
    // Shouter
    min_single_post_shouter = fb(min_single_post_shouter)
    max_single_post_shouter = fb(max_single_post_shouter)
    min_multi_post_shouter = fb(min_multi_post_shouter)
    max_multi_post_shouter = fb(max_multi_post_shouter)
    // CPR
    min_single_post_cpr = fb_2de(min_single_post_cpr)
    max_single_post_cpr = fb_2de(max_single_post_cpr)
    min_multi_post_cpr = fb_2de(min_multi_post_cpr)
    max_multi_post_cpr = fb_2de(max_multi_post_cpr)
  }
  return {
    // Reach
    "min_single_post_reach": Math.min(min_single_post_reach, max_single_post_reach),
    "max_single_post_reach": Math.max(min_single_post_reach, max_single_post_reach),
    "min_multi_post_reach": Math.min(min_multi_post_reach, max_multi_post_reach),
    "max_multi_post_reach": Math.max(min_multi_post_reach, max_multi_post_reach),
    // Shouter
    "min_single_post_shouter": Math.min(min_single_post_shouter, max_single_post_shouter),
    "max_single_post_shouter": Math.max(min_single_post_shouter, max_single_post_shouter),
    "min_multi_post_shouter": Math.min(min_multi_post_shouter, max_multi_post_shouter),
    "max_multi_post_shouter": Math.max(min_multi_post_shouter, max_multi_post_shouter),
    // CPR
    "min_single_post_cpr": Math.min(min_single_post_cpr, max_single_post_cpr),
    "max_single_post_cpr": Math.max(min_single_post_cpr, max_single_post_cpr),
    "min_multi_post_cpr": Math.min(min_multi_post_cpr, max_multi_post_cpr),
    "max_multi_post_cpr": Math.max(min_multi_post_cpr, max_multi_post_cpr)
  }
}

function cal_story_post(check_fb, budget) {
  const min_avg_reach_1_shouter = min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter
  const max_avg_reach_1_shouter = max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter

  // Reach
  let min_fc_single_reach = get_reach(budget,
    get_factor((min_fc_price_per_shouter + min_single_price_per_shouter) * 0.9, min_avg_reach_1_shouter)
  )
  let max_fc_single_reach = get_reach(budget,
    get_factor((max_fc_price_per_shouter + max_single_price_per_shouter) * 0.9, max_avg_reach_1_shouter)
  )
  let min_fc_multi_reach = get_reach(budget,
    get_factor((min_fc_price_per_shouter + min_multi_price_per_shouter) * 0.9, min_avg_reach_1_shouter)
  )
  let max_fc_multi_reach = get_reach(budget,
    get_factor((max_fc_price_per_shouter + max_multi_price_per_shouter) * 0.9, max_avg_reach_1_shouter)
  )
  let min_ugc_single_reach = get_reach(budget,
    get_factor((min_ugc_price_per_shouter + min_single_price_per_shouter) * 0.9, min_avg_reach_1_shouter)
  )
  let max_ugc_single_reach = get_reach(budget,
    get_factor((max_ugc_price_per_shouter + max_single_price_per_shouter) * 0.9, max_avg_reach_1_shouter)
  )
  let min_ugc_multi_reach = get_reach(budget,
    get_factor((min_ugc_price_per_shouter + min_multi_price_per_shouter) * 0.9, min_avg_reach_1_shouter)
  )
  let max_ugc_multi_reach = get_reach(budget,
    get_factor((max_ugc_price_per_shouter + max_multi_price_per_shouter) * 0.9, max_avg_reach_1_shouter)
  )

  // Shouter
  let min_fc_single_shouter = get_shouter(min_fc_single_reach, min_avg_reach_1_shouter)
  let max_fc_single_shouter = get_shouter(max_fc_single_reach, max_avg_reach_1_shouter)
  let min_fc_multi_shouter = get_shouter(min_fc_multi_reach, min_avg_reach_1_shouter)
  let max_fc_multi_shouter = get_shouter(max_fc_multi_reach, max_avg_reach_1_shouter)
  let min_ugc_single_shouter = get_shouter(min_ugc_single_reach, min_avg_reach_1_shouter)
  let max_ugc_single_shouter = get_shouter(max_ugc_single_reach, max_avg_reach_1_shouter)
  let min_ugc_multi_shouter = get_shouter(min_ugc_multi_reach, min_avg_reach_1_shouter)
  let max_ugc_multi_shouter = get_shouter(max_ugc_multi_reach, max_avg_reach_1_shouter)

  // CPR
  let min_fc_single_cpr = get_cpr(budget, min_fc_single_reach)
  let max_fc_single_cpr = get_cpr(budget, max_fc_single_reach)
  let min_fc_multi_cpr = get_cpr(budget, min_fc_multi_reach)
  let max_fc_multi_cpr = get_cpr(budget, max_fc_multi_reach)
  let min_ugc_single_cpr = get_cpr(budget, min_ugc_single_reach)
  let max_ugc_single_cpr = get_cpr(budget, max_ugc_single_reach)
  let min_ugc_multi_cpr = get_cpr(budget, min_ugc_multi_reach)
  let max_ugc_multi_cpr= get_cpr(budget, max_ugc_multi_reach)

  if (check_fb) {
    // Reach
    min_fc_single_reach = fb_100(min_fc_single_reach)
    max_fc_single_reach = fb_100(max_fc_single_reach)
    min_fc_multi_reach = fb_100(min_fc_multi_reach)
    max_fc_multi_reach = fb_100(max_fc_multi_reach)
    min_ugc_single_reach = fb_100(min_ugc_single_reach)
    max_ugc_single_reach = fb_100(max_ugc_single_reach)
    min_ugc_multi_reach = fb_100(min_ugc_multi_reach)
    max_ugc_multi_reach = fb_100(max_ugc_multi_reach)
    // Shouter
    min_fc_single_shouter = fb(min_fc_single_shouter)
    max_fc_single_shouter = fb(max_fc_single_shouter)
    min_fc_multi_shouter = fb(min_fc_multi_shouter)
    max_fc_multi_shouter = fb(max_fc_multi_shouter)
    min_ugc_single_shouter = fb(min_ugc_single_shouter)
    max_ugc_single_shouter = fb(max_ugc_single_shouter)
    min_ugc_multi_shouter = fb(min_ugc_multi_shouter)
    max_ugc_multi_shouter = fb(max_ugc_multi_shouter)
    // CPR
    min_fc_single_cpr = fb_2de(min_fc_single_cpr)
    max_fc_single_cpr = fb_2de(max_fc_single_cpr)
    min_fc_multi_cpr = fb_2de(min_fc_multi_cpr)
    max_fc_multi_cpr = fb_2de(max_fc_multi_cpr)
    min_ugc_single_cpr = fb_2de(min_ugc_single_cpr)
    max_ugc_single_cpr = fb_2de(max_ugc_single_cpr)
    min_ugc_multi_cpr = fb_2de(min_ugc_multi_cpr)
    max_ugc_multi_cpr = fb_2de(max_ugc_multi_cpr)
  }

  return {
    // Reach
    "min_fc_single_reach": Math.min(min_fc_single_reach, max_fc_single_reach),
    "max_fc_single_reach": Math.max(min_fc_single_reach, max_fc_single_reach),
    "min_fc_multi_reach": Math.min(min_fc_multi_reach, max_fc_multi_reach),
    "max_fc_multi_reach": Math.max(min_fc_multi_reach, max_fc_multi_reach),
    "min_ugc_single_reach": Math.min(min_ugc_single_reach, max_ugc_single_reach),
    "max_ugc_single_reach": Math.max(min_ugc_single_reach, max_ugc_single_reach),
    "min_ugc_multi_reach": Math.min(min_ugc_multi_reach, max_ugc_multi_reach),
    "max_ugc_multi_reach": Math.max(min_ugc_multi_reach, max_ugc_multi_reach),
    // Shouter
    "min_fc_single_shouter": Math.min(min_fc_single_shouter, max_fc_single_shouter),
    "max_fc_single_shouter": Math.max(min_fc_single_shouter, max_fc_single_shouter),
    "min_fc_multi_shouter": Math.min(min_fc_multi_shouter, max_fc_multi_shouter),
    "max_fc_multi_shouter": Math.max(min_fc_multi_shouter, max_fc_multi_shouter),
    "min_ugc_single_shouter": Math.min(min_ugc_single_shouter, max_ugc_single_shouter),
    "max_ugc_single_shouter": Math.max(min_ugc_single_shouter, max_ugc_single_shouter),
    "min_ugc_multi_shouter": Math.min(min_ugc_multi_shouter, max_ugc_multi_shouter),
    "max_ugc_multi_shouter": Math.max(min_ugc_multi_shouter, max_ugc_multi_shouter),
    // CPR
    "min_fc_single_cpr": Math.min(min_fc_single_cpr, max_fc_single_cpr),
    "max_fc_single_cpr": Math.max(min_fc_single_cpr, max_fc_single_cpr),
    "min_fc_multi_cpr": Math.min(min_fc_multi_cpr, max_fc_multi_cpr),
    "max_fc_multi_cpr": Math.max(min_fc_multi_cpr, max_fc_multi_cpr),
    "min_ugc_single_cpr": Math.min(min_ugc_single_cpr, max_ugc_single_cpr),
    "max_ugc_single_cpr": Math.max(min_ugc_single_cpr, max_ugc_single_cpr),
    "min_ugc_multi_cpr": Math.min(min_ugc_multi_cpr, max_ugc_multi_cpr),
    "max_ugc_multi_cpr": Math.max(min_ugc_multi_cpr, max_ugc_multi_cpr),
  }
}
///////////////////////////////////////////////////////////////////
// Set Value
///////////////////////////////////////////////////////////////////
function set_right_bar_pc(dict) {
  document.getElementById("rightbar_shouter").innerHTML = numberWithCommas(dict["min_fc_story_shouter"]) + " - " + numberWithCommas(dict["max_fc_story_shouter"]) + " คน"
  document.getElementById("rightbar_reach").innerHTML = numberWithCommas(dict["min_fc_story_reach"]) + " - " + numberWithCommas(dict["max_fc_story_reach"]) + " reach"
  document.getElementById("rightbar_cpr").innerHTML = numberWithCommas(dict["min_fc_story_cpr"]) + " - " + numberWithCommas(dict["max_fc_story_cpr"]) + " บาท"

  document.getElementById("rightbar_work_format").innerHTML = "Prepared Content"
  document.getElementById("rightbar_work_quantity").innerHTML = "1 Story"

  return {
    "content_type": "Prepared Content",
    "shouter": numberWithCommas(dict["min_fc_story_shouter"]) + " - " + numberWithCommas(dict["max_fc_story_shouter"]) + " คน",
    "reach": numberWithCommas(dict["min_fc_story_reach"]) + " - " + numberWithCommas(dict["max_fc_story_reach"]) + " reach",
    "cpr": numberWithCommas(dict["min_fc_story_cpr"]) + " - " + numberWithCommas(dict["max_fc_story_cpr"]) + " บาท"
  }
}

function set_right_bar_ugc(dict) {
  document.getElementById("rightbar_shouter").innerHTML = numberWithCommas(dict["min_ugc_story_shouter"]) + " - " + numberWithCommas(dict["max_ugc_story_shouter"]) + " คน"
  document.getElementById("rightbar_reach").innerHTML = numberWithCommas(dict["min_ugc_story_reach"]) + " - " + numberWithCommas(dict["max_ugc_story_reach"]) + " reach"
  document.getElementById("rightbar_cpr").innerHTML = numberWithCommas(dict["min_ugc_story_cpr"]) + " - " + numberWithCommas(dict["max_ugc_story_cpr"]) + " บาท"

  document.getElementById("rightbar_work_format").innerHTML = "User Generated Content"
  document.getElementById("rightbar_work_quantity").innerHTML = "1 Story"

  return {
    "content_type": "User Generated Content",
    "shouter": numberWithCommas(dict["min_ugc_story_shouter"]) + " - " + numberWithCommas(dict["max_ugc_story_shouter"]) + " คน",
    "reach": numberWithCommas(dict["min_ugc_story_reach"]) + " - " + numberWithCommas(dict["max_ugc_story_reach"]) + " reach",
    "cpr": numberWithCommas(dict["min_ugc_story_cpr"]) + " - " + numberWithCommas(dict["max_ugc_story_cpr"]) + " บาท"
  }
}

function set_right_bar_single(dict) {
  document.getElementById("rightbar_shouter").innerHTML = numberWithCommas(dict["min_single_post_shouter"]) + " - " + numberWithCommas(dict["max_single_post_shouter"]) + " คน"
  document.getElementById("rightbar_reach").innerHTML = numberWithCommas(dict["min_single_post_reach"]) + " - " + numberWithCommas(dict["max_single_post_reach"]) + " reach"
  document.getElementById("rightbar_cpr").innerHTML = numberWithCommas(dict["min_single_post_cpr"]) + " - " + numberWithCommas(dict["max_single_post_cpr"]) + " บาท"

  document.getElementById("rightbar_work_format").innerHTML = "Single Post"
  document.getElementById("rightbar_work_quantity").innerHTML = "1 Post, 1 รูป"

  return {
    "content_type": "Single Post",
    "shouter": numberWithCommas(dict["min_single_post_shouter"]) + " - " + numberWithCommas(dict["max_single_post_shouter"]) + " คน",
    "reach": numberWithCommas(dict["min_single_post_reach"]) + " - " + numberWithCommas(dict["max_single_post_reach"]) + " reach",
    "cpr": numberWithCommas(dict["min_single_post_cpr"]) + " - " + numberWithCommas(dict["max_single_post_cpr"]) + " บาท",
  }
}

function set_right_bar_multi(dict) {
  document.getElementById("rightbar_shouter").innerHTML = numberWithCommas(dict["min_multi_post_shouter"]) + " - " + numberWithCommas(dict["max_multi_post_shouter"]) + " คน"
  document.getElementById("rightbar_reach").innerHTML = numberWithCommas(dict["min_multi_post_reach"]) + " - " + numberWithCommas(dict["max_multi_post_reach"]) + " reach"
  document.getElementById("rightbar_cpr").innerHTML = numberWithCommas(dict["min_multi_post_cpr"]) + " - " + numberWithCommas(dict["max_multi_post_cpr"]) + " บาท"

  document.getElementById("rightbar_work_format").innerHTML = "Multi Post"
  document.getElementById("rightbar_work_quantity").innerHTML = "1 Post, 3-5 รูป"

  return {
    "content_type": "Multi Post",
    "shouter": numberWithCommas(dict["min_multi_post_shouter"]) + " - " + numberWithCommas(dict["max_multi_post_shouter"]) + " คน",
    "reach": numberWithCommas(dict["min_multi_post_reach"]) + " - " + numberWithCommas(dict["max_multi_post_reach"]) + " reach",
    "cpr": numberWithCommas(dict["min_multi_post_cpr"]) + " - " + numberWithCommas(dict["max_multi_post_cpr"]) + " บาท"
  }
}
///////////////////////////////////////////////////////////////////
function set_story_value(dict) {
  document.getElementById("pc_shouter").innerHTML = numberWithCommas(dict["min_fc_story_shouter"]) + " - " + numberWithCommas(dict["max_fc_story_shouter"]) + " คน"
  document.getElementById("pc_reach").innerHTML = numberWithCommas(dict["min_fc_story_reach"]) + " - " + numberWithCommas(dict["max_fc_story_reach"]) + " reach"
  document.getElementById("pc_cpr").innerHTML = numberWithCommas(dict["min_fc_story_cpr"]) + " - " + numberWithCommas(dict["max_fc_story_cpr"]) + " บาท"

  document.getElementById("ugc_shouter").innerHTML = numberWithCommas(dict["min_ugc_story_shouter"]) + " - " + numberWithCommas(dict["max_ugc_story_shouter"]) + " คน"
  document.getElementById("ugc_reach").innerHTML = numberWithCommas(dict["min_ugc_story_reach"]) + " - " + numberWithCommas(dict["max_ugc_story_reach"]) + " reach"
  document.getElementById("ugc_cpr").innerHTML = numberWithCommas(dict["min_ugc_story_cpr"]) + " - " + numberWithCommas(dict["max_ugc_story_cpr"]) + " บาท"
}

function set_post_value(dict) {
  document.getElementById("single_shouter").innerHTML = numberWithCommas(dict["min_single_post_shouter"]) + " - " + numberWithCommas(dict["max_single_post_shouter"]) + " คน"
  document.getElementById("single_reach").innerHTML = numberWithCommas(dict["min_single_post_reach"]) + " - " + numberWithCommas(dict["max_single_post_reach"]) + " reach"
  document.getElementById("single_cpr").innerHTML = numberWithCommas(dict["min_single_post_cpr"]) + " - " + numberWithCommas(dict["max_single_post_cpr"]) + " บาท"

  document.getElementById("multi_shouter").innerHTML = numberWithCommas(dict["min_multi_post_shouter"]) + " - " + numberWithCommas(dict["max_multi_post_shouter"]) + " คน"
  document.getElementById("multi_reach").innerHTML = numberWithCommas(dict["min_multi_post_reach"]) + " - " + numberWithCommas(dict["max_multi_post_reach"]) + " reach"
  document.getElementById("multi_cpr").innerHTML = numberWithCommas(dict["min_multi_post_cpr"]) + " - " + numberWithCommas(dict["max_multi_post_cpr"]) + " บาท"
}

function set_fc_single_value(dict) {
  document.getElementById("pc_shouter").innerHTML = numberWithCommas(dict["min_fc_single_shouter"]) + " - " + numberWithCommas(dict["max_fc_single_shouter"]) + " คน"
  document.getElementById("pc_reach").innerHTML = numberWithCommas(dict["min_fc_single_reach"]) + " - " + numberWithCommas(dict["max_fc_single_reach"]) + " reach"
  document.getElementById("pc_cpr").innerHTML = numberWithCommas(dict["min_fc_single_cpr"]) + " - " + numberWithCommas(dict["max_fc_single_cpr"]) + " บาท"

  document.getElementById("ugc_shouter").innerHTML = "- คน"
  document.getElementById("ugc_reach").innerHTML = "- reach"
  document.getElementById("ugc_cpr").innerHTML = "- บาท"

  document.getElementById("single_shouter").innerHTML = numberWithCommas(dict["min_fc_single_shouter"]) + " - " + numberWithCommas(dict["max_fc_single_shouter"]) + " คน"
  document.getElementById("single_reach").innerHTML = numberWithCommas(dict["min_fc_single_reach"]) + " - " + numberWithCommas(dict["max_fc_single_reach"]) + " reach"
  document.getElementById("single_cpr").innerHTML = numberWithCommas(dict["min_fc_single_cpr"]) + " - " + numberWithCommas(dict["max_fc_single_cpr"]) + " บาท"

  document.getElementById("multi_shouter").innerHTML = "- คน"
  document.getElementById("multi_reach").innerHTML = "- reach"
  document.getElementById("multi_cpr").innerHTML = "- บาท"

  document.getElementById("rightbar_shouter").innerHTML = numberWithCommas(dict["min_fc_single_shouter"]) + " - " + numberWithCommas(dict["max_fc_single_shouter"]) + " คน"
  document.getElementById("rightbar_reach").innerHTML = numberWithCommas(dict["min_fc_single_reach"]) + " - " + numberWithCommas(dict["max_fc_single_reach"]) + " reach"
  document.getElementById("rightbar_cpr").innerHTML = numberWithCommas(dict["min_fc_single_cpr"]) + " - " + numberWithCommas(dict["max_fc_single_cpr"]) + " บาท"

  document.getElementById("rightbar_work_format").innerHTML = "Prepared Content & Single Post"
  document.getElementById("rightbar_work_quantity").innerHTML = "1 Story, 1 Post, 1 รูป"

  return {
    "content_type": "Prepared Content & Single Post",
    "shouter": numberWithCommas(dict["min_fc_single_shouter"]) + " - " + numberWithCommas(dict["max_fc_single_shouter"]) + " คน",
    "reach": numberWithCommas(dict["min_fc_single_reach"]) + " - " + numberWithCommas(dict["max_fc_single_reach"]) + " reach",
    "cpr": numberWithCommas(dict["min_fc_single_cpr"]) + " - " + numberWithCommas(dict["max_fc_single_cpr"]) + " บาท"
  }
}

function set_fc_multi_value(dict) {
  document.getElementById("pc_shouter").innerHTML = numberWithCommas(dict["min_fc_multi_shouter"]) + " - " + numberWithCommas(dict["max_fc_multi_shouter"]) + " คน"
  document.getElementById("pc_reach").innerHTML = numberWithCommas(dict["min_fc_multi_reach"]) + " - " + numberWithCommas(dict["max_fc_multi_reach"]) + " reach"
  document.getElementById("pc_cpr").innerHTML = numberWithCommas(dict["min_fc_multi_cpr"]) + " - " + numberWithCommas(dict["max_fc_multi_cpr"]) + " บาท"

  document.getElementById("ugc_shouter").innerHTML = "- คน"
  document.getElementById("ugc_reach").innerHTML = "- reach"
  document.getElementById("ugc_cpr").innerHTML = "- บาท"

  document.getElementById("single_shouter").innerHTML = "- คน"
  document.getElementById("single_reach").innerHTML = "- reach"
  document.getElementById("single_cpr").innerHTML = "- บาท"

  document.getElementById("multi_shouter").innerHTML = numberWithCommas(dict["min_fc_multi_shouter"]) + " - " + numberWithCommas(dict["max_fc_multi_shouter"]) + " คน"
  document.getElementById("multi_reach").innerHTML = numberWithCommas(dict["min_fc_multi_reach"]) + " - " + numberWithCommas(dict["max_fc_multi_reach"]) + " reach"
  document.getElementById("multi_cpr").innerHTML = numberWithCommas(dict["min_fc_multi_cpr"]) + " - " + numberWithCommas(dict["max_fc_multi_cpr"]) + " บาท"

  document.getElementById("rightbar_shouter").innerHTML = numberWithCommas(dict["min_fc_multi_shouter"]) + " - " + numberWithCommas(dict["max_fc_multi_shouter"]) + " คน"
  document.getElementById("rightbar_reach").innerHTML = numberWithCommas(dict["min_fc_multi_reach"]) + " - " + numberWithCommas(dict["max_fc_multi_reach"]) + " reach"
  document.getElementById("rightbar_cpr").innerHTML = numberWithCommas(dict["min_fc_multi_cpr"]) + " - " + numberWithCommas(dict["max_fc_multi_cpr"]) + " บาท"

  document.getElementById("rightbar_work_format").innerHTML = "Prepared Content & Multi Post"
  document.getElementById("rightbar_work_quantity").innerHTML = "1 Story, 1 Post, 3-5 รูป"

  return {
    "content_type": "Prepared Content & Multi Post",
    "shouter": numberWithCommas(dict["min_fc_multi_shouter"]) + " - " + numberWithCommas(dict["max_fc_multi_shouter"]) + " คน",
    "reach": numberWithCommas(dict["min_fc_multi_reach"]) + " - " + numberWithCommas(dict["max_fc_multi_reach"]) + " reach",
    "cpr": numberWithCommas(dict["min_fc_multi_cpr"]) + " - " + numberWithCommas(dict["max_fc_multi_cpr"]) + " บาท",
  }
}

function set_ugc_single_value(dict) {
  document.getElementById("pc_shouter").innerHTML = "- คน"
  document.getElementById("pc_reach").innerHTML = "- reach"
  document.getElementById("pc_cpr").innerHTML = "- บาท"

  document.getElementById("ugc_shouter").innerHTML = numberWithCommas(dict["min_ugc_single_shouter"]) + " - " + numberWithCommas(dict["max_ugc_single_shouter"]) + " คน"
  document.getElementById("ugc_reach").innerHTML = numberWithCommas(dict["min_ugc_single_reach"]) + " - " + numberWithCommas(dict["max_ugc_single_reach"]) + " reach"
  document.getElementById("ugc_cpr").innerHTML = numberWithCommas(dict["min_ugc_single_cpr"]) + " - " + numberWithCommas(dict["max_ugc_single_cpr"]) + " บาท"

  document.getElementById("single_shouter").innerHTML = numberWithCommas(dict["min_ugc_single_shouter"]) + " - " + numberWithCommas(dict["max_ugc_single_shouter"]) + " คน"
  document.getElementById("single_reach").innerHTML = numberWithCommas(dict["min_ugc_single_reach"]) + " - " + numberWithCommas(dict["max_ugc_single_reach"]) + " reach"
  document.getElementById("single_cpr").innerHTML = numberWithCommas(dict["min_ugc_single_cpr"]) + " - " + numberWithCommas(dict["max_ugc_single_cpr"]) + " บาท"

  document.getElementById("multi_shouter").innerHTML = "- คน"
  document.getElementById("multi_reach").innerHTML = "- reach"
  document.getElementById("multi_cpr").innerHTML = "- บาท"

  document.getElementById("rightbar_shouter").innerHTML = numberWithCommas(dict["min_ugc_single_shouter"]) + " - " + numberWithCommas(dict["max_ugc_single_shouter"]) + " คน"
  document.getElementById("rightbar_reach").innerHTML = numberWithCommas(dict["min_ugc_single_reach"]) + " - " + numberWithCommas(dict["max_ugc_single_reach"]) + " reach"
  document.getElementById("rightbar_cpr").innerHTML = numberWithCommas(dict["min_ugc_single_cpr"]) + " - " + numberWithCommas(dict["max_ugc_single_cpr"]) + " บาท"

  document.getElementById("rightbar_work_format").innerHTML = "User Generated & Single Post"
  document.getElementById("rightbar_work_quantity").innerHTML = "1 Story, 1 Post, 1 รูป"

  return {
    "content_type": "User Generated & Single Post",
    "shouter": numberWithCommas(dict["min_ugc_single_shouter"]) + " - " + numberWithCommas(dict["max_ugc_single_shouter"]) + " คน",
    "reach": numberWithCommas(dict["min_ugc_single_reach"]) + " - " + numberWithCommas(dict["max_ugc_single_reach"]) + " reach",
    "cpr": numberWithCommas(dict["min_ugc_single_cpr"]) + " - " + numberWithCommas(dict["max_ugc_single_cpr"]) + " บาท",
  }
}

function set_ugc_multi_value(dict) {
  document.getElementById("pc_shouter").innerHTML = "- คน"
  document.getElementById("pc_reach").innerHTML = "- reach"
  document.getElementById("pc_cpr").innerHTML = "- บาท"

  document.getElementById("ugc_shouter").innerHTML = numberWithCommas(dict["min_ugc_multi_shouter"]) + " - " + numberWithCommas(dict["max_ugc_multi_shouter"]) + " คน"
  document.getElementById("ugc_reach").innerHTML = numberWithCommas(dict["min_ugc_multi_reach"]) + " - " + numberWithCommas(dict["max_ugc_multi_reach"]) + " reach"
  document.getElementById("ugc_cpr").innerHTML = numberWithCommas(dict["min_ugc_multi_cpr"]) + " - " + numberWithCommas(dict["max_ugc_multi_cpr"]) + " บาท"

  document.getElementById("single_shouter").innerHTML = "- คน"
  document.getElementById("single_reach").innerHTML = "- reach"
  document.getElementById("single_cpr").innerHTML = "- บาท"

  document.getElementById("multi_shouter").innerHTML = numberWithCommas(dict["min_ugc_multi_shouter"]) + " - " + numberWithCommas(dict["max_ugc_multi_shouter"]) + " คน"
  document.getElementById("multi_reach").innerHTML = numberWithCommas(dict["min_ugc_multi_reach"]) + " - " + numberWithCommas(dict["max_ugc_multi_reach"]) + " reach"
  document.getElementById("multi_cpr").innerHTML = numberWithCommas(dict["min_ugc_multi_cpr"]) + " - " + numberWithCommas(dict["max_ugc_multi_cpr"]) + " บาท"

  document.getElementById("rightbar_shouter").innerHTML = numberWithCommas(dict["min_ugc_multi_shouter"]) + " - " + numberWithCommas(dict["max_ugc_multi_shouter"]) + " คน"
  document.getElementById("rightbar_reach").innerHTML = numberWithCommas(dict["min_ugc_multi_reach"]) + " - " + numberWithCommas(dict["max_ugc_multi_reach"]) + " reach"
  document.getElementById("rightbar_cpr").innerHTML = numberWithCommas(dict["min_ugc_multi_cpr"]) + " - " + numberWithCommas(dict["max_ugc_multi_cpr"]) + " บาท"

  document.getElementById("rightbar_work_format").innerHTML = "User Generated & Multi Post"
  document.getElementById("rightbar_work_quantity").innerHTML = "1 Story, 1 Post, 3-5 รูป"

  return {
    "content_type": "User Generated & Multi Post",
    "shouter": numberWithCommas(dict["min_ugc_multi_shouter"]) + " - " + numberWithCommas(dict["max_ugc_multi_shouter"]) + " คน",
    "reach": numberWithCommas(dict["min_ugc_multi_reach"]) + " - " + numberWithCommas(dict["max_ugc_multi_reach"]) + " reach",
    "cpr": numberWithCommas(dict["min_ugc_multi_cpr"]) + " - " + numberWithCommas(dict["max_ugc_multi_cpr"]) + " บาท"
  }
}

function set_modal(dict) {
  document.getElementById("modal_content_type").innerHTML = dict["content_type"]
  document.getElementById("modal_shouter").innerHTML = dict["shouter"]
  document.getElementById("modal_reach").innerHTML = dict["reach"]
  document.getElementById("modal_cpr").innerHTML = dict["cpr"]
}
///////////////////////////////////////////////////////////////////
// Document Ready Function
///////////////////////////////////////////////////////////////////
$(document).ready(function() {
  const input = $("#budget").html();
  const budget = input.replace(',','');
  const dict_story = cal_story(check_fb(), budget);
  const dict_post = cal_post(check_fb(), budget);
  if (!(check_is_post())) {
    set_story_value(dict_story);
  }
  if (!(check_is_story())) {
    set_post_value(dict_post);
  }
  $('.campaign__create__content__scope').on('change', function() {
    let modal_dict;
    if (!(check_is_post())) {
      if (check_pc()) {
        modal_dict = set_right_bar_pc(dict_story);
        set_modal(modal_dict);
      }
      if (check_ugc()) {
        modal_dict = set_right_bar_ugc(dict_story);
        set_modal(modal_dict);
      }
    }
    if (!(check_is_story())) {
      if (check_single()) {
        modal_dict = set_right_bar_single(dict_post);
        set_modal(modal_dict);
      }
      if (check_multi()) {
        modal_dict = set_right_bar_multi(dict_post);

      }
    }
    if (check_is_story() && check_is_post()) {
      const dict_story_post = cal_story_post(check_fb(), budget)
      if (check_pc_single()) {
        modal_dict = set_fc_single_value(dict_story_post)
        set_modal(modal_dict);
      }
      if (check_pc_multi()) {
        modal_dict = set_fc_multi_value(dict_story_post)
        set_modal(modal_dict);
      }
      if (check_ugc_single()) {
        modal_dict = set_ugc_single_value(dict_story_post)
        set_modal(modal_dict);
      }
      if (check_ugc_multi()) {
        modal_dict = set_ugc_multi_value(dict_story_post)
        set_modal(modal_dict);
      }
    }
  });
});
