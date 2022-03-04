import requests
import statistics
from shouters.utils import settings

from shouters.utils.function import fn_engagement_outlier

def get_like(media_objects, access_token):
  params = {
    'fields': 'like_count',
    'access_token': access_token
  }
  raw_list = []
  id_list = []
  session = requests.Session()
  # shouter have media >= 15 media
  if len(media_objects) >= 15:
    for item in media_objects[0:15]:
      response = session.get(settings.fb_endpoint + item, params=params)
      data = response.json()
      if response.ok:
        try:
          raw_list.append(data['like_count'])
          id_list.append(item)
        except:
          continue
  # shouter have media < 15 media
  else:
    for item in media_objects[0:len(media_objects)]:
      response = session.get(settings.fb_endpoint + item, params=params)
      if response.ok:
        data = response.json()
        try:
          raw_list.append(data['like_count'])
          id_list.append(item)
        except:
          continue

  context = fn_engagement_outlier.cut(raw_list, id_list)
  # Return with context = {'list_like': list_like, 'mean_list': mean_list}
  # list_like = [{id: like_count}, ... ]
  return context


def get_reach(final_dict, access_token):
  params = {
    'metric': 'reach',
    'access_token': access_token
  }
  reach_list = []
  session = requests.Session()
  for key, value in final_dict.items():
    response = session.get(settings.fb_endpoint + key + '/insights', params=params)
    if not response.ok:
      break
    data = response.json()
    try:
      post_reach = data['data'][0]['values'][0]['value']
      if post_reach < value:
        continue
      reach_list.append(post_reach)
    except:
      continue

  # Calculate Average Post Reach
  if not reach_list:
    context = {
      'reach_list': reach_list
    }
    return context

  ig_average_post_reach = statistics.mean(reach_list)
  context = {
    'reach_list': reach_list,
    'ig_average_post_reach': ig_average_post_reach
  }
  return context


