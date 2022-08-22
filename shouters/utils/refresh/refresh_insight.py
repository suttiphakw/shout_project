from shouters.models import Shouter
from shouters.utils.function import fn_audience

pass_shouter = []
type_list_shouter = []
no_data_shouter = []
fail_shouter = []
shouters = Shouter.objects.filter(is_approve=True)

for shouter in shouters:
  current_shouter = shouter.ig_username
  data = shouter.ig_response_audience_insight
  if type(data) == list:
    type_list_shouter.append(shouter.ig_username)
    continue
  if not data or data['data'] == []:
    no_data_shouter.append(shouter.ig_username)
    continue
  if not data['data'][0]['values'][0]['value'] or not data['data'][2]['values'][0]['value']:
    no_data_shouter.append(shouter.ig_username)
    continue
  result = fn_audience.get(shouter.ig_response_audience_insight, shouter)
  if result:
    pass_shouter.append(shouter.ig_username)
  else:
    fail_shouter.append(shouter.ig_username)

