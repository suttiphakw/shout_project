function submitForm() {
  const first_name = $('#first_name').val();
  const last_name = $('#last_name').val();
  const nickname = $('#nickname').val();
  const email = $('#email').val();
  const tel = $('#tel').val();
  const gender = $("input[type='radio'][name='gender']:checked").val();
  const birthday_date = $('#birthday_date').val();
  const birthday_month = $('#birthday_month').val();
  const birthday_year = $('#birthday_year').val();
  const province = $('#province').val();
  const education = $('#education').val();
  const college = $('#college').val();
  const interest = $('#interest').val();

  console.log(interest);

  if (first_name.trim() === '' || last_name.trim() === '' ||
    nickname.trim() === '' || email.trim() === '' || tel.trim() === '' || gender === undefined ||
    birthday_date.trim() === '' || birthday_month.trim() === '' || birthday_year.trim() === '' ||
    province.trim() === '' || education.trim() === '' || college.trim() === '' || interest.length === 0) {
    $(".submit_button").notify("Please fill in all information.", {position: "top left"}, "error");
  } else {
    if(interest.length > 5) {
      $(".submit_button").notify("Please choose max to 5 interest.", {position: "top left"}, "error");
    } else if(tel.length !== 10) {
      $(".submit_button").notify("Please enter tel 10 digit.", {position: "top left"}, "error");
    } else if(!email.includes("@")) {
      $(".submit_button").notify("Please enter correct form of email.", {position: "top left"}, "error");
    } else {
      $("#registration").submit();
    }
  }
}