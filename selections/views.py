from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Selection
from shouters.models import Shouter
from campaigns.models import Campaign
from .utils.score import cal


@login_required()
def shouter_score(request, campaign_id):
  selection_list = []
  campaign = Campaign.objects.filter(id=campaign_id).first()

  # IG ONLY
  if not campaign.campaign_is_fb:
    # Work Type = Story only
    if campaign.campaign_work_type == 'story':
      # Query Shouter
      shouters = Shouter.objects.filter(
        is_approve=True,
        is_insight=True,
        gender__in=campaign.shouter_gender,
        is_check_ig=True,
        is_check_ig_story=True,
      )
    # Work Type = Post only
    elif campaign.campaign_work_type == 'post':
      # Query Shouter
      shouters = Shouter.objects.filter(
        is_approve=True,
        is_insight=True,
        gender__in=campaign.shouter_gender,
        is_check_ig=True,
        is_check_ig_post=True
      )
    # Work Type = Story + Post
    else:
      # Query Shouter
      shouters = Shouter.objects.filter(
        is_approve=True,
        is_insight=True,
        gender__in=campaign.shouter_gender,
        is_check_ig=True,
        is_check_ig_story_post=True
      )

  # IG + FB
  else:
    # Work Type = Story only
    if campaign.campaign_work_type == 'story':
      # Query Shouter
      shouters = Shouter.objects.filter(
        is_approve=True,
        is_insight=True,
        gender__in=campaign.shouter_gender,
        is_check_ig_fb=True,
        is_check_ig_fb_story=True,
      )
    # Work Type = Post only
    elif campaign.campaign_work_type == 'post':
      # Query Shouter
      shouters = Shouter.objects.filter(
        is_approve=True,
        is_insight=True,
        gender__in=campaign.shouter_gender,
        is_check_ig_fb=True,
        is_check_ig_fb_post=True
      )
    # Work Type = Story + Post
    else:
      # Query Shouter
      shouters = Shouter.objects.filter(
        is_approve=True,
        is_insight=True,
        gender__in=campaign.shouter_gender,
        is_check_ig_fb=True,
        is_check_ig_fb_story_post=True
      )

  for shouter in shouters:
    # Cal Matching Score
    score = cal(campaign, shouter)

    # PRICE
    ###################################################
    # IG ONLY
    if not campaign.campaign_is_fb:
      # Work Type = Story only
      if campaign.campaign_work_type == 'story':
        if campaign.campaign_content_type_story == 'prepared_content':
          price = shouter.ig_price_story_fc
        else:
          price = shouter.ig_price_story_ugc
      # Work Type = Post only
      elif campaign.campaign_work_type == 'post':
        if campaign.campaign_content_type_post == 'single_post':
          price = shouter.ig_price_post_fc
        else:
          price = shouter.ig_price_post_ugc
      # Work Type = Story + Post
      else:
        if campaign.campaign_content_type_story == 'prepared_content':
          price = shouter.ig_price_story_post_fc
        else:
          price = shouter.ig_price_story_post_ugc

    # IG + FB
    else:
      # Work Type = Story only
      if campaign.campaign_work_type == 'story':
        if campaign.campaign_content_type_story == 'prepared_content':
          price = shouter.ig_fb_price_story_fc
        else:
          price = shouter.ig_fb_price_story_ugc
      # Work Type = Post only
      elif campaign.campaign_work_type == 'post':
        if campaign.campaign_content_type_post == 'single_post':
          price = shouter.ig_fb_price_post_fc
        else:
          price = shouter.ig_fb_price_post_ugc
      # Work Type = Story + Post
      else:
        if campaign.campaign_content_type_story == 'prepared_content':
          price = shouter.ig_fb_price_story_post_fc
        else:
          price = shouter.ig_fb_price_story_post_ugc

    selection_list.append(Selection(
      campaign=campaign,
      shouter=shouter,
      score=score,
      brand_price=round(price*1.4, 0),
      shouter_price=price,
      cpr=round(shouter.ig_ad_post_reach/round(price*1.4, 0), 2),
    ))

  Selection.objects.bulk_create(selection_list)
  return redirect('create_shouter_selection', campaign_id)
