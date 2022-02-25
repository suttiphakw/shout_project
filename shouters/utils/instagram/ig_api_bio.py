import requests
from shouters.utils import settings

def get(business_account_id, access_token):
  params = {
    'fields': ','.join(settings.ig_bio_scope),
    'access_token': access_token
  }
  response = requests.get(settings.fb_endpoint_v3_2 + business_account_id,
                          params=params)
  if not response.ok:
    return False

  data = response.json()
  try:
    username = data['username']
    media_count = data['media_count']
    followers_count = data['followers_count']
    followings_count = data['follows_count']
    ig_profile_picture = data['profile_picture_url']
  except ValueError:
    return False

  context = {
    'username': username,
    'media_count': media_count,
    'followers_count': followers_count,
    'followings_count': followings_count,
    'ig_profile_picture': ig_profile_picture,
  }
  return context