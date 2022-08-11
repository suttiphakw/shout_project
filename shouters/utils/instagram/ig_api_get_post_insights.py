import requests
from shouters.utils import settings


def get(post_id, access_token):
  params = {
    'access_token': access_token,
    'metric': 'engagement,impressions,reach,saved'
  }
  response = requests.get(settings.fb_endpoint + post_id + '/insights', params=params)
  if not response.ok:
    return False

  data = response.json()
  return data['data']
