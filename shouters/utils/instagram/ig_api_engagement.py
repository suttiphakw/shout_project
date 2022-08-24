import requests
import statistics
from shouters.utils import settings

from shouters.utils.function import fn_engagement_outlier


def get_like(media_objects, access_token):
  params = {
    'fields': 'like_count, media_url',
    'access_token': access_token
  }
  raw_list = []
  id_list = []
  media_srcs = []
  session = requests.Session()
  # shouter have media >= 15 media
  if len(media_objects) >= 15:
    for item in media_objects[0:15]:
      response = session.get(settings.fb_endpoint + item, params=params)
      data = response.json()
      if response.ok:
        try:
          if data['like_count'] < 10:
            continue
          # List Like and Media ID
          raw_list.append(data['like_count'])
          id_list.append(item)
          # List Media url
          if 'media_url' in data:
            media_srcs.append(data['media_url'])
        except KeyError:
          continue
  # shouter have media < 15 media
  else:
    for item in media_objects[0:len(media_objects)]:
      response = session.get(settings.fb_endpoint + item, params=params)
      if response.ok:
        data = response.json()
        try:
          if data['like_count'] < 10:
            continue
          # List Like and Media ID
          raw_list.append(data['like_count'])
          id_list.append(item)
          # List Media url
          if 'media_url' in data:
            media_srcs.append(data['media_url'])
        except KeyError:
          continue
  
  context = fn_engagement_outlier.cut(raw_list, id_list)
  # Return with context = {
  #   'final_dict': final_dict,
  #   'ig_average_total_like': ig_average_total_like,
  # }
  # final_dict = [{id: like_count}, ... ]
  context['media_srcs'] = media_srcs
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
    except KeyError:
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


