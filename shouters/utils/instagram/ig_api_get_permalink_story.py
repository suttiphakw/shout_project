import requests
from shouters.utils import settings


def get(story_list, access_token, url):

  for story in story_list:
    story_id = story['id']


    params = {
      'fields': 'permalink',
      'access_token': access_token
    }
    response = requests.get(settings.fb_endpoint + story_id,
                            params=params)
    if not response.ok:
      return False

    data = response.json()

    if data['permalink'] not in url:
      continue

    story_id = story_id
    return story_id

  return False