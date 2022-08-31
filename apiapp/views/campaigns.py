import json
from django.http.response import JsonResponse

from campaigns.models import Campaign


def api_name(request):
  campaign_name = request.POST.get('campaign_name', None)
  campaign = Campaign.objects.create(user=request.user, campaign_name=campaign_name)
  campaign.campaign_phase = 1
  campaign.save()
  # Get ID
  campaign_id = campaign.id

  # context
  context = {
    'status': 'success',
    'campaign_id': campaign_id,
  }
  return JsonResponse(context)


def api_scope_budget(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()
  if not campaign:
    return JsonResponse({'status': 'Campaign name is not found'})

  # Get Input
  campaign_is_ig = json.loads(request.POST.get('is_check_instagram', None))  # bool
  campaign_is_fb = json.loads(request.POST.get('is_check_facebook', None))  # bool
  campaign_budget = int(request.POST.get('budget', None))  # int
  campaign_work_type = request.POST.get('work_type', None)  # str

  if campaign_is_ig or campaign_is_fb:
    if campaign_budget and campaign_work_type:
      campaign.campaign_is_ig = campaign_is_ig
      campaign.campaign_is_fb = campaign_is_fb
      campaign.campaign_budget = int(campaign_budget)
      campaign.campaign_work_type = campaign_work_type
      campaign.campaign_phase = 2
      campaign.save()

      context = {
        'status': 'success',
      }
      return JsonResponse(context)

  context = {
    'status': 'failed'
  }
  return JsonResponse(context)


def api_content_type(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()
  if not campaign:
    return JsonResponse({'status': 'Campaign name is not found'})

  # Get Input
  campaign_content_type_story = request.POST.get('content_type_story', None)
  campaign_fc_story_count = request.POST.get('content_type_story_count', None)
  campaign_content_type_post = request.POST.get('content_type_post', None)

#   print(campaign_content_type_story, type(campaign_content_type_story_count), campaign_content_type_post)
  if campaign_content_type_story == 'undefined' and campaign_content_type_post == 'undefined':
    return JsonResponse({'status': 'failed'})

  if campaign_content_type_story != 'undefined' and campaign_content_type_post == 'undefined':
    campaign.campaign_content_type_story = campaign_content_type_story
    campaign.campaign_fc_story_count = int(campaign_fc_story_count)

  if campaign_content_type_story == 'undefined' and campaign_content_type_post != 'undefined':
    campaign.campaign_content_type_post = campaign_content_type_post

  if campaign_content_type_story != 'undefined' and campaign_content_type_post != 'undefined':
    campaign.campaign_content_type_story = campaign_content_type_story
    campaign.campaign_fc_story_count = campaign_fc_story_count
    campaign.campaign_content_type_post = campaign_content_type_post

  campaign.campaign_phase = 3
  campaign.save()

  context = {
    'status': 'success'
  }

  return JsonResponse(context)



