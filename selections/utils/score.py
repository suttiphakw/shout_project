# # Sample Insight Data
# data = {"data":
#          [
#            {"id": "17841400619453016/insights/audience_city/lifetime", "name": "audience_city", "title": "เมืองกลุ่มเป้าหมาย", "period": "lifetime",
#            "values": [{"value": {"Seoul, Seoul": 4, "Trang, Trang": 4, "Phuket, Phuket": 6, "Ban Phru, Satun": 10, "Sadao, Songkhla": 4,
#                                  "Bangkok, Bangkok": 724, "Pattani, Pattani": 3, "Toronto, Ontario": 3, "Hat Yai, Songkhla": 281, "Kau Teo, Songkhla": 4,
#                                  "Songkhla, Songkhla": 33, "Melbourne, Victoria": 3, "Yala, Yala Province": 4, "Ayutthaya, Ayutthaya": 5,
#                                  "Chon Buri, Chon Buri": 4, "Khon Kaen, Khon Kaen": 5, "Ocean City, Maryland": 3, "Bang Bo, Samut Prakan": 4,
#                                  "Rangsit, Pathum Thani": 5, "Amphoe Chana, Songkhla": 3, "Amphoe Sadao, Songkhla": 8, "Amphoe Thalang, Phuket": 5,
#                                  "Ban Khuan So, Songkhla": 3, "Chiang Mai, Chiang Mai": 10, "Lake Delton, Wisconsin": 5, "Nonthaburi, Nonthaburi": 20,
#                                  "Udon Thani, Udon Thani": 3, "Williamsburg, Virginia": 3, "Ban Tha Chang, Songkhla": 4, "Bang Phun, Pathum Thani": 4,
#                                  "Sydney, New South Wales": 9, "Ban Bang Riang, Songkhla": 3, "Ban Nang Lae, Chiang Rai": 3,
#                                  "Phitsanulok, Phitsanulok": 3, "Surat Thani, Surat Thani": 4, "Kam Phaeng Phet, Songkhla": 4,
#                                  "Amphoe Rattaphum, Songkhla": 3, "Ban Tha Kham (1), Songkhla": 13, "Amphoe Ban Pong, Ratchaburi": 3,
#                                  "Changwat Songkhla, Songkhla": 4, "South Lake Tahoe, California": 5, "Ubon Ratchathani, Ubon Ratchathani": 3,
#                                  "Changwat Samut Prakan, Samut Prakan": 17, "Ban Khlong Maha Sawat, Nakhon Pathom": 3,
#                                  "Nakhon Si Thammarat, Nakhon Si Thammarat": 4}, "end_time": "2022-07-25T07:00:00+0000"}],
#            "description": "เมืองของผู้ติดตามโปรไฟล์นี้"},
#           {"id": "17841400619453016/insights/audience_country/lifetime", "name": "audience_country", "title": "ประเทศกลุ่มเป้าหมาย", "period": "lifetime",
#            "values": [{"value": {"AU": 13, "BE": 1, "BN": 1, "CA": 3, "CH": 1, "CN": 1, "CZ": 1, "DE": 2, "DZ": 1, "ES": 1, "FR": 1, "GB": 4, "HK": 1,
#                                  "HR": 1, "ID": 2, "IN": 4, "IQ": 1, "JP": 1, "KH": 2, "KR": 4, "MY": 3, "NG": 2, "NO": 1, "PE": 1, "PH": 4, "PL": 2,
#                                  "RU": 2, "SA": 2, "SG": 2, "TH": 1383, "TR": 4, "TW": 1, "TZ": 2, "US": 55, "VE": 1, "VN": 2},
#                        "end_time": "2022-07-25T07:00:00+0000"}],
#            "description": "ประเทศของผู้ติดตามโปรไฟล์นี้"},
#           {"id": "17841400619453016/insights/audience_gender_age/lifetime", "name": "audience_gender_age", "title": "เพศและอายุ", "period": "lifetime",
#            "values": [{"value": {"F.65+": 5, "M.65+": 1, "U.65+": 2, "F.13-17": 5, "F.18-24": 545, "F.25-34": 216, "F.35-44": 21, "F.45-54": 12,
#                                  "F.55-64": 5, "M.13-17": 2, "M.18-24": 263, "M.25-34": 145, "M.35-44": 17, "M.45-54": 9, "M.55-64": 2, "U.13-17": 7,
#                                  "U.18-24": 163, "U.25-34": 77, "U.35-44": 13, "U.55-64": 3}, "end_time": "2022-07-25T07:00:00+0000"}],
#            "description": "การแบ่งประเภทเพศและอายุของผู้ติดตามโปรไฟล์นี้"},
#           {"id": "17841400619453016/insights/audience_locale/lifetime", "name": "audience_locale", "title": "ตำแหน่ง", "period": "lifetime",
#            "values": [{"value": {"ar_AE": 1,"de_DE": 2,"en_GB": 52,"en_TH": 1,"en_US": 786,"es_ES": 1,"es_LA": 1,"fr_FR": 2,"ja_JP": 1,"ko_KR": 1,"ru_RU": 2,
#                                  "th_TH": 659,"tr_TR": 2,"vi_VN": 1,"zh_HK": 1},"end_time": "2022-07-25T07:00:00+0000"}],
#            "description": "ตำแหน่งที่ตั้งตามรหัสประเทศของผู้ติดตามโปรไฟล์นี้"},
#           {"id": "17841400619453016/insights/online_followers/lifetime", "name": "online_followers", "title": "ผู้ติดตามออนไลน์", "period": "lifetime",
#            "values": [{"value": {}, "end_time": "2022-07-25T07:00:00+0000"}],
#            "description": "จำนวนทั้งหมดของผู้ติดตามโปรไฟล์นี้ที่ออนไลน์ในช่วงเวลาที่กำหนด"}
#           ]
#        }

# Calculate Interest Function (30%)
def cal_interest_score(campaign_interests: list, shouter_interests: list):
  score = 0
  # cal
  for interest in shouter_interests:
    if interest in campaign_interests:
      score += 10
  return score


# Calculate Gender Function (15%)
# gender มี 3 อย่างคือ male, female, all
def cal_gender_score(campaign_gender, shouter_male, shouter_female):
  score = 0
  # cal
  if campaign_gender == "all":
    # Find age cal
    score += 15
  elif campaign_gender == "male":
    score += shouter_male * 0.15
  elif campaign_gender == "female":
    score += shouter_female * 0.15
  return score


# Calculate Age Function (15%)
# age มี 6 ช่วง
def cal_age_score(campaign_age, shouter_age):
  score = 0
  # cal
  if 'all_age' in campaign_age:
    score += 15
  else:
    for key, value in shouter_age.items():
      if key in campaign_age:
        score += value * 0.15
  return score


# Calculate Location Function (15%)
# location รับค่าเป็น string
def cal_location_score(campaign_location, shouter_location_1, shouter_location_1_percent, shouter_location_2, shouter_location_2_percent):
  score = 0
  # cal
  if campaign_location == 'all_province':
    score += 15
  # bangkok
  else:
    if 'bangkok' in shouter_location_1.lower():
      score += shouter_location_1_percent * 0.15
    elif 'bangkok' in shouter_location_2.lower():
      score += shouter_location_2_percent * 0.15
  return score


# Calculate Active Follower Function (25%)
def cal_active_follower_score(shouter_active_follower):
  return shouter_active_follower * 0.3


# Calculate Total Score Function
def cal(campaign, shouter):

  # Cal interest score
  campaign_interests = campaign.campaign_interest
  shouter_interests = shouter.interest
  interest_score = cal_interest_score(campaign_interests, shouter_interests)  # PASS

  # Cal gender score
  campaign_gender = campaign.campaign_gender
  shouter_male = shouter.ig_audience_male_percent
  shouter_female = shouter.ig_audience_female_percent
  gender_score = cal_gender_score(campaign_gender, shouter_male, shouter_female)  # PASS

  # Cal age score
  campaign_age = campaign.campaign_age
  shouter_age = {
    "13_17": shouter.ig_age_range_13_17,
    "18_24": shouter.ig_age_range_18_24,
    "25_34": shouter.ig_age_range_25_34,
    "35_44": shouter.ig_age_range_35_44,
    "45_54": shouter.ig_age_range_45_54,
    "55_64": shouter.ig_age_range_55_64,
  }
  age_score = cal_age_score(campaign_age, shouter_age)  # PASS

  # Cal location score
  campaign_location = campaign.campaign_province
  shouter_location_1 = shouter.ig_audience_location_1
  shouter_location_1_percent = shouter.ig_audience_location_1_percent
  shouter_location_2 = shouter.ig_audience_location_2
  shouter_location_2_percent = shouter.ig_audience_location_2_percent

  location_score = cal_location_score(campaign_location, shouter_location_1, shouter_location_1_percent, shouter_location_2, shouter_location_2_percent)

  # Cal active follower score
  active_follower_score = cal_active_follower_score(shouter.ig_active_follower_percent)  # PASS

  # return Total score
  return interest_score + gender_score + age_score + location_score + active_follower_score
