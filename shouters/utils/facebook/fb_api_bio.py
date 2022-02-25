import requests
from shouters.utils import settings

def get(access_token):
  params = {
    'access_token': access_token,
    'fields': 'name,picture'
  }
  response = requests.get(settings.fb_endpoint + 'me/',
                          params=params)
  if not response.ok:
    return False

  data = response.json()
  try:
    fb_name = data['name']
    fb_profile_picture = data['picture']['data']['url']
  except:
    return False

  context = {
    'fb_name': fb_name,
    'fb_profile_picture': fb_profile_picture
  }
  return context

