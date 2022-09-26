import requests

# from shouters.temp import FacebookAPI
# Import Own Utils
from .utils.function import fn_ad_gaurantee_reach, fn_round_to_five
from .utils.facebook import fb_api_bio, fb_api_permissions
from .utils.instagram import ig_api_engagement, ig_api_active_follower, ig_api_bio, ig_api_media_objects, ig_api_audience_insight
from .utils.predicted import predicted_post_reach, predicted_story_view
from .utils.pricing.calculate_price import IGStoryFc, IGStoryUgc, IGPostFc, IGPostUgc
from .utils.function import fn_audience


def refresh_shouters(access_token, business_account_id):
  """ For refreshing shouter data by instagram api """
  # Check If Access Token Failed / Expired
  # Get Permissions
  permissions  = fb_api_permissions.get(access_token)
  if not permissions:
    # Return To Recheck Permission
    return False
  if len(permissions['permissions']) < 5:
    # Return prompt in admin session
    return False
  # Get Facebook Biography
  context__fb_biography = fb_api_bio.get(access_token)
  if not context__fb_biography:
    return False
  try:
    fb_name = context__fb_biography['fb_name']
    fb_profile_picture = context__fb_biography['fb_profile_picture']
  except ValueError:
    fb_name = fb_profile_picture = None

  # Get Instagram Biography
  context__ig_biography = ig_api_bio.get(business_account_id, access_token)
  if not context__ig_biography:
    return False
  try:
    ig_username = context__ig_biography['username']
    ig_media_count = context__ig_biography['media_count']
    ig_follower_count = context__ig_biography['followers_count']
    ig_following_count = context__ig_biography['followings_count']
    ig_profile_picture = context__ig_biography['ig_profile_picture']
  except:
    ig_username = ig_media_count = ig_follower_count = ig_following_count = ig_profile_picture = None

  ##########################################################################################################################
  # Get Instagram Active Follower
  context__active_follower = ig_api_active_follower.get(business_account_id=business_account_id, access_token=access_token, followers_count=ig_follower_count)
  if not context__active_follower:
    return False
  try:
    ig_response_active_follower = context__active_follower['data']
    ig_active_follower = context__active_follower['geometric_active_follower']
    ig_active_follower_harmonic = context__active_follower['harmonic_active_follower']
    ig_active_follower_percent = context__active_follower['ig_active_follower_percent']
  except:
    ig_response_active_follower = ig_active_follower = ig_active_follower_harmonic = ig_active_follower_percent = None
  ##########################################################################################################################

  ##########################################################################################################################
  # Get Media Objects => Return ค่าออกมา 3 อย่าง คือ ig_average_total_like, ig_story_view, ig_average_post_reach
  context__media_objects = ig_api_media_objects.get(business_account_id=business_account_id, access_token=access_token)
  try:
    ig_response_media_objects = context__media_objects['data']
    media_objects = context__media_objects['media_objects']
  except:
    ig_response_media_objects = {}
    media_objects = []
  if not context__media_objects or len(media_objects) == 0:
    ig_average_total_like = 0
    ig_story_view = 0
    ig_average_post_reach = 0
    ig_reach_source = 'no media'
  else:
    # context__like_engagement return เป็น dict => dict['list_like'] = list และ dict['mean'] = average like after cut outlier
    context__like_engagement = ig_api_engagement.get_like(media_objects=media_objects, access_token=access_token)
    # return =>
    # {
    #   'final_dict': [{id: like_count}, ... ],
    #   'ig_average_total_like' : ...
    # }
    # if no final dict => context__like_engagement return False
    if not context__like_engagement:
      ig_average_total_like = 0
      ig_story_view = 0
      ig_average_post_reach = 0
      ig_reach_source = 'all media like < 10'
    else:
      # AVERAGE LIKE & STORY VIEW
      final_dict = context__like_engagement['final_dict']
      ig_average_total_like = context__like_engagement['ig_average_total_like']
      ig_story_view = predicted_story_view.get(ig_follower_count=ig_follower_count, ig_average_total_like=ig_average_total_like)

      # เก็บ POST REACH เพื่อดูว่าเก็บไก้มากกว่า 3 ไหม
      context__post_reach = ig_api_engagement.get_reach(final_dict=final_dict, access_token=access_token)
      if 'ig_average_post_reach' in context__post_reach.keys():
        reach_list = context__post_reach['reach_list']
        # Media < 3 -> like = average, story_view = 0, post_reach = 0
        if len(media_objects) < 3 or len(reach_list) < 3:
          ig_average_post_reach = predicted_post_reach.get(ig_average_total_like=ig_average_total_like, ig_story_view=ig_story_view)
          ig_reach_source = 'predicted'
        else:
          # AVERAGE POST REACH
          ig_average_post_reach = context__post_reach['ig_average_post_reach']
          ig_reach_source = 'api'
      else:
        ig_average_post_reach = predicted_post_reach.get(ig_average_total_like=ig_average_total_like, ig_story_view=ig_story_view)
        ig_reach_source = 'predicted'
  ##########################################################################################################################

  ##########################################################################################################################
  # ANALYSIS => Return ค่า Engagement โดยการนำค่า 3 ค่าที่ได้จากก่อนหน้ามาคำนวน
  ig_engagement_percent = (ig_average_total_like / ig_follower_count) * 100
  ig_engagement_percent = round(ig_engagement_percent, 2)

  # Cal AD and Guarantee Reach
  context__ad_gaurantee = fn_ad_gaurantee_reach.get(ig_story_view=ig_story_view,ig_average_post_reach=ig_average_post_reach)
  ig_predicted_ad_post_reach = context__ad_gaurantee['ig_predicted_ad_post_reach']
  ig_post_reach_guarantee = context__ad_gaurantee['ig_post_reach_guarantee']
  ig_story_view_guarantee = context__ad_gaurantee['ig_story_view_guarantee']
  ig_ad_post_reach = context__ad_gaurantee['ig_ad_post_reach']

  # Cal Price
  # instagram story + post
  ig_price_story_fc = fn_round_to_five.get(IGStoryFc().cal_price(ig_story_view))
  ig_price_story_ugc = fn_round_to_five.get(IGStoryUgc().cal_price(ig_story_view))
  ig_price_post_fc = fn_round_to_five.get(IGPostFc().cal_price(ig_ad_post_reach))
  ig_price_post_ugc = fn_round_to_five.get(IGPostUgc().cal_price(ig_ad_post_reach))
  ig_price_story_post_fc = (ig_price_story_fc + ig_price_post_fc) * 0.9
  ig_price_story_post_ugc = (ig_price_story_ugc + ig_price_post_ugc) * 0.9
  ig_price_story_post_fc = fn_round_to_five.get(ig_price_story_post_fc)
  ig_price_story_post_ugc = fn_round_to_five.get(ig_price_story_post_ugc)
  # facebook story + post
  ig_fb_price_story_fc = fn_round_to_five.get(ig_price_story_fc * 1.1)
  ig_fb_price_story_ugc = fn_round_to_five.get(ig_price_story_ugc * 1.1)
  ig_fb_price_post_fc = fn_round_to_five.get(ig_price_post_fc * 1.1)
  ig_fb_price_post_ugc = fn_round_to_five.get(ig_price_post_ugc * 1.1)
  ig_fb_price_story_post_fc = fn_round_to_five.get(ig_price_story_post_fc * 1.1)
  ig_fb_price_story_post_ugc = fn_round_to_five.get(ig_price_story_post_ugc * 1.1)
  ##########################################################################################################################

  ##########################################################################################################################
  # IG INSIGHT
  data = ig_api_audience_insight.get(business_account_id=business_account_id, access_token=access_token)
  ig_response_audience_insight = data
  if data and data['data'] != []:
    if data['data'][0]['values'][0]['value'] and data['data'][2]['values'][0]['value']:
      gender, age, location = fn_audience.get_refresh(data)
      ig_audience_male_percent = gender['male']
      ig_audience_female_percent = gender['female']
      ig_audience_undefined_percent = gender['undefined']

      # age
      ig_age_range_13_17 = age['age_13_17']
      ig_age_range_18_24 = age['age_18_24']
      ig_age_range_25_34 = age['age_25_34']
      ig_age_range_35_44 = age['age_35_44']
      ig_age_range_45_54 = age['age_45_54']
      ig_age_range_55_64 = age['age_55_64']

      # location
      ig_audience_location_1 = list(location['location_1'].keys())[0]
      ig_audience_location_1_percent = list(location['location_1'].values())[0]
      ig_audience_location_2 = list(location['location_2'].keys())[0]
      ig_audience_location_2_percent = list(location['location_2'].values())[0]
    else:
      ig_audience_male_percent = ig_audience_female_percent = ig_audience_undefined_percent = None
      ig_age_range_13_17 = ig_age_range_18_24 = ig_age_range_25_34 = ig_age_range_35_44 = ig_age_range_45_54 = ig_age_range_55_64 = None
      ig_audience_location_1 = ig_audience_location_1_percent = ig_audience_location_2 = ig_audience_location_2_percent = None
  else:
    ig_audience_male_percent = ig_audience_female_percent = ig_audience_undefined_percent = None
    ig_age_range_13_17 = ig_age_range_18_24 = ig_age_range_25_34 = ig_age_range_35_44 = ig_age_range_45_54 = ig_age_range_55_64 = None
    ig_audience_location_1 = ig_audience_location_1_percent = ig_audience_location_2 = ig_audience_location_2_percent = None
  ##########################################################################################################################

  response = {
    ##########################################################################################################################
    # Facebook
    "fb_name": fb_name,
    "fb_profile_picture": fb_profile_picture,
    ##########################################################################################################################
    # IG Biography
    "ig_username": ig_username,
    "ig_media_count": ig_media_count,
    "ig_follower_count": ig_follower_count,
    "ig_following_count": ig_following_count,
    "ig_profile_picture": ig_profile_picture,
    ##########################################################################################################################
    # IG Active Follower
    "ig_response_active_follower": ig_response_active_follower,
    "ig_active_follower": ig_active_follower,
    "ig_active_follower_harmonic": ig_active_follower_harmonic,
    "ig_active_follower_percent": ig_active_follower_percent,
    ##########################################################################################################################
    # Media Objects
    "ig_response_media_objects": ig_response_media_objects,
    ##########################################################################################################################
    # Engagement => จาก Media Objects
    "ig_average_total_like": ig_average_total_like,
    "ig_story_view": ig_story_view,
    "ig_average_post_reach": ig_average_post_reach,
    "ig_reach_source": ig_reach_source,
    ##########################################################################################################################
    # Engagement => จากการคำนวน
    "ig_engagement_percent": ig_engagement_percent,
    "ig_predicted_ad_post_reach": ig_predicted_ad_post_reach,
    "ig_post_reach_guarantee": ig_post_reach_guarantee,
    "ig_story_view_guarantee": ig_story_view_guarantee,
    "ig_ad_post_reach": ig_ad_post_reach,
    ##########################################################################################################################
    # Price
    "ig_price_story_fc": ig_price_story_fc,
    "ig_price_story_ugc": ig_price_story_ugc,
    "ig_price_post_fc": ig_price_post_fc,
    "ig_price_post_ugc": ig_price_post_ugc,
    "ig_price_story_post_fc": ig_price_story_post_fc,
    "ig_price_story_post_ugc": ig_price_story_post_ugc,
    "ig_fb_price_story_fc": ig_fb_price_story_fc,
    "ig_fb_price_story_ugc": ig_fb_price_story_ugc,
    "ig_fb_price_post_fc": ig_fb_price_post_fc,
    "ig_fb_price_post_ugc": ig_fb_price_post_ugc,
    "ig_fb_price_story_post_fc": ig_fb_price_story_post_fc,
    "ig_fb_price_story_post_ugc": ig_fb_price_story_post_ugc,
    ##########################################################################################################################
    # Audience Insight
    "ig_response_audience_insight": ig_response_audience_insight,
    "ig_audience_male_percent": ig_audience_male_percent,
    "ig_audience_female_percent": ig_audience_female_percent,
    "ig_audience_undefined_percent": ig_audience_undefined_percent,
    "ig_age_range_13_17": ig_age_range_13_17,
    "ig_age_range_18_24": ig_age_range_18_24,
    "ig_age_range_25_34": ig_age_range_25_34,
    "ig_age_range_35_44": ig_age_range_35_44,
    "ig_age_range_45_54": ig_age_range_45_54,
    "ig_age_range_55_64": ig_age_range_55_64,
    "ig_audience_location_1": ig_audience_location_1,
    "ig_audience_location_1_percent": ig_audience_location_1_percent,
    "ig_audience_location_2": ig_audience_location_2,
    "ig_audience_location_2_percent": ig_audience_location_2_percent
    ##########################################################################################################################
  }
  # print(response)
  return response
