function submitForm() {
  const instagram = $("input[type='radio'][name='instagram']:checked").val();
  if (instagram === undefined) {
    $(".submit_button").notify("โปรดเลือก 1 บัญชี Instagram.", {position: "top left"}, "error");
  } else {
    $("#choose-instagram").submit();
  }
}

function removeClass() {
  $("#submitButton").removeClass('submit__disabled');
}