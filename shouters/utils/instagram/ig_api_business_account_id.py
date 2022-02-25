import requests
from shouters.utils import settings

def get(page_id, access_token):
  params = {
    'fields': 'instagram_business_account',
    'access_token': access_token
  }
  response = requests.get(settings.fb_endpoint + page_id,
                          params=params)
  if not response.ok:
    return False

  data = response.json()
  try:
    business_account_id = data['instagram_business_account']['id']
  except:
    return False

  context = {
    'data': data,
    'business_account_id': business_account_id
  }
  return context