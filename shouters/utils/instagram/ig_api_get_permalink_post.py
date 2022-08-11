import requests
from shouters.utils import settings


def get(post_list, access_token, url):

  for post in post_list:
    post_id = post['id']
    params = {
      'fields': 'permalink, like_count, comments_count',
      'access_token': access_token
    }
    response = requests.get(settings.fb_endpoint + post_id, params=params)
    if not response.ok:
      return False

    data = response.json()

    if data['permalink'] not in url:
      continue

    like_count = data['like_count']
    comments_count = data['comments_count']
    return post_id, like_count, comments_count

  return False, False, False
