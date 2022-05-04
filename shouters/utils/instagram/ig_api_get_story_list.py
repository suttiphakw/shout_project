import requests
from shouters.utils import settings

def get(business_account_id, access_token):
  params = {
    'access_token': access_token
  }
  response = requests.get(settings.fb_endpoint + business_account_id + '/stories',
                          params=params)
  if not response.ok:
    return False

  data = response.json()
  data = data['data']

  context = {
    'data': data
  }
  return context