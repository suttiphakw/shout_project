import requests
from shouters.utils import settings

def get(id_token):
  params = {
    'id_token': id_token,
    'client_id': settings.line_client_id
  }
  response = requests.get(settings.line_endpoint + 'verify/',
                          data=params)

  if not response.ok:
    return False

  data = response.json()
  try:
    line_user_id = data['sub']
    line_username = data['name']
  except:
    return False

  try:
    line_profile_picture = data['picture']
  except:
    line_profile_picture = None

  context = {
    'line_user_id': line_user_id,
    'line_username': line_username,
    'line_profile_picture': line_profile_picture
  }

  return context