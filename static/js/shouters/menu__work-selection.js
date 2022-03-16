function toggleVisible(bool) {
  return bool !== true;
}

function is_visible(bool, element) {
  if (bool === false) {
    element.style.display = "none";
  } else {
    element.style.display = "block";
  }
}

// IG
function is_check_ig() {
  const is_check_ig_bool = $("input[type='checkbox'][name='is_check_ig']").is(':checked');

  // Set Opposite
  const bool = toggleVisible(is_check_ig_bool);

  // Show / UnShow below detail
  const is_check_ig_visible = document.getElementById("is_check_ig_visible");
  is_visible(bool, is_check_ig_visible);
}


// IG + FB
function is_check_ig_fb() {
  const is_check_ig_fb_bool = $("input[type='checkbox'][name='is_check_ig_fb']").is(':checked');

  // Set Opposite
  const bool = toggleVisible(is_check_ig_fb_bool);

  // Show / UnShow below detail
  const is_check_ig_fb_visible = document.getElementById("is_check_ig_fb_visible");
  is_visible(bool, is_check_ig_fb_visible);
}


// TIKTOK
function is_check_tiktok() {
  const is_check_tiktok_bool = $("input[type='checkbox'][name='is_check_tiktok']").is(':checked');

  // Set Opposite
  const bool = toggleVisible(is_check_tiktok_bool);

  // Show / UnShow below detail
  const is_check_tiktok_visible = document.getElementById("is_check_tiktok_visible");
  is_visible(bool, is_check_tiktok_visible);
}


// TWITTER
function is_check_twitter() {
  const is_check_twitter_bool = $("input[type='checkbox'][name='is_check_twitter']").is(':checked');

  // Set Opposite
  const bool = toggleVisible(is_check_twitter_bool);

  // Show / UnShow below detail
  const is_check_twitter_visible = document.getElementById("is_check_twitter_visible");
  is_visible(bool, is_check_twitter_visible);
}



function defaultVisible() {
  // IG
  const is_check_ig_bool = $("input[type='checkbox'][name='is_check_ig']").is(':checked');
  // Show / UnShow below detail
  const is_check_ig_visible = document.getElementById("is_check_ig_visible");
  is_visible(is_check_ig_bool, is_check_ig_visible);

  // FB
  const is_check_ig_fb_bool = $("input[type='checkbox'][name='is_check_ig_fb']").is(':checked');
  // Show / UnShow below detail
  const is_check_ig_fb_visible = document.getElementById("is_check_ig_fb_visible");
  is_visible(is_check_ig_fb_bool, is_check_ig_fb_visible)

  // TIKTOK
  const is_check_tiktok_bool = $("input[type='checkbox'][name='is_check_tiktok']").is(':checked');
  // Show / UnShow below detail
  const is_check_tiktok_visible = document.getElementById("is_check_tiktok_visible");
  is_visible(is_check_tiktok_bool, is_check_tiktok_visible)

  // TWITTER
  const is_check_twitter_bool = $("input[type='checkbox'][name='is_check_twitter']").is(':checked');
  // Show / UnShow below detail
  const is_check_twitter_visible = document.getElementById("is_check_twitter_visible");
  is_visible(is_check_twitter_bool, is_check_twitter_visible)
}

$(document).ready(function(){
  console.log('ready')
  defaultVisible();
});
