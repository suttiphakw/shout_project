import requests
from shouters.utils import settings

def get(access_token):
  params = {
    'access_token': access_token
  }
  response = requests.get(settings.fb_endpoint + 'me/accounts/',
                          params=params)
  if not response.ok:
    return False

  data = response.json()
  try:
    objs = data['data']
  except:
    return False

  context = {
    'objs': objs
  }

  return context