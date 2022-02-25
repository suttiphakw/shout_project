import requests
from shouters.utils import settings

def fb_auth(state):
  return f'{settings.fb_authentication_uri}' \
         f'?client_id={settings.fb_client_id}' \
         f'&redirect_uri={settings.fb_redirect_uri}' \
         f'&state={state}' \
         f'&scope={settings.fb_permissions_scope}'


def get(code):
  params = {
    'client_id': settings.fb_client_id,
    'redirect_uri': settings.fb_redirect_uri,
    'client_secret': settings.fb_client_secret,
    'code': code
  }
  # Response API
  response = requests.get(settings.fb_endpoint + 'oauth/access_token',
                          params=params)

  # Check Response
  if not response.ok:
    return False

  data = response.json()
  try:
    access_token = data['access_token']
  except:
    return False

  # Return access_token
  return access_token

def params(code):
  return {
    'client_id': settings.fb_client_id,
    'redirect_uri': settings.fb_redirect_uri,
    'client_secret': settings.fb_client_secret,
    'code': code
  }