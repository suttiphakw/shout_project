//////////////////////////////////////////////////////////////////////////
function showModal_1() {
  const modal_1_1 = document.getElementById("modal_1_1");
  modal_1_1.style.display = "flex";
}
function nextTo1_2() {
  const modal_1_1 = document.getElementById("modal_1_1");
  const modal_1_2 = document.getElementById("modal_1_2");
  modal_1_1.style.display = "none";
  modal_1_2.style.display = "flex";
}
function backTo1_1() {
  const modal_1_1 = document.getElementById("modal_1_1");
  const modal_1_2 = document.getElementById("modal_1_2");
  modal_1_1.style.display = "flex";
  modal_1_2.style.display = "none";
}
function nextTo1_3() {
  const modal_1_2 = document.getElementById("modal_1_2");
  const modal_1_3 = document.getElementById("modal_1_3");
  modal_1_2.style.display = "none";
  modal_1_3.style.display = "flex";
}
function backTo1_2() {
  const modal_1_2 = document.getElementById("modal_1_2");
  const modal_1_3 = document.getElementById("modal_1_3");
  modal_1_2.style.display = "flex";
  modal_1_3.style.display = "none";
}
//////////////////////////////////////////////////////////////////////////
function showModal_2() {
  const modal_2_1 = document.getElementById("modal_2_1");
  modal_2_1.style.display = "flex";
}
function nextTo2_2() {
  const modal_2_1 = document.getElementById("modal_2_1");
  const modal_2_2 = document.getElementById("modal_2_2");
  modal_2_1.style.display = "none";
  modal_2_2.style.display = "flex";
}
function backTo2_1() {
  const modal_2_1 = document.getElementById("modal_2_1");
  const modal_2_2 = document.getElementById("modal_2_2");
  modal_2_1.style.display = "flex";
  modal_2_2.style.display = "none";
}
function nextTo2_3() {
  const modal_2_2 = document.getElementById("modal_2_2");
  const modal_2_3 = document.getElementById("modal_2_3");
  modal_2_2.style.display = "none";
  modal_2_3.style.display = "flex";
}
function backTo2_2() {
  const modal_2_2 = document.getElementById("modal_2_2");
  const modal_2_3 = document.getElementById("modal_2_3");
  modal_2_2.style.display = "flex";
  modal_2_3.style.display = "none";
}
//////////////////////////////////////////////////////////////////////////
function showModal_3() {
  const modal_3_1 = document.getElementById("modal_3_1");
  modal_3_1.style.display = "flex";
}
function nextTo3_2() {
  const modal_3_1 = document.getElementById("modal_3_1");
  const modal_3_2 = document.getElementById("modal_3_2");
  modal_3_1.style.display = "none";
  modal_3_2.style.display = "flex";
}
function backTo3_1() {
  const modal_3_1 = document.getElementById("modal_3_1");
  const modal_3_2 = document.getElementById("modal_3_2");
  modal_3_1.style.display = "flex";
  modal_3_2.style.display = "none";
}
function nextTo3_3() {
  const modal_3_2 = document.getElementById("modal_3_2");
  const modal_3_3 = document.getElementById("modal_3_3");
  modal_3_2.style.display = "none";
  modal_3_3.style.display = "flex";
}
function backTo3_2() {
  const modal_3_2 = document.getElementById("modal_3_2");
  const modal_3_3 = document.getElementById("modal_3_3");
  modal_3_2.style.display = "flex";
  modal_3_3.style.display = "none";
}
//////////////////////////////////////////////////////////////////////////
function closeModal() {
  const modal_1_3 = document.getElementById("modal_1_3");
  const modal_2_3 = document.getElementById("modal_2_3");
  const modal_3_3 = document.getElementById("modal_3_3");
  modal_1_3.style.display = "none";
  modal_2_3.style.display = "none";
  modal_3_3.style.display = "none";
}
//////////////////////////////////////////////////////////////////////////
$(document).ready(function(){
  $('input[type="checkbox"]').click(function() {
    if($('#checkbox_1').is(":checked")
      && $('#checkbox_2').is(":checked")
      && $('#checkbox_3').is(":checked")) {
      $("#nextPage").removeClass("register__choose-device__button-disable");
    } else {
      $("#nextPage").addClass("register__choose-device__button-disable");
    }
  });
});
//////////////////////////////////////////////////////////////////////////