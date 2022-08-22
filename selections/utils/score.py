# Sample Insight Data
data = {"data":
         [
           {"id": "17841400619453016/insights/audience_city/lifetime", "name": "audience_city", "title": "เมืองกลุ่มเป้าหมาย", "period": "lifetime",
           "values": [{"value": {"Seoul, Seoul": 4, "Trang, Trang": 4, "Phuket, Phuket": 6, "Ban Phru, Satun": 10, "Sadao, Songkhla": 4,
                                 "Bangkok, Bangkok": 724, "Pattani, Pattani": 3, "Toronto, Ontario": 3, "Hat Yai, Songkhla": 281, "Kau Teo, Songkhla": 4,
                                 "Songkhla, Songkhla": 33, "Melbourne, Victoria": 3, "Yala, Yala Province": 4, "Ayutthaya, Ayutthaya": 5,
                                 "Chon Buri, Chon Buri": 4, "Khon Kaen, Khon Kaen": 5, "Ocean City, Maryland": 3, "Bang Bo, Samut Prakan": 4,
                                 "Rangsit, Pathum Thani": 5, "Amphoe Chana, Songkhla": 3, "Amphoe Sadao, Songkhla": 8, "Amphoe Thalang, Phuket": 5,
                                 "Ban Khuan So, Songkhla": 3, "Chiang Mai, Chiang Mai": 10, "Lake Delton, Wisconsin": 5, "Nonthaburi, Nonthaburi": 20,
                                 "Udon Thani, Udon Thani": 3, "Williamsburg, Virginia": 3, "Ban Tha Chang, Songkhla": 4, "Bang Phun, Pathum Thani": 4,
                                 "Sydney, New South Wales": 9, "Ban Bang Riang, Songkhla": 3, "Ban Nang Lae, Chiang Rai": 3,
                                 "Phitsanulok, Phitsanulok": 3, "Surat Thani, Surat Thani": 4, "Kam Phaeng Phet, Songkhla": 4,
                                 "Amphoe Rattaphum, Songkhla": 3, "Ban Tha Kham (1), Songkhla": 13, "Amphoe Ban Pong, Ratchaburi": 3,
                                 "Changwat Songkhla, Songkhla": 4, "South Lake Tahoe, California": 5, "Ubon Ratchathani, Ubon Ratchathani": 3,
                                 "Changwat Samut Prakan, Samut Prakan": 17, "Ban Khlong Maha Sawat, Nakhon Pathom": 3,
                                 "Nakhon Si Thammarat, Nakhon Si Thammarat": 4}, "end_time": "2022-07-25T07:00:00+0000"}],
           "description": "เมืองของผู้ติดตามโปรไฟล์นี้"},
          {"id": "17841400619453016/insights/audience_country/lifetime", "name": "audience_country", "title": "ประเทศกลุ่มเป้าหมาย", "period": "lifetime",
           "values": [{"value": {"AU": 13, "BE": 1, "BN": 1, "CA": 3, "CH": 1, "CN": 1, "CZ": 1, "DE": 2, "DZ": 1, "ES": 1, "FR": 1, "GB": 4, "HK": 1,
                                 "HR": 1, "ID": 2, "IN": 4, "IQ": 1, "JP": 1, "KH": 2, "KR": 4, "MY": 3, "NG": 2, "NO": 1, "PE": 1, "PH": 4, "PL": 2,
                                 "RU": 2, "SA": 2, "SG": 2, "TH": 1383, "TR": 4, "TW": 1, "TZ": 2, "US": 55, "VE": 1, "VN": 2},
                       "end_time": "2022-07-25T07:00:00+0000"}],
           "description": "ประเทศของผู้ติดตามโปรไฟล์นี้"},
          {"id": "17841400619453016/insights/audience_gender_age/lifetime", "name": "audience_gender_age", "title": "เพศและอายุ", "period": "lifetime",
           "values": [{"value": {"F.65+": 5, "M.65+": 1, "U.65+": 2, "F.13-17": 5, "F.18-24": 545, "F.25-34": 216, "F.35-44": 21, "F.45-54": 12,
                                 "F.55-64": 5, "M.13-17": 2, "M.18-24": 263, "M.25-34": 145, "M.35-44": 17, "M.45-54": 9, "M.55-64": 2, "U.13-17": 7,
                                 "U.18-24": 163, "U.25-34": 77, "U.35-44": 13, "U.55-64": 3}, "end_time": "2022-07-25T07:00:00+0000"}],
           "description": "การแบ่งประเภทเพศและอายุของผู้ติดตามโปรไฟล์นี้"},
          {"id": "17841400619453016/insights/audience_locale/lifetime", "name": "audience_locale", "title": "ตำแหน่ง", "period": "lifetime",
           "values": [{"value": {"ar_AE": 1,"de_DE": 2,"en_GB": 52,"en_TH": 1,"en_US": 786,"es_ES": 1,"es_LA": 1,"fr_FR": 2,"ja_JP": 1,"ko_KR": 1,"ru_RU": 2,
                                 "th_TH": 659,"tr_TR": 2,"vi_VN": 1,"zh_HK": 1},"end_time": "2022-07-25T07:00:00+0000"}],
           "description": "ตำแหน่งที่ตั้งตามรหัสประเทศของผู้ติดตามโปรไฟล์นี้"},
          {"id": "17841400619453016/insights/online_followers/lifetime", "name": "online_followers", "title": "ผู้ติดตามออนไลน์", "period": "lifetime",
           "values": [{"value": {}, "end_time": "2022-07-25T07:00:00+0000"}],
           "description": "จำนวนทั้งหมดของผู้ติดตามโปรไฟล์นี้ที่ออนไลน์ในช่วงเวลาที่กำหนด"}
          ]
       }

# Calculate Interest Function (30%)
def cal_interest(campaign_interests: list, shouter_interests: list):
  score = 0
  # cal
  for interest in shouter_interests:
    if interest in campaign_interests:
      score += 10
  return score


# Calculate Gender & Age Function (25%)
# หาจาก shouter insight ว่าคนตามอายุเท่าไร คนตามอยู่ประมาณไหน ...
# gender มี 3 อย่างคือ male, female, all
# age รับค่าเป็นช่วง
def cal_gender(campaign_gender: str, campaign_age: list, shouter_insight: object) -> int:
  score = 0
  # cal
  if campaign_gender == "all":
    # Find age cal

  else:

  return score


# Calculate Location Function (15%)
# location รับค่าเป็น string
def cal_location_score(campaign_location: str, shouter_insight: object) -> int:
  score = 0
  # cal
  return score


# Calculate Active Follower Function (30%)
def cal_active_follower(shouter_active_follower):
  return shouter_active_follower * 0.3


# Calculate Total Score Function
def cal(campaign, shouter):

  # Cal interest score
  campaign_interests = campaign.campaign_interest
  shouter_interests = shouter.interest
  interest_score = cal_interest(campaign_interests, shouter_interests)  # PASS

  # Cal gender and age score
  campaign_gender = campaign.campaign_gender
  campaign_age = campaign.campaign_age
  shouter_insight = shouter.ig_response_audience_insight
  gender_age_score = cal_gender(campaign_gender, campaign_age, shouter_insight)

  # Cal location score
  campaign_location = campaign.campaign_province
  location_score = cal_location_score(campaign_location, shouter_insight)

  # Cal active follower score
  active_follower_score = cal_active_follower(shouter.ig_active_follower_percent) # PASS

  # return Total score
  return interest_score + gender_age_score + location_score + active_follower_score
