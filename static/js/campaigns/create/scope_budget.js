///////////////////////////////////////////////////////////////////
// Function
///////////////////////////////////////////////////////////////////
function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
///////////////////////////////////////////////////////////////////
// Check Value
///////////////////////////////////////////////////////////////////
function check_social() {
  return $('#is_check_instagram').is(":checked")
}

function check_facebook() {
  return $('#is_check_facebook').is(":checked")
}

function check_budget() {
  return $('#budget').val() !== ''
}

function check_work_type() {
  return $('#story').is(":checked") || $('#post').is(":checked") || $('#post_story').is(":checked")
}
///////////////////////////////////////////////////////////////////
// Enable / Disable FB
///////////////////////////////////////////////////////////////////
function enable_facebook() {
  const facebook_checkbox_disabled = document.getElementById("facebook_checkbox_disabled");

  $("#is_check_facebook").removeAttr("disabled", true);
  $("#facebook_checkbox").removeClass("disabled");
  facebook_checkbox_disabled.style.display = "none";
}

function disabled_facebook() {
  const facebook_checkbox_disabled = document.getElementById("facebook_checkbox_disabled");

  $("#is_check_facebook").attr("disabled", true);
  $("#facebook_checkbox").addClass("disabled");
  facebook_checkbox_disabled.style.display = "flex";
}
///////////////////////////////////////////////////////////////////
// Show Icon
///////////////////////////////////////////////////////////////////
function show_instagram_icon() {
  const instagram_icon = document.getElementById("icon_instagram");
  instagram_icon.style.display = "block";
}

function show_facebook_icon() {
  const facebook_icon = document.getElementById("icon_facebook");
  facebook_icon.style.display = "block";
}
///////////////////////////////////////////////////////////////////
// Unshow Icon
///////////////////////////////////////////////////////////////////
function unshow_instagram_icon() {
  const instagram_icon = document.getElementById("icon_instagram");
  instagram_icon.style.display = "none";
}

function unshow_facebook_icon() {
  const facebook_icon = document.getElementById("icon_facebook");
  facebook_icon.style.display = "none";
}
///////////////////////////////////////////////////////////////////
// Enable / Disable Submit Button
///////////////////////////////////////////////////////////////////
function change_button_context(work_type) {

  ///////////////////////////////////////////////////

  const story_button = document.getElementById("story_button");
  const story_button_selected = document.getElementById("story_button_selected");
  const post_button = document.getElementById("post_button");
  const post_button_selected = document.getElementById("post_button_selected");
  const post_story_button = document.getElementById("post_story_button");
  const post_story_button_selected = document.getElementById("post_story_button_selected");

  ///////////////////////////////////////////////////
  if(work_type === "story") {
    story_button.style.display = "none";
    story_button_selected.style.display = "flex";
    
    post_button.style.display = "flex";
    post_button_selected.style.display = "none";

    post_story_button.style.display = "flex";
    post_story_button_selected.style.display = "none";
  }
  ///////////////////////////////////////////////////
  if(work_type === "post") {
    story_button.style.display = "flex";
    story_button_selected.style.display = "none";
    
    post_button.style.display = "none";
    post_button_selected.style.display = "flex";

    post_story_button.style.display = "flex";
    post_story_button_selected.style.display = "none";
  }
  ///////////////////////////////////////////////////
  if(work_type === "post_story") {
    story_button.style.display = "flex";
    story_button_selected.style.display = "none";
    
    post_button.style.display = "flex";
    post_button_selected.style.display = "none";

    post_story_button.style.display = "none";
    post_story_button_selected.style.display = "flex";
  }
  ///////////////////////////////////////////////////
}
///////////////////////////////////////////////////////////////////
// Responsive Value
///////////////////////////////////////////////////////////////////
function change_budget() {
  $("#res_budget").html(numberWithCommas($('#budget').val()));
  $("#budget").val(numberWithCommas($('#budget').val()));
}
///////////////////////////////////////////////////////////////////
// Responsive Value
///////////////////////////////////////////////////////////////////
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
// Calculate Price
///////////////////////////////////////////////////////////////////
function cal_price() {
  const input = document.getElementById("budget").value;
  const budget = input.replace(',','');

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

  // // Reach
  // Story
  let min_fc_story_reach = get_reach(budget, get_factor(min_fc_price_per_shouter, min_avg_story_reach_per_shouter))
  let max_fc_story_reach = get_reach(budget, get_factor(max_fc_price_per_shouter, max_avg_story_reach_per_shouter))
  let min_ugc_story_reach = get_reach(budget, get_factor(min_ugc_price_per_shouter, min_avg_story_reach_per_shouter))
  let max_ugc_story_reach = get_reach(budget, get_factor(max_ugc_price_per_shouter, max_avg_story_reach_per_shouter))
  // Post
  let min_single_post_reach = get_reach(budget, get_factor(min_single_price_per_shouter, min_avg_post_reach_per_shouter))
  let max_single_post_reach = get_reach(budget, get_factor(max_single_price_per_shouter, max_avg_post_reach_per_shouter))
  let min_multi_post_reach = get_reach(budget, get_factor(min_multi_price_per_shouter, min_avg_post_reach_per_shouter))
  let max_multi_post_reach = get_reach(budget, get_factor(max_multi_price_per_shouter, max_avg_post_reach_per_shouter))
  // Story + Post
  let min_fc_single_reach = get_reach(budget,
    get_factor((min_fc_price_per_shouter + min_single_price_per_shouter) * 0.9,
      min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter
      )
  )
  let max_fc_single_reach = get_reach(budget,
    get_factor((max_fc_price_per_shouter + max_single_price_per_shouter) * 0.9,
    max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter
    )
  )
  let min_ugc_multi_reach = get_reach(budget,
    get_factor((min_ugc_price_per_shouter + min_multi_price_per_shouter) * 0.9,
      min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter
      )
  )
  let max_ugc_multi_reach = get_reach(budget,
    get_factor((max_ugc_price_per_shouter + max_multi_price_per_shouter) * 0.9,
    max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter
    )
  )

  // Min Max Reach
  let min_story_reach = Math.min(min_fc_story_reach, max_fc_story_reach, min_ugc_story_reach, max_ugc_story_reach)
  let max_story_reach = Math.max(min_fc_story_reach, max_fc_story_reach, min_ugc_story_reach, max_ugc_story_reach)
  let min_post_reach = Math.min(min_single_post_reach, max_single_post_reach, min_multi_post_reach, max_multi_post_reach)
  let max_post_reach = Math.max(min_single_post_reach, max_single_post_reach, min_multi_post_reach, max_multi_post_reach)
  let min_story_post_reach = Math.min(min_fc_single_reach, max_fc_single_reach, min_ugc_multi_reach, max_ugc_multi_reach)
  let max_story_post_reach = Math.max(min_fc_single_reach, max_fc_single_reach, min_ugc_multi_reach, max_ugc_multi_reach)


  // // Shouter
  // Story
  let min_fc_story_shouter = get_shouter(min_fc_story_reach, min_avg_story_reach_per_shouter)
  let max_fc_story_shouter = get_shouter(max_fc_story_reach, max_avg_story_reach_per_shouter)
  let min_ugc_story_shouter = get_shouter(min_ugc_story_reach, min_avg_story_reach_per_shouter)
  let max_ugc_story_shouter = get_shouter(max_ugc_story_reach, max_avg_story_reach_per_shouter)
  // Post
  let min_single_post_shouter = get_shouter(min_single_post_reach, min_avg_post_reach_per_shouter)
  let max_single_post_shouter = get_shouter(max_single_post_reach, max_avg_post_reach_per_shouter)
  let min_multi_post_shouter = get_shouter(min_multi_post_reach, min_avg_post_reach_per_shouter)
  let max_multi_post_shouter = get_shouter(max_multi_post_reach, max_avg_post_reach_per_shouter)
  // Story + Post
  let min_fc_single_shouter = get_shouter(min_fc_single_reach, min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter)
  let max_fc_single_shouter = get_shouter(max_fc_single_reach, max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter)
  let min_ugc_multi_shouter = get_shouter(min_ugc_multi_reach, min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter)
  let max_ugc_multi_shouter = get_shouter(max_ugc_multi_reach, max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter)

  // Min Max Shouter
  let min_story_shouter = Math.min(min_fc_story_shouter, max_fc_story_shouter, min_ugc_story_shouter, max_ugc_story_shouter)
  let max_story_shouter = Math.max(min_fc_story_shouter, max_fc_story_shouter, min_ugc_story_shouter, max_ugc_story_shouter)
  let min_post_shouter = Math.min(min_single_post_shouter, max_single_post_shouter, min_multi_post_shouter, max_multi_post_shouter)
  let max_post_shouter = Math.max(min_single_post_shouter, max_single_post_shouter, min_multi_post_shouter, max_multi_post_shouter)
  let min_story_post_shouter = Math.min(min_fc_single_shouter, max_fc_single_shouter, min_ugc_multi_shouter, max_ugc_multi_shouter)
  let max_story_post_shouter = Math.max(min_fc_single_shouter, max_fc_single_shouter, min_ugc_multi_shouter, max_ugc_multi_shouter)

  // // CPR
  // Story
  let min_fc_story_cpr = get_cpr(budget, min_fc_story_reach)
  let max_fc_story_cpr = get_cpr(budget, max_fc_story_reach)
  let min_ugc_story_cpr = get_cpr(budget, min_ugc_story_reach)
  let max_ugc_story_cpr = get_cpr(budget, max_ugc_story_reach)
  // Post
  let min_single_post_cpr = get_cpr(budget, min_single_post_reach)
  let max_single_post_cpr = get_cpr(budget, max_single_post_reach)
  let min_multi_post_cpr = get_cpr(budget, min_multi_post_reach)
  let max_multi_post_cpr = get_cpr(budget, max_multi_post_reach)
  // Story + Post
  let min_fc_single_cpr = get_cpr(budget, min_fc_single_reach)
  let max_fc_single_cpr = get_cpr(budget, max_fc_single_reach)
  let min_ugc_multi_cpr = get_cpr(budget, min_ugc_multi_reach)
  let max_ugc_multi_cpr= get_cpr(budget, max_ugc_multi_reach)

  // Min Max CPR
  let min_story_cpr = Math.min(min_fc_story_cpr, max_fc_story_cpr, min_ugc_story_cpr, max_ugc_story_cpr)
  let max_story_cpr = Math.max(min_fc_story_cpr, max_fc_story_cpr, min_ugc_story_cpr, max_ugc_story_cpr)
  let min_post_cpr = Math.min(min_single_post_cpr, max_single_post_cpr, min_multi_post_cpr, max_multi_post_cpr)
  let max_post_cpr = Math.max(min_single_post_cpr, max_single_post_cpr, min_multi_post_cpr, max_multi_post_cpr)
  let min_story_post_cpr = Math.min(min_fc_single_cpr, max_fc_single_cpr, min_ugc_multi_cpr, max_ugc_multi_cpr)
  let max_story_post_cpr = Math.max(min_fc_single_cpr, max_fc_single_cpr, min_ugc_multi_cpr, max_ugc_multi_cpr)

  if (check_facebook()) {
    // Reach
    min_story_reach = fb_100(min_story_reach)
    max_story_reach = fb_100(max_story_reach)
    min_post_reach = fb_100(min_post_reach)
    max_post_reach = fb_100(max_post_reach)
    min_story_post_reach = fb_100(min_story_post_reach)
    max_story_post_reach = fb_100(max_story_post_reach)
    // Shouter
    min_story_shouter = fb(min_story_shouter)
    max_story_shouter = fb(max_story_shouter)
    min_post_shouter = fb(min_post_shouter)
    max_post_shouter = fb(max_post_shouter)
    min_story_post_shouter = fb(min_story_post_shouter)
    max_story_post_shouter = fb(max_story_post_shouter)
    // CPR
    min_story_cpr = fb_2de(min_story_cpr)
    max_story_cpr = fb_2de(max_story_cpr)
    min_post_cpr = fb_2de(min_post_cpr)
    max_post_cpr = fb_2de(max_post_cpr)
    min_story_post_cpr = fb_2de(min_story_post_cpr)
    max_story_post_cpr = fb_2de(max_story_post_cpr)
  }

  // console.log(min_story_reach, max_story_reach, min_post_reach, max_post_reach, min_story_post_reach, max_story_post_reach)
  // console.log(min_story_shouter, max_story_shouter, min_post_shouter, max_post_shouter, min_story_post_shouter, max_story_post_shouter)
  // console.log(min_story_cpr, max_story_cpr, min_post_cpr, max_post_cpr, min_story_post_cpr, max_story_post_cpr)

  return {
    "min_story_reach": min_story_reach,
    "max_story_reach": max_story_reach,
    "min_post_reach": min_post_reach,
    "max_post_reach": max_post_reach,
    "min_story_post_reach": min_story_post_reach,
    "max_story_post_reach": max_story_post_reach,

    "min_story_shouter": min_story_shouter,
    "max_story_shouter": max_story_shouter,
    "min_post_shouter": min_post_shouter,
    "max_post_shouter": max_post_shouter,
    "min_story_post_shouter": min_story_post_shouter,
    "max_story_post_shouter": max_story_post_shouter,

    "min_story_cpr": min_story_cpr,
    "max_story_cpr": max_story_cpr,
    "min_post_cpr": min_post_cpr,
    "max_post_cpr": max_post_cpr,
    "min_story_post_cpr": min_story_post_cpr,
    "max_story_post_cpr": max_story_post_cpr
  }
}
///////////////////////////////////////////////////////////////////
// Set Value
///////////////////////////////////////////////////////////////////
function set_input_value(dict) {
  document.getElementById("shouter_story").innerHTML = numberWithCommas(dict["min_story_shouter"]) + " - " + numberWithCommas(dict["max_story_shouter"]) + " คน"
  document.getElementById("reach_story").innerHTML = numberWithCommas(dict["min_story_reach"]) + " - " + numberWithCommas(dict["max_story_reach"]) + " reach"
  document.getElementById("cpr_story").innerHTML = numberWithCommas(dict["min_story_cpr"]) + " - " + numberWithCommas(dict["max_story_cpr"]) + " บาท"

  document.getElementById("shouter_post").innerHTML = numberWithCommas(dict["min_post_shouter"]) + " - " + numberWithCommas(dict["max_post_shouter"]) + " คน"
  document.getElementById("reach_post").innerHTML = numberWithCommas(dict["min_post_reach"]) + " - " + numberWithCommas(dict["max_post_reach"]) + " reach"
  document.getElementById("cpr_post").innerHTML = numberWithCommas(dict["min_post_cpr"]) + " - " + numberWithCommas(dict["max_post_cpr"]) + " บาท"

  document.getElementById("shouter_post_story").innerHTML = numberWithCommas(dict["min_story_post_shouter"]) + " - " + numberWithCommas(dict["max_story_post_shouter"]) + " คน"
  document.getElementById("reach_post_story").innerHTML = numberWithCommas(dict["min_story_post_reach"]) + " - " + numberWithCommas(dict["max_story_post_reach"]) + " reach"
  document.getElementById("cpr_post_story").innerHTML = numberWithCommas(dict["min_story_post_cpr"]) + " - " + numberWithCommas(dict["max_story_post_cpr"]) + " บาท"
}

function set_value_story(min_story_shouter, max_story_shouter, min_story_reach, max_story_reach, min_story_cpr, max_story_cpr) {
  document.getElementById("number_shouter").innerHTML = numberWithCommas(min_story_shouter) + " - " + numberWithCommas(max_story_shouter) + " คน"
  document.getElementById("number_reach").innerHTML = numberWithCommas(min_story_reach) + " - " + numberWithCommas(max_story_reach) + " reach"
  document.getElementById("number_cpr").innerHTML = numberWithCommas(min_story_cpr) + " - " + numberWithCommas(max_story_cpr) + " บาท"
}

function set_value_post(min_post_shouter, max_post_shouter, min_post_reach, max_post_reach, min_post_cpr, max_post_cpr) {
  document.getElementById("number_shouter").innerHTML = numberWithCommas(min_post_shouter) + " - " + numberWithCommas(max_post_shouter) + " คน"
  document.getElementById("number_reach").innerHTML = numberWithCommas(min_post_reach) + " - " + numberWithCommas(max_post_reach) + " reach"
  document.getElementById("number_cpr").innerHTML = numberWithCommas(min_post_cpr) + " - " + numberWithCommas(max_post_cpr) + " บาท"
}

function set_value_post_story(min_story_post_shouter, max_story_post_shouter, min_story_post_reach, max_story_post_reach, min_story_post_cpr, max_story_post_cpr) {
  document.getElementById("number_shouter").innerHTML = numberWithCommas(min_story_post_shouter) + " - " + numberWithCommas(max_story_post_shouter) + " คน"
  document.getElementById("number_reach").innerHTML = numberWithCommas(min_story_post_reach) + " - " + numberWithCommas(max_story_post_reach) + " reach"
  document.getElementById("number_cpr").innerHTML = numberWithCommas(min_story_post_cpr) + " - " + numberWithCommas(max_story_post_cpr) + " บาท"
}
///////////////////////////////////////////////////////////////////
// Document Ready Function
///////////////////////////////////////////////////////////////////
$(document).ready(function(){
  $('.campaign__create__content__scope').on('change', function() {
    if(check_social() && check_budget() && check_work_type()) {
      $("#submit_button").removeClass("btn__grey");
      $("#submit_button").removeAttr("disabled", true);
    }
    if(!check_social() || !check_budget() || !check_work_type()) {
      $("#submit_button").addClass("btn__grey");
      $("#submit_button").attr("disabled", true);
    }
    if(check_social()) {
      enable_facebook();
      show_instagram_icon();
    }
    if(check_facebook()) {
      show_facebook_icon();
    }
    if(!check_social()) {
      disabled_facebook();
      unshow_instagram_icon();
      unshow_facebook_icon();
    }
    if(!check_facebook()) {
      unshow_facebook_icon();
    }
    if(check_budget()) {
      change_budget();
      const dict = cal_price();
      set_input_value(dict);
    }
    if(check_work_type()) {
      const dict = cal_price();
      if($('#story').is(":checked")) {
        set_value_story(dict["min_story_shouter"], dict["max_story_shouter"], dict["min_story_reach"], dict["max_story_reach"], dict["min_story_cpr"], dict["max_story_cpr"])
      }
      if($('#post').is(":checked")) {
        set_value_post(dict["min_post_shouter"], dict["max_post_shouter"], dict["min_post_reach"], dict["max_post_reach"], dict["min_post_cpr"], dict["max_post_cpr"])
      }
      if($('#post_story').is(":checked")) {
        set_value_post_story(dict["min_story_post_shouter"], dict["max_story_post_shouter"], dict["min_story_post_reach"], dict["max_story_post_reach"]
        , dict["min_story_post_cpr"], dict["max_story_post_cpr"])
      }
    }
  });
});
///////////////////////////////////////////////////////////////////