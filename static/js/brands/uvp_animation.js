function change_page_0() {
  const active_page_0 = document.getElementById("default_uvp");
  const active_page_1 = document.getElementById("uvp_1");
  const active_page_2 = document.getElementById("uvp_2");
  const active_page_3 = document.getElementById("uvp_3");
  const active_page_4 = document.getElementById("uvp_4");
  const active_page_5 = document.getElementById("uvp_5");
  active_page_0.style.display = "block";
  active_page_1.style.display = "none";
  active_page_2.style.display = "none";
  active_page_3.style.display = "none";
  active_page_4.style.display = "none";
  active_page_5.style.display = "none";
} 

function change_page_1() {
  const active_page_0 = document.getElementById("default_uvp");
  const active_page_1 = document.getElementById("uvp_1");
  const active_page_2 = document.getElementById("uvp_2");
  const active_page_3 = document.getElementById("uvp_3");
  const active_page_4 = document.getElementById("uvp_4");
  const active_page_5 = document.getElementById("uvp_5");
  active_page_0.style.display = "none";
  active_page_1.style.display = "block";
  active_page_2.style.display = "none";
  active_page_3.style.display = "none";
  active_page_4.style.display = "none";
  active_page_5.style.display = "none";
}

function change_page_2() {
  const active_page_0 = document.getElementById("default_uvp");
  const active_page_1 = document.getElementById("uvp_1");
  const active_page_2 = document.getElementById("uvp_2");
  const active_page_3 = document.getElementById("uvp_3");
  const active_page_4 = document.getElementById("uvp_4");
  const active_page_5 = document.getElementById("uvp_5");
  active_page_0.style.display = "none";
  active_page_1.style.display = "none";
  active_page_2.style.display = "block";
  active_page_3.style.display = "none";
  active_page_4.style.display = "none";
  active_page_5.style.display = "none";
}

function change_page_3() {
  const active_page_0 = document.getElementById("default_uvp");
  const active_page_1 = document.getElementById("uvp_1");
  const active_page_2 = document.getElementById("uvp_2");
  const active_page_3 = document.getElementById("uvp_3");
  const active_page_4 = document.getElementById("uvp_4");
  const active_page_5 = document.getElementById("uvp_5");
  active_page_0.style.display = "none";
  active_page_1.style.display = "none";
  active_page_2.style.display = "none";
  active_page_3.style.display = "block";
  active_page_4.style.display = "none";
  active_page_5.style.display = "none";
}

function change_page_4() {
  const active_page_0 = document.getElementById("default_uvp");
  const active_page_1 = document.getElementById("uvp_1");
  const active_page_2 = document.getElementById("uvp_2");
  const active_page_3 = document.getElementById("uvp_3");
  const active_page_4 = document.getElementById("uvp_4");
  const active_page_5 = document.getElementById("uvp_5");
  active_page_0.style.display = "none";
  active_page_1.style.display = "none";
  active_page_2.style.display = "none";
  active_page_3.style.display = "none";
  active_page_4.style.display = "block";
  active_page_5.style.display = "none";
}

function change_page_5() {
  const active_page_0 = document.getElementById("default_uvp");
  const active_page_1 = document.getElementById("uvp_1");
  const active_page_2 = document.getElementById("uvp_2");
  const active_page_3 = document.getElementById("uvp_3");
  const active_page_4 = document.getElementById("uvp_4");
  const active_page_5 = document.getElementById("uvp_5");
  active_page_0.style.display = "none";
  active_page_1.style.display = "none";
  active_page_2.style.display = "none";
  active_page_3.style.display = "none";
  active_page_4.style.display = "none";
  active_page_5.style.display = "block";
}

function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function cal_price() {
  const budget = document.getElementById("budget").value;

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

  // console.log("=========================")
  // console.log("Number of Shouter")
  // console.log("=========================")
  // console.log("Story : ", min_story_shouter, " - ", max_story_shouter)
  // console.log("Post : ", min_post_shouter, " - ", max_post_shouter)
  // console.log("Story + Post : ", min_story_post_shouter, " - ", max_story_post_shouter)
  // console.log("=========================")
  // console.log("Estimated Reach")
  // console.log("=========================")
  // console.log("Story : ", min_story_reach, " - ", max_story_reach)
  // console.log("Post : ", min_post_reach, " - ", max_post_reach)
  // console.log("Story + Post : ", min_story_post_reach, " - ", max_story_post_reach)
  // console.log("=========================")
  // console.log("Cost Per Reach")
  // console.log("Story : ", min_story_cpr, " - ", max_story_cpr)
  // console.log("Post : ", min_post_cpr, " - ", max_post_cpr)
  // console.log("Story + Post : ", min_story_post_cpr, " - ", max_story_post_cpr)

  // Change Inner HTML Value

  // Shouter
  document.getElementById("story_shouter").innerHTML = numberWithCommas(min_story_shouter) + " - " + numberWithCommas(max_story_shouter) + " คน"
  document.getElementById("post_shouter").innerHTML = numberWithCommas(min_post_shouter) + " - " + numberWithCommas(max_post_shouter) + " คน"
  document.getElementById("story_post_shouter").innerHTML = numberWithCommas(min_story_post_shouter) + " - " + numberWithCommas(max_story_post_shouter) + " คน"

  // Reach
  document.getElementById("story_reach").innerHTML = numberWithCommas(min_story_reach) + " - " + numberWithCommas(max_story_reach) + " reach"
  document.getElementById("post_reach").innerHTML = numberWithCommas(min_post_reach) + " - " + numberWithCommas(max_post_reach) + " reach"
  document.getElementById("story_post_reach").innerHTML = numberWithCommas(min_story_post_reach) + " - " + numberWithCommas(max_story_post_reach) + " reach"

  // CPR
  document.getElementById("story_cpr").innerHTML = min_story_cpr + " - " + max_story_cpr + " บาท"
  document.getElementById("post_cpr").innerHTML = min_post_cpr + " - " + max_post_cpr + " บาท"
  document.getElementById("story_post_cpr").innerHTML = min_story_post_cpr + " - " + max_story_post_cpr + " บาท"

}

var myVar = false;
function resolveAfter10Seconds() {
  return new Promise(resolve => {
    setTimeout(() => {resolve()}, 10000);
  });
}

function stopChange_uvp() {
  console.log('test');
  myVar = true;
}

async function change_uvp(){
  if(myVar === true) {
    return
  } else {
    change_page_0();
    await resolveAfter10Seconds();
  }
  if(myVar === true) {
    return
  } else {
    change_page_1();
    await resolveAfter10Seconds();
  }
  if(myVar === true) {
    return
  } else {
    change_page_2();
    await resolveAfter10Seconds();
  }
  if(myVar === true) {
    return
  } else {
    change_page_3();
    await resolveAfter10Seconds();
  }
  if(myVar === true) {
    return
  } else {
    change_page_4();
    await resolveAfter10Seconds();
  }
  if(myVar === true) {
    return
  } else {
    change_page_5();
    await resolveAfter10Seconds();
  }
  setTimeout(change_uvp(), 10000);
}

// function updateTextView(_obj){
//   var num = getNumber(_obj.val());
//   if(num==0){
//     _obj.val('');
//   }else{
//     _obj.val(num.toLocaleString());
//   }
// }
// function getNumber(_str){
//   var arr = _str.toString().split('');
//   var out = new Array();
//   for(var cnt=0;cnt<arr.length;cnt++){
//     if(isNaN(arr[cnt])==false){
//       out.push(arr[cnt]);
//     }
//   }
//   return Number(out.join(''));
// }

$(document).ready(function(){
  change_uvp();
});
