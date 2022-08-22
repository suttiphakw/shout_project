const endpoint = campaign_id => `/apiapp/campaigns/create/content_type/${campaign_id}/`
const redirect_url = campaign_id => `/campaigns/create/product/${campaign_id}/`

// Redirect Function
const redirect = url => window.location.href = `${url}`;

// Get Campaign ID Function
let campaign_id = window.location.href.split("/");
campaign_id = campaign_id[campaign_id.length - 2];

// GET INPUT
let context;
const get_input = () => {
  const story_type = $("input[name='story_type']:checked").val();
  const story_type_count = $("#campaign_fc_story_count").val();
  const post_type = $("input[name='post_type']:checked").val();

  context = {
    story_type,
    story_type_count,
    post_type,
  }
  console.log(context);
  return context;
};

// AXIOS
async function axiosPost(endpoint, data) {
  const response = await axios.post(endpoint, data);
  return response.data
}

// POST METHOD
const post_data = (csrf_token) => {
  // Input Data
  const input = get_input();

  // APPEND CSRF TOKEN + DATA
  let data = new FormData;
  data.append("csrfmiddlewaretoken", `${csrf_token}`);
  data.append("content_type_story", input.story_type);
  data.append("content_type_story_count", input.story_type_count);
  data.append("content_type_post", input.post_type);

  // POST
  axiosPost(endpoint(campaign_id), data)
    .then(res => {
      if (res.status === 'success') {
        console.log(res)
        redirect(redirect_url(campaign_id));
      } else {
        // 404 Error page
        // redirect(redirect_url(data.campaign_id));
        console.log('404Error')
      }
    })
    .catch(errors => console.log(errors));
};