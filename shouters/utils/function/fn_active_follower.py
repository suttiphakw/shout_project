import statistics

from . import fn_geo_mean_overflow

def get(data, followers_count):
  my_list = []
  my_list_2 = []
  try:
    for value in data['data'][0]['values']:
      mean_1 = sum([value['value']['0'], value['value']['1'], value['value']['2']])
      mean_2 = sum([value['value']['3'], value['value']['4'], value['value']['5']])
      mean_3 = sum([value['value']['6'], value['value']['7'], value['value']['8']])
      mean_4 = sum([value['value']['9'], value['value']['10'], value['value']['11']])
      mean_5 = sum([value['value']['12'], value['value']['13'], value['value']['14']])
      mean_6 = sum([value['value']['15'], value['value']['16'], value['value']['17']])
      mean_7 = sum([value['value']['18'], value['value']['19'], value['value']['20']])
      mean_8 = sum([value['value']['21'], value['value']['22'], value['value']['23']])
      avg = fn_geo_mean_overflow.cal([mean_1, mean_2, mean_3, mean_4, mean_5, mean_6, mean_7, mean_8])
      avg_2 = statistics.harmonic_mean([mean_1, mean_2, mean_3, mean_4, mean_5, mean_6, mean_7, mean_8])
      my_list.append(avg)
      my_list_2.append(avg_2)
    geometric_active_follower = statistics.mean(my_list)
    harmonic_active_follower = statistics.mean(my_list_2)
  except:
    predicted_active_followers = 0.65 * followers_count
    geometric_active_follower = predicted_active_followers
    harmonic_active_follower = predicted_active_followers

  ig_active_follower_percent = (geometric_active_follower / followers_count) * 100
  ig_active_follower_percent = round(ig_active_follower_percent, 2)

  context = {
    'data': data,
    'geometric_active_follower': geometric_active_follower,
    'harmonic_active_follower': harmonic_active_follower,
    'ig_active_follower_percent': ig_active_follower_percent
  }

  return context