from . import constant


def get(ig_follower_count, ig_average_total_like):
  if ig_follower_count <= 5000:
    return ig_average_total_like * constant.peers_story_view_per_like
  if ig_follower_count <= 10000:
    return ig_average_total_like * constant.nano_story_view_per_like
  return ig_average_total_like * constant.micro_story_view_per_like