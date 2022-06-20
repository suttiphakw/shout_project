min_avg_story_reach_per_shouter = 621
max_avg_story_reach_per_shouter = 2300
min_avg_post_reach_per_shouter = 3000
max_avg_post_reach_per_shouter = 7250

min_fc_price_per_shouter = 500
max_fc_price_per_shouter = 1458

min_ugc_price_per_shouter = 783
max_ugc_price_per_shouter = 2333

min_single_price_per_shouter = 2000
max_single_price_per_shouter = 3667

min_multi_price_per_shouter = 2500
max_multi_price_per_shouter = 4400


# Constant AVG.Reach
def get_factor(price_per_shouter, avg_reach_1_shouter):
  return price_per_shouter / avg_reach_1_shouter


def get_reach(budget, factor):
  return round((budget / factor) / 100) * 100


def get_shouter(reach, avg_reach_1_shouter):
  return round(reach / avg_reach_1_shouter)


def get_cpr(budget, reach):
  return round((budget / reach) * 100) / 100


def fb(number):
  return round(number / 1.1)


def fb_100(number):
  return round((number / 1.1) / 100) * 100


def fb_2de(number):
  return round(number / 1.1, 2)


def cal(budget):
  min_avg_reach_1_shouter = min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter
  max_avg_reach_1_shouter = max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter

  # # Reach
  # Story
  min_fc_story_reach = get_reach(budget, get_factor(min_fc_price_per_shouter, min_avg_story_reach_per_shouter))
  max_fc_story_reach = get_reach(budget, get_factor(max_fc_price_per_shouter, max_avg_story_reach_per_shouter))
  min_ugc_story_reach = get_reach(budget, get_factor(min_ugc_price_per_shouter, min_avg_story_reach_per_shouter))
  max_ugc_story_reach = get_reach(budget, get_factor(max_ugc_price_per_shouter, max_avg_story_reach_per_shouter))
  # Post
  min_single_post_reach = get_reach(budget, get_factor(min_single_price_per_shouter, min_avg_post_reach_per_shouter))
  max_single_post_reach = get_reach(budget, get_factor(max_single_price_per_shouter, max_avg_post_reach_per_shouter))
  min_multi_post_reach = get_reach(budget, get_factor(min_multi_price_per_shouter, min_avg_post_reach_per_shouter))
  max_multi_post_reach = get_reach(budget, get_factor(max_multi_price_per_shouter, max_avg_post_reach_per_shouter))
  # Story + Post
  min_fc_single_reach = get_reach(budget,
                                  get_factor(
                                    (min_fc_price_per_shouter + min_single_price_per_shouter) * 0.9,
                                    min_avg_reach_1_shouter)
                                  )
  max_fc_single_reach = get_reach(budget,
                                  get_factor(
                                    (max_fc_price_per_shouter + max_single_price_per_shouter) * 0.9,
                                    max_avg_reach_1_shouter)
                                  )
  min_fc_multi_reach = get_reach(budget,
                                 get_factor(
                                   (min_fc_price_per_shouter + min_multi_price_per_shouter) * 0.9,
                                   min_avg_reach_1_shouter)
                                 )
  max_fc_multi_reach = get_reach(budget,
                                 get_factor(
                                   (max_fc_price_per_shouter + max_multi_price_per_shouter) * 0.9,
                                   max_avg_reach_1_shouter)
                                 )
  min_ugc_single_reach = get_reach(budget,
                                   get_factor(
                                     (min_ugc_price_per_shouter + min_single_price_per_shouter) * 0.9,
                                     min_avg_reach_1_shouter)
                                   )
  max_ugc_single_reach = get_reach(budget,
                                   get_factor(
                                     (max_ugc_price_per_shouter + max_single_price_per_shouter) * 0.9,
                                     max_avg_reach_1_shouter)
                                   )
  min_ugc_multi_reach = get_reach(budget,
                                  get_factor(
                                    (min_ugc_price_per_shouter + min_multi_price_per_shouter) * 0.9,
                                    min_avg_reach_1_shouter)
                                  )
  max_ugc_multi_reach = get_reach(budget,
                                  get_factor(
                                    (max_ugc_price_per_shouter + max_multi_price_per_shouter) * 0.9,
                                    max_avg_reach_1_shouter)
                                  )

  # Min Max Reach
  min_story_reach = min(min_fc_story_reach, max_fc_story_reach, min_ugc_story_reach, max_ugc_story_reach)
  max_story_reach = max(min_fc_story_reach, max_fc_story_reach, min_ugc_story_reach, max_ugc_story_reach)
  min_post_reach = min(min_single_post_reach, max_single_post_reach, min_multi_post_reach, max_multi_post_reach)
  max_post_reach = max(min_single_post_reach, max_single_post_reach, min_multi_post_reach, max_multi_post_reach)
  min_story_post_reach = min(min_fc_single_reach, max_fc_single_reach, min_ugc_multi_reach, max_ugc_multi_reach)
  max_story_post_reach = max(min_fc_single_reach, max_fc_single_reach, min_ugc_multi_reach, max_ugc_multi_reach)

  # # Shouter
  # Story
  min_fc_story_shouter = get_shouter(min_fc_story_reach, min_avg_story_reach_per_shouter)
  max_fc_story_shouter = get_shouter(max_fc_story_reach, max_avg_story_reach_per_shouter)
  min_ugc_story_shouter = get_shouter(min_ugc_story_reach, min_avg_story_reach_per_shouter)
  max_ugc_story_shouter = get_shouter(max_ugc_story_reach, max_avg_story_reach_per_shouter)
  # Post
  min_single_post_shouter = get_shouter(min_single_post_reach, min_avg_post_reach_per_shouter)
  max_single_post_shouter = get_shouter(max_single_post_reach, max_avg_post_reach_per_shouter)
  min_multi_post_shouter = get_shouter(min_multi_post_reach, min_avg_post_reach_per_shouter)
  max_multi_post_shouter = get_shouter(max_multi_post_reach, max_avg_post_reach_per_shouter)
  # Story + Post
  min_fc_single_shouter = get_shouter(min_fc_single_reach, min_avg_reach_1_shouter)
  max_fc_single_shouter = get_shouter(max_fc_single_reach, max_avg_reach_1_shouter)
  min_fc_multi_shouter = get_shouter(min_fc_multi_reach, min_avg_reach_1_shouter)
  max_fc_multi_shouter = get_shouter(max_fc_multi_reach, max_avg_reach_1_shouter)
  min_ugc_single_shouter = get_shouter(min_ugc_single_reach, min_avg_reach_1_shouter)
  max_ugc_single_shouter = get_shouter(max_ugc_single_reach, max_avg_reach_1_shouter)
  min_ugc_multi_shouter = get_shouter(min_ugc_multi_reach, min_avg_reach_1_shouter)
  max_ugc_multi_shouter = get_shouter(max_ugc_multi_reach, max_avg_reach_1_shouter)

  # Min Max Shouter
  min_story_shouter = min(min_fc_story_shouter, max_fc_story_shouter, min_ugc_story_shouter, max_ugc_story_shouter)
  max_story_shouter = max(min_fc_story_shouter, max_fc_story_shouter, min_ugc_story_shouter, max_ugc_story_shouter)
  min_post_shouter = min(min_single_post_shouter, max_single_post_shouter, min_multi_post_shouter,
                         max_multi_post_shouter)
  max_post_shouter = max(min_single_post_shouter, max_single_post_shouter, min_multi_post_shouter,
                         max_multi_post_shouter)
  min_story_post_shouter = min(min_fc_single_shouter, max_fc_single_shouter, min_ugc_multi_shouter,
                               max_ugc_multi_shouter)
  max_story_post_shouter = max(min_fc_single_shouter, max_fc_single_shouter, min_ugc_multi_shouter,
                               max_ugc_multi_shouter)

  # # CPR
  # Story
  min_fc_story_cpr = get_cpr(budget, min_fc_story_reach)
  max_fc_story_cpr = get_cpr(budget, max_fc_story_reach)
  min_ugc_story_cpr = get_cpr(budget, min_ugc_story_reach)
  max_ugc_story_cpr = get_cpr(budget, max_ugc_story_reach)
  # Post
  min_single_post_cpr = get_cpr(budget, min_single_post_reach)
  max_single_post_cpr = get_cpr(budget, max_single_post_reach)
  min_multi_post_cpr = get_cpr(budget, min_multi_post_reach)
  max_multi_post_cpr = get_cpr(budget, max_multi_post_reach)
  # Story + Post
  min_fc_single_cpr = get_cpr(budget, min_fc_single_reach)
  max_fc_single_cpr = get_cpr(budget, max_fc_single_reach)
  min_ugc_multi_cpr = get_cpr(budget, min_ugc_multi_reach)
  max_ugc_multi_cpr = get_cpr(budget, max_ugc_multi_reach)

  # Min Max CPR
  min_story_cpr = min(min_fc_story_cpr, max_fc_story_cpr, min_ugc_story_cpr, max_ugc_story_cpr)
  max_story_cpr = max(min_fc_story_cpr, max_fc_story_cpr, min_ugc_story_cpr, max_ugc_story_cpr)
  min_post_cpr = min(min_single_post_cpr, max_single_post_cpr, min_multi_post_cpr, max_multi_post_cpr)
  max_post_cpr = max(min_single_post_cpr, max_single_post_cpr, min_multi_post_cpr, max_multi_post_cpr)
  min_story_post_cpr = min(min_fc_single_cpr, max_fc_single_cpr, min_ugc_multi_cpr, max_ugc_multi_cpr)
  max_story_post_cpr = max(min_fc_single_cpr, max_fc_single_cpr, min_ugc_multi_cpr, max_ugc_multi_cpr)

  # Return
  return {
    # Reach
    "min_story_reach": min_story_reach,
    "max_story_reach": max_story_reach,
    "min_post_reach": min_post_reach,
    "max_post_reach": max_post_reach,
    "min_story_post_reach": min_story_post_reach,
    "max_story_post_reach": max_story_post_reach,
    # Shouter
    "min_story_shouter": min_story_shouter,
    "max_story_shouter": max_story_shouter,
    "min_post_shouter": min_post_shouter,
    "max_post_shouter": max_post_shouter,
    "min_story_post_shouter": min_story_post_shouter,
    "max_story_post_shouter": max_story_post_shouter,
    # CPR
    "min_story_cpr": min_story_cpr,
    "max_story_cpr": max_story_cpr,
    "min_post_cpr": min_post_cpr,
    "max_post_cpr": max_post_cpr,
    "min_story_post_cpr": min_story_post_cpr,
    "max_story_post_cpr": max_story_post_cpr
  }


def cal_fb(budget):
  # # Reach
  # Story
  min_fc_story_reach = get_reach(budget, get_factor(min_fc_price_per_shouter, min_avg_story_reach_per_shouter))
  max_fc_story_reach = get_reach(budget, get_factor(max_fc_price_per_shouter, max_avg_story_reach_per_shouter))
  min_ugc_story_reach = get_reach(budget, get_factor(min_ugc_price_per_shouter, min_avg_story_reach_per_shouter))
  max_ugc_story_reach = get_reach(budget, get_factor(max_ugc_price_per_shouter, max_avg_story_reach_per_shouter))
  # Post
  min_single_post_reach = get_reach(budget, get_factor(min_single_price_per_shouter, min_avg_post_reach_per_shouter))
  max_single_post_reach = get_reach(budget, get_factor(max_single_price_per_shouter, max_avg_post_reach_per_shouter))
  min_multi_post_reach = get_reach(budget, get_factor(min_multi_price_per_shouter, min_avg_post_reach_per_shouter))
  max_multi_post_reach = get_reach(budget, get_factor(max_multi_price_per_shouter, max_avg_post_reach_per_shouter))
  # Story + Post
  min_fc_single_reach = get_reach(budget,
                                  get_factor(
                                    (min_fc_price_per_shouter + min_single_price_per_shouter) * 0.9,
                                    min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter)
                                  )
  max_fc_single_reach = get_reach(budget,
                                  get_factor(
                                    (max_fc_price_per_shouter + max_single_price_per_shouter) * 0.9,
                                    max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter)
                                  )
  min_ugc_multi_reach = get_reach(budget,
                                  get_factor(
                                    (min_ugc_price_per_shouter + min_multi_price_per_shouter) * 0.9,
                                    min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter)
                                  )
  max_ugc_multi_reach = get_reach(budget,
                                  get_factor(
                                    (max_ugc_price_per_shouter + max_multi_price_per_shouter) * 0.9,
                                    max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter)
                                  )

  # Min Max Reach
  min_story_reach = fb_100(min(min_fc_story_reach, max_fc_story_reach, min_ugc_story_reach, max_ugc_story_reach))
  max_story_reach = fb_100(max(min_fc_story_reach, max_fc_story_reach, min_ugc_story_reach, max_ugc_story_reach))
  min_post_reach = fb_100(min(min_single_post_reach, max_single_post_reach, min_multi_post_reach, max_multi_post_reach))
  max_post_reach = fb_100(max(min_single_post_reach, max_single_post_reach, min_multi_post_reach, max_multi_post_reach))
  min_story_post_reach = fb_100(min(min_fc_single_reach, max_fc_single_reach, min_ugc_multi_reach, max_ugc_multi_reach))
  max_story_post_reach = fb_100(max(min_fc_single_reach, max_fc_single_reach, min_ugc_multi_reach, max_ugc_multi_reach))

  # # Shouter
  # Story
  min_fc_story_shouter = get_shouter(min_fc_story_reach, min_avg_story_reach_per_shouter)
  max_fc_story_shouter = get_shouter(max_fc_story_reach, max_avg_story_reach_per_shouter)
  min_ugc_story_shouter = get_shouter(min_ugc_story_reach, min_avg_story_reach_per_shouter)
  max_ugc_story_shouter = get_shouter(max_ugc_story_reach, max_avg_story_reach_per_shouter)
  # Post
  min_single_post_shouter = get_shouter(min_single_post_reach, min_avg_post_reach_per_shouter)
  max_single_post_shouter = get_shouter(max_single_post_reach, max_avg_post_reach_per_shouter)
  min_multi_post_shouter = get_shouter(min_multi_post_reach, min_avg_post_reach_per_shouter)
  max_multi_post_shouter = get_shouter(max_multi_post_reach, max_avg_post_reach_per_shouter)
  # Story + Post
  min_fc_single_shouter = get_shouter(min_fc_single_reach,
                                      min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter)
  max_fc_single_shouter = get_shouter(max_fc_single_reach,
                                      max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter)
  min_ugc_multi_shouter = get_shouter(min_ugc_multi_reach,
                                      min_avg_story_reach_per_shouter + min_avg_post_reach_per_shouter)
  max_ugc_multi_shouter = get_shouter(max_ugc_multi_reach,
                                      max_avg_story_reach_per_shouter + max_avg_post_reach_per_shouter)

  # Min Max Shouter
  min_story_shouter = fb(min(min_fc_story_shouter, max_fc_story_shouter, min_ugc_story_shouter, max_ugc_story_shouter))
  max_story_shouter = fb(max(min_fc_story_shouter, max_fc_story_shouter, min_ugc_story_shouter, max_ugc_story_shouter))
  min_post_shouter = fb(min(min_single_post_shouter, max_single_post_shouter, min_multi_post_shouter,
                            max_multi_post_shouter))
  max_post_shouter = fb(max(min_single_post_shouter, max_single_post_shouter, min_multi_post_shouter,
                            max_multi_post_shouter))
  min_story_post_shouter = fb(min(min_fc_single_shouter, max_fc_single_shouter, min_ugc_multi_shouter,
                                  max_ugc_multi_shouter))
  max_story_post_shouter = fb(max(min_fc_single_shouter, max_fc_single_shouter, min_ugc_multi_shouter,
                                  max_ugc_multi_shouter))

  # # CPR
  # Story
  min_fc_story_cpr = get_cpr(budget, min_fc_story_reach)
  max_fc_story_cpr = get_cpr(budget, max_fc_story_reach)
  min_ugc_story_cpr = get_cpr(budget, min_ugc_story_reach)
  max_ugc_story_cpr = get_cpr(budget, max_ugc_story_reach)
  # Post
  min_single_post_cpr = get_cpr(budget, min_single_post_reach)
  max_single_post_cpr = get_cpr(budget, max_single_post_reach)
  min_multi_post_cpr = get_cpr(budget, min_multi_post_reach)
  max_multi_post_cpr = get_cpr(budget, max_multi_post_reach)
  # Story + Post
  min_fc_single_cpr = get_cpr(budget, min_fc_single_reach)
  max_fc_single_cpr = get_cpr(budget, max_fc_single_reach)
  min_ugc_multi_cpr = get_cpr(budget, min_ugc_multi_reach)
  max_ugc_multi_cpr = get_cpr(budget, max_ugc_multi_reach)

  # Min Max CPR
  min_story_cpr = fb_2de(min(min_fc_story_cpr, max_fc_story_cpr, min_ugc_story_cpr, max_ugc_story_cpr))
  max_story_cpr = fb_2de(max(min_fc_story_cpr, max_fc_story_cpr, min_ugc_story_cpr, max_ugc_story_cpr))
  min_post_cpr = fb_2de(min(min_single_post_cpr, max_single_post_cpr, min_multi_post_cpr, max_multi_post_cpr))
  max_post_cpr = fb_2de(max(min_single_post_cpr, max_single_post_cpr, min_multi_post_cpr, max_multi_post_cpr))
  min_story_post_cpr = fb_2de(min(min_fc_single_cpr, max_fc_single_cpr, min_ugc_multi_cpr, max_ugc_multi_cpr))
  max_story_post_cpr = fb_2de(max(min_fc_single_cpr, max_fc_single_cpr, min_ugc_multi_cpr, max_ugc_multi_cpr))

  # Return
  return {
    # Reach
    "min_story_reach": min_story_reach,
    "max_story_reach": max_story_reach,
    "min_post_reach": min_post_reach,
    "max_post_reach": max_post_reach,
    "min_story_post_reach": min_story_post_reach,
    "max_story_post_reach": max_story_post_reach,
    # Shouter
    "min_story_shouter": min_story_shouter,
    "max_story_shouter": max_story_shouter,
    "min_post_shouter": min_post_shouter,
    "max_post_shouter": max_post_shouter,
    "min_story_post_shouter": min_story_post_shouter,
    "max_story_post_shouter": max_story_post_shouter,
    # CPR
    "min_story_cpr": min_story_cpr,
    "max_story_cpr": max_story_cpr,
    "min_post_cpr": min_post_cpr,
    "max_post_cpr": max_post_cpr,
    "min_story_post_cpr": min_story_post_cpr,
    "max_story_post_cpr": max_story_post_cpr
  }
