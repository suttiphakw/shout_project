from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from utils import media
from .models import Campaign


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
  campaign = Campaign.objects.filter(id=campaign_id).first()

  # if campaign is not found
  if not campaign:
    return HttpResponse('404Error')

  # if campaign is not created by request.user
  if request.user != campaign.user:
    return HttpResponse('Campaign not allowed')

  # if method == post
  if request.method == 'POST':
    if campaign.campaign_work_type == 'story':
      campaign.campaign_content_type_story = request.POST.get('story_type', None)
      campaign.campaign_fc_story_count = request.POST.get('campaign_fc_story_count', None)
      campaign.save()
    elif campaign.campaign_work_type == 'post':
      campaign.campaign_content_type_post = request.POST.get('post_type', None)
      campaign.save()
    else:
      campaign.campaign_content_type_story = request.POST.get('story_type', None)
      campaign.campaign_fc_story_count = request.POST.get('campaign_fc_story_count', None)
      campaign.campaign_content_type_post = request.POST.get('post_type', None)
      campaign.save()

    return redirect('create_product', campaign_id)

  context = {
    'campaign': campaign,
  }
  return render(request, 'campaigns/create/content_type.html', context)


@login_required()
def create_product(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()
  if campaign:
    if request.method == "POST":
      # File Storage System
      fs = FileSystemStorage()

      product_name = request.POST['product_name']
      product_photo_1 = request.FILES["product_photo_1"] if "product_photo_1" in request.FILES else False
      product_photo_2 = request.FILES["product_photo_2"] if "product_photo_2" in request.FILES else False
      product_photo_3 = request.FILES["product_photo_3"] if "product_photo_3" in request.FILES else False
      product_detail = request.POST['product_detail']
      product_link = request.POST['product_link']

      # Save to DOM
      campaign.product_name = product_name
      campaign.product_detail = product_detail
      campaign.product_link = product_link

      filename_product_photo_1 = fs.save(media.get_unique_name_product('campaign/product/', product_photo_1.name, campaign_id),
                                         product_photo_1)
      campaign.product_photo_1 = filename_product_photo_1
      if product_photo_2:
        filename_product_photo_2 = fs.save(media.get_unique_name_product('campaign/product/', product_photo_2.name, campaign_id, counter=2),
                                           product_photo_2)
        campaign.product_photo_2 = filename_product_photo_2
      if product_photo_3:
        filename_product_photo_3 = fs.save(media.get_unique_name_product('campaign/product/', product_photo_3.name, campaign_id, counter=3),
                                           product_photo_3)
        campaign.product_photo_3 = filename_product_photo_3

      campaign.save()

      return redirect('create_target', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/product.html', context)
  return HttpResponse('404Error')


@login_required()
def create_target(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()

  if campaign:
    if request.method == 'POST':
      # Get Input
      gender = request.POST['gender']
      age = request.POST.getlist('age')
      province = request.POST['province']
      interest = request.POST.getlist('interest')
      shouter_gender = request.POST.getlist('shouter_gender')

      campaign.campaign_gender = gender
      campaign.campaign_age = age
      campaign.campaign_province = province
      campaign.campaign_interest = interest
      campaign.shouter_gender = shouter_gender
      campaign.save()

      return redirect('shouter_score', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/target.html', context)
  return HttpResponse('404Error')


@login_required()
def create_shouter_selection(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()
  # Create Shouter Selection Database
  # List of approve shouter => shouters = Shouter.objects.filter(is_approve=True)
  # for shouter in shouters => shouter_selection.create(shouter = shouter.instagram (def string)

  if campaign:
    # if request.method == 'POST':

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/shouter_selection.html', context)
  return HttpResponse('404Error')



