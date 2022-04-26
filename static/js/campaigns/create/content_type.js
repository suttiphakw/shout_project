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