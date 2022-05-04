# Constant AVG.Reach
min_avg_story_reach_factor = 621
max_avg_story_reach_factor = 2300
min_avg_post_reach_factor = 3000
max_avg_post_reach_factor = 7250
min_avg_story_post_reach_factor = 3621
max_avg_story_post_reach_factor = 9550

# Constant Story FC
min_fc_story_reach_factor = 0.805
max_fc_story_reach_factor = 0.634

# Constant Story UGC
min_ugc_story_reach_factor = 1.261
max_ugc_story_reach_factor = 1.014

# Constant Post Single
min_single_post_reach_factor = 0.667
max_single_post_reach_factor = 0.506

# Constant Post Multi
min_multi_post_reach_factor = 0.833
max_multi_post_reach_factor = 0.607

# Constant Story + Post Lower
min_lower_story_post_reach_factor = 0.621
max_lower_story_post_reach_factor = 0.483

# Constant Story + Post Upper
min_upper_story_post_reach_factor = 0.816
max_upper_story_post_reach_factor = 0.635

######################################################################################################
# Number of Shouter
def min_story_shouter(budget):
  return round((budget / max_ugc_story_reach_factor) / max_avg_story_reach_factor)


def max_story_shouter(budget):
  return round((budget / min_fc_story_reach_factor) / min_avg_story_reach_factor)


def min_post_shouter(budget):
  return round((budget / max_multi_post_reach_factor) / max_avg_post_reach_factor)


def max_post_shouter(budget):
  return round((budget / min_single_post_reach_factor) / min_avg_post_reach_factor)


def min_story_post_shouter(budget):
  return round((budget / max_upper_story_post_reach_factor) / max_avg_story_post_reach_factor)


def max_story_post_shouter(budget):
  return round((budget / min_lower_story_post_reach_factor) / min_avg_story_post_reach_factor)

######################################################################################################
# Number of Reach
def min_story_reach(budget):
  return round((budget / min_ugc_story_reach_factor) / 100) * 100


def max_story_reach(budget):
  return round((budget / max_fc_story_reach_factor) / 100) * 100


def min_post_reach(budget):
  return round((budget / min_multi_post_reach_factor) / 100) * 100


def max_post_reach(budget):
  return round((budget / max_single_post_reach_factor) / 100) * 100


def min_story_post_reach(budget):
  return round((budget / min_upper_story_post_reach_factor) / 100) * 100


def max_story_post_reach(budget):
  return round((budget / max_lower_story_post_reach_factor) / 100) * 100

######################################################################################################
