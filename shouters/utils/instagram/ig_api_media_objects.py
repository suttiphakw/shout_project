import requests
from shouters.utils import settings


def get(business_account_id, access_token):
  params = {
    'access_token': access_token
  }
  response = requests.get(settings.fb_endpoint + business_account_id + '/media',
                          params=params)
  if not response.ok:
    return False

  data = response.json()
  try:
    items = data['data']
    media_objects = [item['id'] for item in items]
  except KeyError:
    media_objects = []

  context = {
    'data': data,
    'media_objects': media_objects
  }
  return context
