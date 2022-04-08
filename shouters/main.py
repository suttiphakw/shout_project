from weakref import ref
from .models import Shouter
from .refresh_data import refresh_shouters

def refresh_all():
  shouters = Shouter.objects.filter(fb_is_connect=True)
  for shouter in shouters:
    access_token = shouter.fb_main_access_token
    business_account_id = shouter.ig_business_account_id

    response = refresh_shouters(access_token=access_token, business_account_id=business_account_id)
    if response:
      # FB Biography
      shouter.fb_name = response.get("fb_name", None)
      shouter.fb_profile_picture = response.get("fb_profile_picture", None)
      # IG Biography
      shouter.ig_username = response.get("ig_username", None)
      shouter.ig_media_count = response.get("ig_media_count", None)
      shouter.ig_follower_count = response.get("ig_follower_count", None)
      shouter.ig_following_count = response.get("ig_following_count", None)
      shouter.ig_profile_picture = response.get("ig_profile_picture", None)
      # IG Active Follower
      shouter.ig_response_active_follower = response.get("ig_response_active_follower", None)
      shouter.ig_active_follower = response.get("ig_active_follower", None)
      shouter.ig_active_follower_harmonic = response.get("ig_active_follower_harmonic", None)
      shouter.ig_active_follower_percent = response.get("ig_active_follower_percent", None)
      # Media Objects
      shouter.ig_response_media_objects = response.get("ig_response_media_objects", None)
      # Engagement
      shouter.ig_average_total_like = response.get("ig_average_total_like", None)
      shouter.ig_story_view = response.get("ig_story_view", None)
      shouter.ig_average_post_reach = response.get("ig_average_post_reach", None)
      shouter.ig_reach_source = response.get("ig_reach_source", None)
      # Engagement => จากการคำนวน
      shouter.ig_engagement_percent = response.get("ig_engagement_percent", None)
      shouter.ig_predicted_ad_post_reach = response.get("ig_predicted_ad_post_reach", None)
      shouter.ig_post_reach_guarantee = response.get("ig_post_reach_guarantee", None)
      shouter.ig_story_view_guarantee = response.get("ig_story_view_guarantee", None)
      shouter.ig_ad_post_reach = response.get("ig_ad_post_reach", None)
      # Price
      shouter.ig_price_story_fc = response.get("ig_price_story_fc", None)
      shouter.ig_price_story_ugc = response.get("ig_price_story_ugc", None)
      shouter.ig_price_post_fc = response.get("ig_price_post_fc", None)
      shouter.ig_price_post_ugc = response.get("ig_price_post_ugc", None)
      shouter.ig_price_story_post_fc = response.get("ig_price_story_post_fc", None)
      shouter.ig_price_story_post_ugc = response.get("ig_price_story_post_ugc", None)
      shouter.ig_fb_price_story_fc = response.get("ig_fb_price_story_fc", None)
      shouter.ig_fb_price_story_ugc = response.get("ig_fb_price_story_ugc", None)
      shouter.ig_fb_price_post_fc = response.get("ig_fb_price_post_fc", None)
      shouter.ig_fb_price_post_ugc = response.get("ig_fb_price_post_ugc", None)
      shouter.ig_fb_price_story_post_fc = response.get("ig_fb_price_story_post_fc", None)
      shouter.ig_fb_price_story_post_ugc = response.get("ig_fb_price_story_post_ugc", None)
      # Audience Insight
      shouter.ig_response_audience_insight = response.get("ig_response_audience_insight",  None)
      # Save
      shouter.save()
      print("ID : " + str(shouter.id) + " => success")
    if not response:
      shouter.fb_is_connect = False
      shouter.save()
      print("ID : " + str(shouter.id) + " => log out / private")