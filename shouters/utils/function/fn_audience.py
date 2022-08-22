# shell
# from shouters.utils.function import fn_audience
# gender_objects = data['data'][2]['values'][0]['value']
# gender = fn_audience.get_gender(gender_objects)
# age_objects = data['data'][2]['values'][0]['value']
# age = fn_audience.get_age(age_objects)
# location_objects = data['data'][0]['values'][0]['value']
# location = fn_audience.get_location(location_objects)

def get_gender(gender_objects):
  female = 0
  male = 0
  undefined = 0
  total = 0
  for key, value in gender_objects.items():
    if 'F' in key:
      female += value
      total += value
    elif 'M' in key:
      male += value
      total += value
    else:
      undefined += value
      total += value

  # if total != 0:
  context = {
    'male': round((male / total) * 100, 2),
    'female': round((female / total) * 100, 2),
    'undefined': round((undefined / total) * 100, 2),
  }
  return context
  # else:
  #   context = {
  #     'male': round((male / 1) * 100, 2),
  #     'female': round((female / 1) * 100, 2),
  #     'undefined': round((undefined / 1) * 100, 2),
  #   }
  #   return context


def get_age(age_objects):
  age_13_17 = 0
  age_18_24 = 0
  age_25_34 = 0
  age_35_44 = 0
  age_45_54 = 0
  age_55_64 = 0
  total = 0
  for key, value in age_objects.items():
    if '13' in key:
      age_13_17 += value
      total += value
    elif '18' in key:
      age_18_24 += value
      total += value
    elif '25' in key:
      age_25_34 += value
      total += value
    elif '35' in key:
      age_35_44 += value
      total += value
    elif '45' in key:
      age_45_54 += value
      total += value
    else:
      age_55_64 += value
      total += value

  context = {
    'age_13_17': round((age_13_17 / total) * 100, 2),
    'age_18_24': round((age_18_24 / total) * 100, 2),
    'age_25_34': round((age_25_34 / total) * 100, 2),
    'age_35_44': round((age_35_44 / total) * 100, 2),
    'age_45_54': round((age_45_54 / total) * 100, 2),
    'age_55_64': round((age_55_64 / total) * 100, 2),
  }
  return context


def get_location(location_objects):
  total = sum([value for key, value in location_objects.items()])
  location_1 = max(location_objects, key=location_objects.get)
  location_1_percent = round((location_objects[location_1] / total) * 100, 2)
  location_objects.pop(location_1, None)
  location_2 = max(location_objects, key=location_objects.get)
  location_2_percent = round((location_objects[location_2] / total) * 100, 2)
  context = {
    "location_1": {location_1: location_1_percent},
    "location_2": {location_2: location_2_percent},
  }
  return context


def save(gender, age, location, shouter):
  # gender
  shouter.ig_audience_male_percent = gender['male']
  shouter.ig_audience_female_percent = gender['female']
  shouter.ig_audience_undefined_percent = gender['undefined']

  # age
  shouter.ig_age_range_13_17 = age['age_13_17']
  shouter.ig_age_range_18_24 = age['age_18_24']
  shouter.ig_age_range_25_34 = age['age_25_34']
  shouter.ig_age_range_35_44 = age['age_35_44']
  shouter.ig_age_range_45_54 = age['age_45_54']
  shouter.ig_age_range_55_64 = age['age_55_64']

  # location
  shouter.ig_audience_location_1 = list(location['location_1'].keys())[0]
  shouter.ig_audience_location_1_percent = list(location['location_1'].values())[0]
  shouter.ig_audience_location_2 = list(location['location_2'].keys())[0]
  shouter.ig_audience_location_2_percent = list(location['location_2'].values())[0]

  shouter.save()


def get(data, shouter):
  # gender
  try:
    gender_objects = data['data'][2]['values'][0]['value']
    gender = get_gender(gender_objects)  # {'male': 29.02, 'female': 53.47, 'undefined': 17.51}
  except KeyError:
    return False

  # age
  try:
    age_objects = data['data'][2]['values'][0]['value']
    age = get_age(age_objects)  # {'age_13_17': 0.93, 'age_18_24': 64.18, 'age_25_34': 28.95, 'age_35_44': 3.37, 'age_45_54': 1.39, 'age_55_64': 1.19}
  except KeyError:
    return False

  # location
  try:
    location_objects = data['data'][0]['values'][0]['value']
    location = get_location(location_objects)  # {'location_1': {'Bangkok, Bangkok': 57.55}, 'location_2': {'Hat Yai, Songkhla': 22.34}}
  except KeyError:
    return False

  save(gender, age, location, shouter)
  return True
