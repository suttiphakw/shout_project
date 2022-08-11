const endpoint = "/apiapp/campaigns/create/name/"
const redirect_url = campaign_id => `/campaigns/create/scope_budget/${campaign_id}/`

const redirect = url => window.location.href = `${url}`;

// GET INPUT
let context;
const get_input = () => {
  const campaign_name = $("#campaign_name").val();
  context = {
    campaign_name
  }
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
  data.append("campaign_name", input.campaign_name);

  // POST
  axiosPost(endpoint, data)
    .then(res => {
      if (res.campaign_id) {
        redirect(redirect_url(res.campaign_id));
      } else {
        // 404 Error page
        // redirect(redirect_url(data.campaign_id));
        console.log('404Error')
      }
    })
    .catch(errors => console.log(errors));
};