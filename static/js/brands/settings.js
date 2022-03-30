function change__password() {
  const default_page = document.getElementById("default");
  const change_password_page = document.getElementById("change_password");
  default_page.style.display = none;
  change_password_page.style.display = block;
}

function submit() {
  $("#change_profile").submit();
}