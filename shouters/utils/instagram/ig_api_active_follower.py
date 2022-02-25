import requests
import time

from shouters.utils import settings
from shouters.utils.function import fn_active_follower

def get(business_account_id, access_token, followers_count):
  unix_time = round(time.time())
  _9_days_before = unix_time - 9 * 86400
  _2_days_before = unix_time - 2 * 86400
  url = settings.fb_endpoint + business_account_id + '/insights'
  response = requests.get(url, params={'metric': 'online_followers',
                                       'period': 'lifetime',
                                       'access_token': access_token,
                                       'since': _9_days_before,
                                       'until': _2_days_before})

  if not response.ok:
    return False

  data = response.json()
  context = fn_active_follower.get(data, followers_count)
  return context
