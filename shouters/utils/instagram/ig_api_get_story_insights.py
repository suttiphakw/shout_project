import requests
from shouters.utils import settings

def get(story_id, access_token):
  params = {
    'access_token': access_token,
    'metric': 'exits,impressions,reach,replies,taps_forward,taps_back'
  }
  response = requests.get(settings.fb_endpoint + story_id + '/insights',
                          params=params)
  if not response.ok:
    return False

  data = response.json()
  data = data['data']

  return data