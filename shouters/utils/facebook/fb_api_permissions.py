import requests
from shouters.utils import settings

def get(access_token):
  params = {
    'access_token': access_token
  }
  response = requests.get(settings.fb_endpoint + 'me/permissions/', params=params)
  if not response.ok:
    return False

  data = response.json()
  permissions = data['data']
  context = {
    'permissions': permissions
  }
  return context

def delete(access_token):
  params = {
    'access_token': access_token
  }
  response = requests.delete(settings.fb_endpoint + 'me/permissions/',
                             params=params)
  if not response.ok:
    return False

  return True