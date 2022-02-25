def get(ig_story_view, ig_average_post_reach):
  ig_predicted_ad_post_reach = ig_story_view * 3
  ig_story_view_guarantee = ig_story_view * 0.5
  if ig_average_post_reach <= ig_predicted_ad_post_reach:
    ig_ad_post_reach = ig_average_post_reach
    ig_post_reach_guarantee = ig_average_post_reach * 0.3
  else:
    ig_ad_post_reach = (ig_average_post_reach + ig_predicted_ad_post_reach) / 2
    ig_post_reach_guarantee = ig_predicted_ad_post_reach

  context = {
    'ig_predicted_ad_post_reach': ig_predicted_ad_post_reach,
    'ig_post_reach_guarantee': ig_post_reach_guarantee,
    'ig_story_view_guarantee': ig_story_view_guarantee,
    'ig_ad_post_reach': ig_ad_post_reach
  }

  return context
