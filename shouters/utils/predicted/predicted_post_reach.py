import statistics

def get(ig_average_total_like, ig_story_view):
  return statistics.mean([ig_average_total_like*5, ig_story_view*3])
