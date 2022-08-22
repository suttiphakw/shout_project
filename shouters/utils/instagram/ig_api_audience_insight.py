import requests
from shouters.utils import settings

# @staticmethod
# def get_key_audience(json_data, position):
#     return json_data['data'][position]['name']
#
# @staticmethod
# def get_item_audience(json_data, position):
#     return json_data['data'][position]['values'][0]['value']
#
# @staticmethod
# def get_gender_count(item_audience_gender_age, gender):
#     return {k: v for k, v in item_audience_gender_age.items() if k[0] == gender}
#
# @staticmethod
# def get_age_count(item_audience_gender_age, age):
#     return {k: v for k, v in item_audience_gender_age.items() if k[2:4] == age}
#
# @staticmethod
# def get_percentage_audience(item_audience, max_total):
#     value = OrderedDict()
#     for k, v in sorted(item_audience.items(), key=lambda item: item[1], reverse=True):
#         value[k] = round(v * 100 / max_total, 1)
#     return value


def get(business_account_id, access_token):
  audience_scope = ['audience_city', 'audience_country', 'audience_gender_age', 'audience_locale', 'online_followers']
  params = {
    'metric': ','.join(audience_scope),
    'period': 'lifetime',
    'access_token': access_token
  }
  response = requests.get(settings.fb_endpoint + business_account_id + '/insights', params=params)
  if not response.ok:
    return False

  data = response.json()
  return data

    # # Get Data -> Audience City
    # key_audience_city = self.get_key_audience(data, 0)
    # item_audience_city = self.get_item_audience(data, 0)
    # total_audience_city = sum(item_audience_city.values())
    #
    # # Get Data -> Audience Country
    # key_audience_country = self.get_key_audience(data, 1)
    # item_audience_country = self.get_item_audience(data, 1)
    # total_audience_country = sum(item_audience_country.values())
    #
    # # Get Data -> Audience Gender in Age range
    # key_audience_gender_age = self.get_key_audience(data, 2)
    # item_audience_gender_age = self.get_item_audience(data, 2)
    # total_audience_gender_age = sum(item_audience_gender_age.values())
    #
    # # Calculate Max Total
    # max_total = max(total_audience_city, total_audience_country, total_audience_gender_age)
    #
    # # Get Data -> Only Male Gender
    # audience_male_gender = self.get_gender_count(item_audience_gender_age, 'M')
    # total_audience_male_gender = sum(audience_male_gender.values())
    #
    # # Get Data -> Only Female Gender
    # audience_female_gender = self.get_gender_count(item_audience_gender_age, 'F')
    # total_audience_female_gender = sum(audience_female_gender.values())
    #
    # # Get Data -> Only Undefined Gender
    # audience_undefined_gender = self.get_gender_count(item_audience_gender_age, 'U')
    # total_audience_undefined_gender = sum(audience_undefined_gender.values())
    #
    # # Get Data -> Age Range 13-17
    # audience_13_to_17_age = self.get_age_count(item_audience_gender_age, '13')
    # total_audience_13_to_17_age = sum(audience_13_to_17_age.values())
    #
    # # Get Data -> Age Range 18-24
    # audience_18_to_24_age = self.get_age_count(item_audience_gender_age, '18')
    # total_audience_18_to_24_age = sum(audience_18_to_24_age.values())
    #
    # # Get Data -> Age Range 25-34
    # audience_25_to_34_age = self.get_age_count(item_audience_gender_age, '25')
    # total_audience_25_to_34_age = sum(audience_25_to_34_age.values())
    #
    # # Get Data -> Age Range 35-44
    # audience_35_to_44_age = self.get_age_count(item_audience_gender_age, '35')
    # total_audience_35_to_44_age = sum(audience_35_to_44_age.values())
    #
    # # Get Data -> Age Range 45-54
    # audience_45_to_54_age = self.get_age_count(item_audience_gender_age, '45')
    # total_audience_45_to_54_age = sum(audience_45_to_54_age.values())
    #
    # # Get Data -> Age Range 55-64
    # audience_55_to_64_age = self.get_age_count(item_audience_gender_age, '55')
    # total_audience_55_to_64_age = sum(audience_55_to_64_age.values())
    #
    # # Get Data -> Age Range 65+
    # audience_65_up_age = self.get_age_count(item_audience_gender_age, '65')
    # total_audience_65_up_age = sum(audience_65_up_age.values())
    #
    # # Get Dict for see Ordered Audience_city
    # value_audience_city = self.get_percentage_audience(item_audience_city, max_total)
    # value_audience_country = self.get_percentage_audience(item_audience_country, max_total)
    # value_audience_gender_age = self.get_percentage_audience(item_audience_gender_age, max_total)
    #
    # two_most_common_city = {key_audience_city: list(value_audience_city.items())[:2]}
    # two_most_common_country = {key_audience_country: list(value_audience_country.items())[:2]}
    # two_most_common_gender_age = {key_audience_gender_age: list(value_audience_gender_age.items())[:2]}
    #
    # audience_male_percentage = round(
    #     total_audience_male_gender * 100 / (max_total - total_audience_undefined_gender), 1)
    # audience_female_percentage = round(
    #     total_audience_female_gender * 100 / (max_total - total_audience_undefined_gender), 1)
    # audience_age_13_17_percentage = round(total_audience_13_to_17_age * 100 / max_total, 1)
    # audience_age_18_24_percentage = round(total_audience_18_to_24_age * 100 / max_total, 1)
    # audience_age_25_34_percentage = round(total_audience_25_to_34_age * 100 / max_total, 1)
    # audience_age_35_44_percentage = round(total_audience_35_to_44_age * 100 / max_total, 1)
    # audience_age_45_54_percentage = round(total_audience_45_to_54_age * 100 / max_total, 1)
    # audience_age_55_64_percentage = round(total_audience_55_to_64_age * 100 / max_total, 1)
    # audience_age_65_up_percentage = round(total_audience_65_up_age * 100 / max_total, 1)
    #
    # context = {
    #     'insight': data,
    #     'max_total': max_total,
    #     'two_most_common_city': two_most_common_city,
    #     'two_most_common_country': two_most_common_country,
    #     'two_most_common_gender_age': two_most_common_gender_age,
    #     'audience_male_percentage': audience_male_percentage,
    #     'audience_female_percentage': audience_female_percentage,
    #     'audience_age_13_17_percentage': audience_age_13_17_percentage,
    #     'audience_age_18_24_percentage': audience_age_18_24_percentage,
    #     'audience_age_25_34_percentage': audience_age_25_34_percentage,
    #     'audience_age_35_44_percentage': audience_age_35_44_percentage,
    #     'audience_age_45_54_percentage': audience_age_45_54_percentage,
    #     'audience_age_55_64_percentage': audience_age_55_64_percentage,
    #     'audience_age_65_up_percentage': audience_age_65_up_percentage,
    # }
    #
    # return context