from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Campaign
from .utils.calculate import cal
from django.http import JsonResponse


# Create your views here.
@login_required()
def campaign_draft(request):
  user = request.user
  context = {
    'message': user
  }
  return render(request, 'campaigns/draft.html', context)


@login_required()
def campaign_in_progress(request):
  user = request.user
  context = {
    'user': user
  }
  return render(request, 'campaigns/in_progress.html', context)


@login_required()
def campaign_finished(request):
  user = request.user
  context = {
    'user': user
  }
  return render(request, 'campaigns/finished.html', context)


@login_required()
def create_name(request):
  return render(request, 'campaigns/create/name.html')


@login_required()
def create_scope_budget(request, campaign_id):
  if campaign_id is not None:
    campaign = Campaign.objects.filter(id=campaign_id).first()
    if request.user == campaign.user:
      return render(request, 'campaigns/create/scope_budget.html')

    return HttpResponse('Campaign not allowed')
  return HttpResponse('404Error')


@login_required()
def create_content_type(request, campaign_id):
  if campaign_id is not None:
    campaign = Campaign.objects.filter(id=campaign_id).first()
    if request.user == campaign.user:
      return render(request, 'campaigns/create/content_type.html')

    return HttpResponse('Campaign not allowed')
  return HttpResponse('404Error')
  # try:
  #   campaign_id = request.session['campaign_id']
  #   campaign = Campaign.objects.filter(id=campaign_id).first()
  # # Not Found campaign id in session
  # except KeyError:
  #   return HttpRespons2e('404Error')
  #
  # # Story
  # if request.method == 'POST':
  #   if campaign.campaign_work_type == "story":
  #     campaign.campaign_content_type_story = request.POST.get('story_type', False)
  #     campaign.campaign_fc_story_count = request.POST['campaign_fc_story_count']
  #
  #     # Cal Price
  #     response = cal(campaign.campaign_budget)
  #
  #   if campaign.campaign_work_type == "post":
  #     campaign.campaign_content_type_post = request.POST['post_type']
  #   if campaign.campaign_work_type == "post_story":
  #     campaign.campaign_content_type_story = request.POST.get('story_type', False)
  #     campaign.campaign_content_type_post = request.POST.get('post_type', False)
  #     campaign.campaign_fc_story_count = request.POST['campaign_fc_story_count']
  #
  #   campaign.save()
  #
  #   return redirect('create_product')
  #
  # context = {
  #   'campaign': campaign
  # }
  # return render(request, 'campaigns/create/content_type.html', context)


@login_required()
def create_product(request):
  try:
    campaign_id = request.session['campaign_id']
    campaign = Campaign.objects.filter(id=campaign_id).first()
  # Not Found campaign id in session
  except KeyError:
    return HttpResponse('404Error')

  if request.method == "POST":
    campaign_product_name = request.POST['product_name']
    campaign_product_photo_1 = request.FILES["product_photo_1"] if "product_photo_1" in request.FILES else False
    campaign_product_photo_2 = request.FILES["product_photo_2"] if "product_photo_2" in request.FILES else False
    campaign_product_photo_3 = request.FILES["product_photo_3"] if "product_photo_3" in request.FILES else False
    campaign_product_detail =  request.POST['product_detail']
    campaign_product_link = request.POST['product_link']

    return redirect('create_target')

  context = {
    'campaign': campaign
  }
  return render(request, 'campaigns/create/product.html', context)


@login_required()
def create_target(request):
  try:
    campaign_id = request.session['campaign_id']
    campaign = Campaign.objects.filter(id=campaign_id).first()
  # Not Found campaign id in session
  except KeyError:
    return HttpResponse('404Error')

  context = {
    'campaign': campaign
  }
  return render(request, 'campaigns/create/target.html', context)


@login_required()
def create_shouter_selection(request):
  try:
    campaign_id = request.session['campaign_id']
    campaign = Campaign.objects.filter(id=campaign_id).first()
  # Not Found campaign id in session
  except KeyError:
    return HttpResponse('404Error')

  # Get Shouter Selection

  context = {
    'campaign': campaign
  }
  return render(request, 'campaigns/create/shouter_selection.html', context)
