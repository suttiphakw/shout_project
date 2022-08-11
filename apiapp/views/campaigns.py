# import json
#
# from django.http.response import JsonResponse
# from rest_framework.decorators import api_view
#
# from campaigns.models import Campaign
#
#
# def qdict_to_dict(qdict):
#   """Convert a Django QueryDict to a Python dict.
#
#   Single-value fields are put in directly, and for multi-value fields, a list
#   of all values is stored at the field's key.
#
#   """
#   return {k: v[0] if len(v) == 1 else v for k, v in qdict.lists()}
#
#
# # Create your views here.
# @api_view(['POST'])
# def api_name(request):
#   # Get Input
#   campaign_name = request.data.get('campaign_name', None)
#   # Create campaign
#   campaign = Campaign.objects.create(user=request.user, campaign_name=campaign_name)
#   campaign.save()
#   campaign_id = campaign.id
#
#   if campaign_name:
#     context = {
#       'status': 'success',
#       'campaign_id': campaign_id
#     }
#     return JsonResponse(context)
#
#   context = {
#     'status': 'Campaign name is not found'
#   }
#   return JsonResponse(context)
#
#
# @api_view(['PATCH'])
# def api_scope_budget(request, campaign_id):
#   campaign = Campaign.objects.filter(id=campaign_id).first()
#
#   # Get Input
#   campaign_is_ig = request.data.get('is_check_instagram', None)
#   campaign_is_fb = request.data.get('is_check_facebook', None)
#   campaign_budget = request.data.get('budget', None)
#   campaign_work_type = request.data.get('work_type', None)
#
#   if campaign_is_ig or campaign_is_fb:
#     if campaign_budget and campaign_work_type:
#       campaign.campaign_is_ig = campaign_is_ig
#       campaign.campaign_is_fb = campaign_is_fb
#       campaign.campaign_budget = campaign_budget
#       campaign.campaign_work_type = campaign_work_type
#       campaign.save()
#
#       context = {
#         'status': 'success',
#       }
#       return JsonResponse(context)
#
#   context = {
#     'status': 'Campaign name is not found'
#   }
#   return JsonResponse(context)
#
#
#

import json
from django.http.response import JsonResponse

from campaigns.models import Campaign


def api_name(request):
  campaign_name = request.POST.get('campaign_name', None)
  campaign = Campaign.objects.create(user=request.user, campaign_name=campaign_name)
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
      campaign.save()

      context = {
        'status': 'success',
      }
      return JsonResponse(context)

  context = {
    'status': 'Campaign name is not found'
  }
  return JsonResponse(context)