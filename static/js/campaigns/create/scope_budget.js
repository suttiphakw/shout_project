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
// Respnosive Value
///////////////////////////////////////////////////////////////////
function change_budget() {
  $("#res_budget").html(numberWithCommas($('#budget').val()));
  $("#budget").val(numberWithCommas($('#budget').val()));
}
///////////////////////////////////////////////////////////////////
// Respnosive Value
///////////////////////////////////////////////////////////////////
function cal_price() {
  const input = document.getElementById("budget").value;
  const budget = input.replace(',','');

  // Constant AVG. Reach
  min_avg_story_reach_factor = 621
  max_avg_story_reach_factor = 2300
  min_avg_post_reach_factor = 3000
  max_avg_post_reach_factor = 7250
  min_avg_story_post_reach_factor = 3621
  max_avg_story_post_reach_factor = 9550

  // Constant Story FC
  min_fc_story_reach_factor = 0.805
  max_fc_story_reach_factor = 0.634

  // Constant Story UGC
  min_ugc_story_reach_factor = 1.261
  max_ugc_story_reach_factor = 1.014

  // Constant Post Single
  min_single_post_reach_factor = 0.667
  max_single_post_reach_factor = 0.506

  // Constant Post Multi
  min_multi_post_reach_factor = 0.833
  max_multi_post_reach_factor = 0.607

  // Constant Story + Post Lower
  min_lower_story_post_reach_factor = 0.621
  max_lower_story_post_reach_factor = 0.483

  // Constant Story + Post Upper
  min_upper_story_post_reach_factor = 0.816
  max_upper_story_post_reach_factor = 0.635

  // Calculate Story Shouter
  min_story_shouter = Math.round((budget/max_ugc_story_reach_factor)/max_avg_story_reach_factor)
  max_story_shouter = Math.round((budget/min_fc_story_reach_factor)/min_avg_story_reach_factor)

  // Calculate Post Shouter
  min_post_shouter = Math.round((budget/max_multi_post_reach_factor)/max_avg_post_reach_factor)
  max_post_shouter = Math.round((budget/min_single_post_reach_factor)/min_avg_post_reach_factor)

  // Calculate Story + Post Shouer
  min_story_post_shouter = Math.round((budget/max_upper_story_post_reach_factor)/max_avg_story_post_reach_factor)
  max_story_post_shouter = Math.round((budget/min_lower_story_post_reach_factor)/min_avg_story_post_reach_factor)

  // Calculate Story Reach
  min_story_reach = Math.round((budget/min_ugc_story_reach_factor)/100) * 100
  max_story_reach = Math.round((budget/max_fc_story_reach_factor)/100) * 100

  // Calculate Post Reach
  min_post_reach = Math.round((budget/min_multi_post_reach_factor)/100) * 100
  max_post_reach = Math.round((budget/max_single_post_reach_factor)/100) * 100

  // Calculate Story Post Reach
  min_story_post_reach = Math.round((budget/min_upper_story_post_reach_factor)/100) * 100
  max_story_post_reach = Math.round((budget/max_lower_story_post_reach_factor)/100) * 100

  // Calculate CPR Story
  min_story_cpr = parseFloat((budget/max_story_reach).toFixed(2))
  max_story_cpr = parseFloat((budget/min_story_reach).toFixed(2))

  // Calculate CPR Post
  min_post_cpr = parseFloat((budget/max_post_reach).toFixed(2))
  max_post_cpr = parseFloat((budget/min_post_reach).toFixed(2))

  // Calculate CPR Story + Post
  min_story_post_cpr = parseFloat((budget/max_story_post_reach).toFixed(2))
  max_story_post_cpr = parseFloat((budget/min_story_post_reach).toFixed(2))

  return {
    "min_story_shouter": min_story_shouter,
    "max_story_shouter": max_story_shouter,
    "min_post_shouter": min_post_shouter,
    "max_post_shouter": max_post_shouter,
    "min_story_post_shouter": min_story_post_shouter,
    "max_story_post_shouter": max_story_post_shouter,
    "min_story_reach": min_story_reach,
    "max_story_reach": max_story_reach,
    "min_post_reach": min_post_reach,
    "max_post_reach": max_post_reach,
    "min_story_post_reach": min_story_post_reach,
    "max_story_post_reach": max_story_post_reach,
    "min_story_cpr": min_story_cpr,
    "max_story_cpr": max_story_cpr,
    "min_post_cpr": min_post_cpr,
    "max_post_cpr": max_post_cpr,
    "min_story_post_cpr": min_story_post_cpr,
    "max_story_post_cpr": max_story_post_cpr
  }

  // Change Inner HTML Value

  // // Shouter
  // document.getElementById("story_shouter").innerHTML = numberWithCommas(min_story_shouter) + " - " + numberWithCommas(max_story_shouter) + " คน"
  // document.getElementById("post_shouter").innerHTML = numberWithCommas(min_post_shouter) + " - " + numberWithCommas(max_post_shouter) + " คน"
  // document.getElementById("story_post_shouter").innerHTML = numberWithCommas(min_story_post_shouter) + " - " + numberWithCommas(max_story_post_shouter) + " คน"

  // // Reach
  // document.getElementById("story_reach").innerHTML = numberWithCommas(min_story_reach) + " - " + numberWithCommas(max_story_reach) + " reach"
  // document.getElementById("post_reach").innerHTML = numberWithCommas(min_post_reach) + " - " + numberWithCommas(max_post_reach) + " reach"
  // document.getElementById("story_post_reach").innerHTML = numberWithCommas(min_story_post_reach) + " - " + numberWithCommas(max_story_post_reach) + " reach"

  // // CPR
  // document.getElementById("story_cpr").innerHTML = min_story_cpr + " - " + max_story_cpr + " บาท"
  // document.getElementById("post_cpr").innerHTML = min_post_cpr + " - " + max_post_cpr + " บาท"
  // document.getElementById("story_post_cpr").innerHTML = min_story_post_cpr + " - " + max_story_post_cpr + " บาท"

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