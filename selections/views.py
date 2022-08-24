from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Selection
from shouters.models import Shouter
from campaigns.models import Campaign
from .utils.score import cal


@login_required()
def shouter_score(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()
  shouters = Shouter.objects.filter(is_approve=True, is_insight=True, gender__in=campaign.shouter_gender)
  selection_list = []
  for shouter in shouters:
    # Cal Matching Score
    score = cal(campaign, shouter)
    selection_list.append(Selection(campaign=campaign, shouter=shouter, score=score))

  Selection.objects.bulk_create(selection_list)
  return redirect('create_shouter_selection', campaign_id)
