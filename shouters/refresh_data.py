import requests

from shouters.utils import FacebookAPI

from utils.cal_price import IGStoryFc, IGStoryUgc, IGPostFc, IGPostUgc


def round_to_five(x, base=5):
  return base * round(x / base)


def refresh_shouters(access_token, business_account_id):
  """ For refreshing shouter data by facebook api """
  # Get FB Name
  response_fb = requests.get('https://graph.facebook.com/v12.0/me', params={'access_token': access_token,
                                                                            'fields': 'name,picture'})
  if response_fb.ok:
    context__basic_fb = response_fb.json()
    fb_name = context__basic_fb['name']
    fb_profile_picture = context__basic_fb['picture']['data']['url']
  else:
    fb_name = fb_profile_picture = None

  # Get Bio
  context__ig_biography = FacebookAPI().get_ig_biography(business_account_id=business_account_id,
                                                         access_token=access_token)
  if context__ig_biography:
    ig_username = context__ig_biography.get('username')
    ig_media_count = context__ig_biography.get('media_count')
    ig_follower_count = context__ig_biography.get('followers')
    ig_following_count = context__ig_biography.get('followings')
    ig_profile_picture = context__ig_biography.get('profile_picture_url')
  else:
    ig_username = ig_media_count = ig_follower_count = ig_following_count = ig_profile_picture = None

  # Get Active Follower
  context__active_follower = FacebookAPI().get_active_follower(business_account_id=business_account_id,
                                                               access_token=access_token)
  if context__active_follower:
    ig_response_active_follower = context__active_follower.get('data')
    ig_active_follower = context__active_follower.get('geometric_active_follower')
    ig_active_follower_harmonic = context__active_follower.get('harmonic_active_follower')
    ig_active_follower_percent = (ig_active_follower / ig_follower_count) * 100
    ig_active_follower_percent = round(ig_active_follower_percent, 2)
  else:
    ig_response_active_follower = ig_active_follower = ig_active_follower_harmonic = ig_active_follower_percent = None

  # Get Media Objects
  context__media_objects = FacebookAPI().get_ig_media_objects(business_account_id=business_account_id,
                                                              access_token=access_token)
  if context__media_objects:
    ig_response_media_objects = context__media_objects.get('data')
    media_objects = context__media_objects.get('media_objects')
  else:
    ig_response_media_objects = None
    media_objects = None

  # Get Engagement
  if media_objects and ig_follower_count:
    context__engagement = FacebookAPI().get_engagement_insight(media_objects=media_objects,
                                                               access_token=access_token,
                                                               followers=ig_follower_count)
    if context__engagement:
      ig_average_total_like = context__engagement.get('average_total_like')
      ig_engagement_percent = (ig_average_total_like / ig_follower_count) * 100
      ig_engagement_percent = round(ig_engagement_percent, 2)
      ig_story_view = context__engagement.get('story_view')
      ig_average_post_reach = context__engagement.get('average_post_reach')

      # Cal Ads Post Reach
      ig_predicted_ad_post_reach = ig_story_view * 3
      if ig_average_post_reach < ig_predicted_ad_post_reach:
        ig_ad_post_reach = ig_average_post_reach
      else:
        ig_ad_post_reach = (ig_average_post_reach + ig_predicted_ad_post_reach) / 2

      # Cal Price IG
      ig_price_story_fc = round_to_five(IGStoryFc().cal_price(ig_story_view))
      ig_price_story_ugc = round_to_five(IGStoryUgc().cal_price(ig_story_view))
      ig_price_post_fc = round_to_five(IGPostFc().cal_price(ig_ad_post_reach))
      ig_price_post_ugc = round_to_five(IGPostUgc().cal_price(ig_ad_post_reach))
      ig_price_story_post_fc = round_to_five((ig_price_story_fc + ig_price_post_fc) * 0.9)
      ig_price_story_post_ugc = round_to_five((ig_price_story_ugc + ig_price_post_ugc) * 0.9)

      # Cal Price IG + FB
      ig_fb_price_story_fc = round_to_five(ig_price_story_fc * 1.1)
      ig_fb_price_story_ugc = round_to_five(ig_price_story_ugc * 1.1)
      ig_fb_price_post_fc = round_to_five(ig_price_post_fc * 1.1)
      ig_fb_price_post_ugc = round_to_five(ig_price_post_ugc * 1.1)
      ig_fb_price_story_post_fc = round_to_five(ig_price_story_post_fc * 1.1)
      ig_fb_price_story_post_ugc = round_to_five(ig_price_story_post_ugc * 1.1)
    else:
      ig_average_total_like = ig_engagement_percent = ig_story_view = ig_average_post_reach = ig_predicted_ad_post_reach = ig_ad_post_reach = None
      ig_price_story_fc = ig_price_story_ugc = ig_price_post_fc = ig_price_post_ugc = ig_price_story_post_fc = ig_price_story_post_ugc = None
      ig_fb_price_story_fc = ig_fb_price_story_ugc = ig_fb_price_post_fc = ig_fb_price_post_ugc = ig_fb_price_story_post_fc = ig_fb_price_story_post_ugc = None

    context__audience_insight = FacebookAPI().get_audience_insight(business_account_id=business_account_id,
                                                                   access_token=access_token)
    if context__audience_insight:
      ig_response_audience_insight = context__audience_insight.get('data')
    else:
      ig_response_audience_insight = None

  else:
    ig_average_total_like = ig_engagement_percent = ig_story_view = ig_average_post_reach = ig_predicted_ad_post_reach = ig_ad_post_reach = None
    ig_price_story_fc = ig_price_story_ugc = ig_price_post_fc = ig_price_post_ugc = ig_price_story_post_fc = ig_price_story_post_ugc = None
    ig_fb_price_story_fc = ig_fb_price_story_ugc = ig_fb_price_post_fc = ig_fb_price_post_ugc = ig_fb_price_story_post_fc = ig_fb_price_story_post_ugc = None
    ig_response_audience_insight = None

  response = {
    # FB
    "fb_name": fb_name,
    "fb_profile_picture": fb_profile_picture,
    # IG Biography
    "ig_username": ig_username,
    "ig_media_count": ig_media_count,
    "ig_follower_count": ig_follower_count,
    "ig_following_count": ig_following_count,
    "ig_profile_picture": ig_profile_picture,
    # IG Active Follower
    "ig_response_active_follower": ig_response_active_follower,
    "ig_active_follower": ig_active_follower,
    "ig_active_follower_harmonic": ig_active_follower_harmonic,
    "ig_active_follower_percent": ig_active_follower_percent,
    # Media Objects
    "ig_response_media_objects": ig_response_media_objects,
    # Engagement
    "ig_average_total_like": ig_average_total_like,
    "ig_engagement_percent": ig_engagement_percent,
    "ig_story_view": ig_story_view,
    "ig_average_post_reach": ig_average_post_reach,
    "ig_predicted_ad_post_reach": ig_predicted_ad_post_reach,
    "ig_ad_post_reach": ig_ad_post_reach,
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
    # Audience Insight
    "ig_response_audience_insight": ig_response_audience_insight
  }

  return response

