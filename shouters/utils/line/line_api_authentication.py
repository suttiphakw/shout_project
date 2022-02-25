import requests
from shouters.utils import settings

def line_auth(state):
  return f'{settings.line_authentication_uri}' \
         f'?response_type={settings.line_response_type}' \
         f'&client_id={settings.line_client_id}' \
         f'&redirect_uri={settings.line_redirect_uri}' \
         f'&state={state}&scope={settings.line_scope}'

def get(code):
  params = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': settings.line_redirect_uri,
    'client_id': settings.line_client_id,
    'client_secret': settings.line_client_secret,
  }
  # Response API
  response = requests.post(settings.line_endpoint + 'token/',
                           data=params)

  # Check Response
  if not response.ok:
    return False

  data = response.json()
  try:
    access_token = data['access_token']
    id_token = data['id_token']
  except:
    return False

  context = {
    'access_token': access_token,
    'id_token': id_token
  }

  # Return context
  return context



