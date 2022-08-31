from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from utils import media
from .models import Campaign
from selections.models import Selection
from shouters.models import Shouter
from orders.models import Order


@login_required()
def campaign_draft(request):
  campaigns = Campaign.objects.filter(user=request.user, campaign_status='draft')
  campaign_draft_count = Campaign.objects.filter(user=request.user, campaign_status='draft').count()
  campaign_in_progress_count = Campaign.objects.filter(user=request.user, campaign_status='in_progress').count()
  campaign_finished_count = Campaign.objects.filter(user=request.user, campaign_status='finished').count()
  context = {
    'campaigns': campaigns,
    'campaign_draft_count': campaign_draft_count,
    'campaign_in_progress_count': campaign_in_progress_count,
    'campaign_finished_count': campaign_finished_count,
  }
  return render(request, 'campaigns/draft.html', context)


@login_required()
def campaign_in_progress(request):
  campaigns = Campaign.objects.filter(user=request.user, campaign_status='in_progress')
  campaign_draft_count = Campaign.objects.filter(user=request.user, campaign_status='draft').count()
  campaign_in_progress_count = Campaign.objects.filter(user=request.user, campaign_status='in_progress').count()
  campaign_finished_count = Campaign.objects.filter(user=request.user, campaign_status='finished').count()
  context = {
    'campaigns': campaigns,
    'campaign_draft_count': campaign_draft_count,
    'campaign_in_progress_count': campaign_in_progress_count,
    'campaign_finished_count': campaign_finished_count,
  }
  return render(request, 'campaigns/in_progress.html', context)


@login_required()
def campaign_finished(request):
  campaigns = Campaign.objects.filter(user=request.user, campaign_status='finished')
  campaign_draft_count = Campaign.objects.filter(user=request.user, campaign_status='draft').count()
  campaign_in_progress_count = Campaign.objects.filter(user=request.user, campaign_status='in_progress').count()
  campaign_finished_count = Campaign.objects.filter(user=request.user, campaign_status='finished').count()
  context = {
    'campaigns': campaigns,
    'campaign_draft_count': campaign_draft_count,
    'campaign_in_progress_count': campaign_in_progress_count,
    'campaign_finished_count': campaign_finished_count,
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
      campaign.campaign_phase = 3
      campaign.save()
    elif campaign.campaign_work_type == 'post':
      campaign.campaign_content_type_post = request.POST.get('post_type', None)
      campaign.campaign_phase = 3
      campaign.save()
    else:
      campaign.campaign_content_type_story = request.POST.get('story_type', None)
      campaign.campaign_fc_story_count = request.POST.get('campaign_fc_story_count', None)
      campaign.campaign_content_type_post = request.POST.get('post_type', None)
      campaign.campaign_phase = 3
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

      campaign.campaign_phase = 4
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
      campaign.campaign_phase = 5
      campaign.save()

      if Selection.objects.filter(campaign=campaign).exists():
        return redirect('create_shouter_selection', campaign_id)
      return redirect('shouter_score', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/target.html', context)
  return HttpResponse('404Error')


@login_required()
def create_shouter_selection(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()
  if campaign:
    if request.method == 'POST':
      for key, value in request.POST.items():
        if key == 'csrfmiddlewaretoken':
          continue
        shouter = Shouter.objects.filter(id=key).first()
        order = Order.objects.filter(campaign=campaign, shouter=shouter).first()
        order.is_selected = True
        order.save()

      return redirect('create_operation_brand_delivery', campaign_id)

    # bulk create
    brand_selected_price = int(campaign.campaign_budget * 1.5)
    # print(brand_selected_price)
    if not Order.objects.filter(campaign=campaign).exists():
      selections = Selection.objects.filter(campaign=campaign).order_by('-score')
      order_list = []
      # Not more than brand_price
      total_price = 0
      for selection in selections:
        if total_price >= brand_selected_price:
          break
        order_list.append(Order(
          # Status
          campaign=campaign,
          shouter=selection.shouter,
          # Info
          brand_price=selection.brand_price,
          shouter_price=selection.shouter_price,
          cpr=selection.cpr,
          score=selection.score,
          # IG Basic
          ig_follower_count=selection.shouter.ig_follower_count,
          ig_following_count=selection.shouter.ig_following_count,
          ig_media_count=selection.shouter.ig_media_count,
          # IG Insight
          ig_average_total_like=selection.shouter.ig_average_total_like,
          ig_engagement_percent=selection.shouter.ig_engagement_percent,
          ig_active_follower=selection.shouter.ig_active_follower,
          ig_active_follower_percent=selection.shouter.ig_active_follower_percent,
          ig_story_view=selection.shouter.ig_story_view,
          ig_ad_post_reach=selection.shouter.ig_ad_post_reach,
          ig_audience_male_percent=selection.shouter.ig_audience_male_percent,
          ig_audience_female_percent=selection.shouter.ig_audience_female_percent,
          ig_audience_undefined_percent=selection.shouter.ig_audience_undefined_percent,
          ig_age_range_13_17=selection.shouter.ig_age_range_13_17,
          ig_age_range_18_24=selection.shouter.ig_age_range_18_24,
          ig_age_range_25_34=selection.shouter.ig_age_range_25_34,
          ig_age_range_35_44=selection.shouter.ig_age_range_35_44,
          ig_age_range_45_54=selection.shouter.ig_age_range_45_54,
          ig_age_range_55_64=selection.shouter.ig_age_range_55_64,
          ig_audience_location_1=selection.shouter.ig_audience_location_1,
          ig_audience_location_1_percent=selection.shouter.ig_audience_location_1_percent,
          ig_audience_location_2=selection.shouter.ig_audience_location_2,
          ig_audience_location_2_percent=selection.shouter.ig_audience_location_2_percent,
        ))
        total_price += selection.brand_price

      Order.objects.bulk_create(order_list)

    orders = Order.objects.filter(campaign=campaign).order_by('-score')
    context = {
      'campaign': campaign,
      'orders': orders,
      'brand_selected_price': brand_selected_price,
    }
    return render(request, 'campaigns/create/shouter_selection.html', context)
  return HttpResponse('404Error')


@login_required()
def create_shouter_selection_2(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()

  if campaign:
    # if request.method == 'POST':

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/shouter_selection_2.html', context)  # shouter_selection 2
  return HttpResponse('404Error')


@login_required()
def create_operation_brand_delivery(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()

  if campaign:
    if request.method == 'POST':
      fs = FileSystemStorage()

      operation_photo = request.FILES["operation_photo"] if "operation_photo" in request.FILES else False
      filename_operation_photo = fs.save(media.get_unique_name_product('campaign/operation/', operation_photo.name, campaign_id, counter=1),
                                         operation_photo)
      campaign.operation_photo = filename_operation_photo

      service_name = request.POST['service_name']
      service_price = request.POST['service_price']

      # date
      campaign_launch_date = request.POST['campaign_launch_date']
      deliver_shouter_date = request.POST['deliver_shouter_date']
      shouter_pickup_date = request.POST['shouter_pickup_date']
      shouter_sent_draft_date = request.POST['shouter_sent_draft_date']
      shouter_post_date = request.POST['shouter_post_date']
      campaign_end_date = request.POST['campaign_end_date']

      service_detail = {
        'service_price': service_price,
        'campaign_launch_date': campaign_launch_date,
        'deliver_shouter_date': deliver_shouter_date,
        'shouter_pickup_date': shouter_pickup_date,
        'shouter_sent_draft_date': shouter_sent_draft_date,
        'campaign_end_date': campaign_end_date,
      }
      campaign.service_type = 'brand delivery'
      campaign.service_name = service_name
      campaign.service_detail = service_detail
      campaign.shouter_post_date = shouter_post_date
      campaign.campaign_phase = 7
      campaign.save()
      return redirect('create_brief', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/operation/brand_delivery.html', context)  # operation & timeline
  return HttpResponse('404Error')


@login_required()
def create_operation_shout_delivery(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()

  if campaign:
    if request.method == 'POST':
      fs = FileSystemStorage()

      operation_photo = request.FILES["operation_photo"] if "operation_photo" in request.FILES else False
      filename_operation_photo = fs.save(media.get_unique_name_product('campaign/operation/', operation_photo.name, campaign_id, counter=1),
                                         operation_photo)
      campaign.operation_photo = filename_operation_photo

      service_name = request.POST['service_name']
      service_price = request.POST['service_price']

      # date
      campaign_launch_date = request.POST['campaign_launch_date']
      deliver_shouter_date = request.POST['deliver_shouter_date']
      shouter_pickup_date = request.POST['shouter_pickup_date']
      shouter_sent_draft_date = request.POST['shouter_sent_draft_date']
      shouter_post_date = request.POST['shouter_post_date']
      campaign_end_date = request.POST['campaign_end_date']

      service_detail = {
        'service_price': service_price,
        'campaign_launch_date': campaign_launch_date,
        'deliver_shouter_date': deliver_shouter_date,
        'shouter_pickup_date': shouter_pickup_date,
        'shouter_sent_draft_date': shouter_sent_draft_date,
        'campaign_end_date': campaign_end_date,
      }
      campaign.service_type = 'shout delivery'
      campaign.service_name = service_name
      campaign.service_detail = service_detail
      campaign.shouter_post_date = shouter_post_date
      campaign.campaign_phase = 7
      campaign.save()
      return redirect('create_brief', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/operation/shout_delivery.html', context)  # operation & timeline
  return HttpResponse('404Error')


@login_required()
def create_operation_self_buy(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()

  if campaign:
    if request.method == 'POST':
      fs = FileSystemStorage()

      operation_photo = request.FILES["operation_photo"] if "operation_photo" in request.FILES else False
      filename_operation_photo = fs.save(media.get_unique_name_product('campaign/operation/', operation_photo.name, campaign_id, counter=1),
                                         operation_photo)
      campaign.operation_photo = filename_operation_photo

      service_name = request.POST['service_name']
      service_price = request.POST['service_price']
      service_place = request.POST['service_place']

      # date
      campaign_launch_date = request.POST['campaign_launch_date']
      shouter_accept_date = request.POST['shouter_accept_date']
      shouter_sent_draft_date = request.POST['shouter_sent_draft_date']
      shouter_post_date = request.POST['shouter_post_date']
      campaign_end_date = request.POST['campaign_end_date']

      service_detail = {
        'service_price': service_price,
        'service_place': service_place,
        'campaign_launch_date': campaign_launch_date,
        'shouter_accept_date': shouter_accept_date,
        'shouter_sent_draft_date': shouter_sent_draft_date,
        'campaign_end_date': campaign_end_date,
      }
      campaign.service_type = 'shouter self-buy'
      campaign.service_name = service_name
      campaign.service_detail = service_detail
      campaign.shouter_post_date = shouter_post_date
      campaign.campaign_phase = 7
      campaign.save()
      return redirect('create_brief', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/operation/self_buy.html', context)  # operation & timeline
  return HttpResponse('404Error')


@login_required()
def create_operation_web_app(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()

  if campaign:
    if request.method == 'POST':
      fs = FileSystemStorage()

      operation_photo = request.FILES["operation_photo"] if "operation_photo" in request.FILES else False
      filename_operation_photo = fs.save(media.get_unique_name_product('campaign/operation/', operation_photo.name, campaign_id, counter=1),
                                         operation_photo)
      campaign.operation_photo = filename_operation_photo

      service_name = request.POST['service_name']
      service_link = request.POST['service_link']

      # date
      campaign_launch_date = request.POST['campaign_launch_date']
      shouter_accept_date = request.POST['shouter_accept_date']
      shouter_sent_draft_date = request.POST['shouter_sent_draft_date']
      shouter_post_date = request.POST['shouter_post_date']
      campaign_end_date = request.POST['campaign_end_date']

      service_detail = {
        'service_link': service_link,
        'campaign_launch_date': campaign_launch_date,
        'shouter_accept_date': shouter_accept_date,
        'shouter_sent_draft_date': shouter_sent_draft_date,
        'campaign_end_date': campaign_end_date,
      }
      campaign.service_type = 'web / app'
      campaign.service_name = service_name
      campaign.service_detail = service_detail
      campaign.shouter_post_date = shouter_post_date
      campaign.campaign_phase = 7
      campaign.save()
      return redirect('create_brief', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/operation/web_app.html', context)  # operation & timeline
  return HttpResponse('404Error')


@login_required()
def create_operation_go_review(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()

  if campaign:
    if request.method == 'POST':
      fs = FileSystemStorage()

      operation_photo = request.FILES["operation_photo"] if "operation_photo" in request.FILES else False
      filename_operation_photo = fs.save(media.get_unique_name_product('campaign/operation/', operation_photo.name, campaign_id, counter=1),
                                         operation_photo)
      campaign.operation_photo = filename_operation_photo

      service_name = request.POST['service_name']
      service_place = request.POST['service_place']
      service_location = request.POST['service_location']
      service_payback = request.POST['service_payback']
      service_price = request.POST['service_price']

      # date
      campaign_launch_date = request.POST['campaign_launch_date']
      shouter_accept_date = request.POST['shouter_accept_date']
      shouter_sent_draft_date = request.POST['shouter_sent_draft_date']
      shouter_post_date = request.POST['shouter_post_date']
      campaign_end_date = request.POST['campaign_end_date']

      service_detail = {
        'service_place': service_place,
        'service_location': service_location,
        'service_payback': service_payback,
        'service_price': service_price,
        'campaign_launch_date': campaign_launch_date,
        'shouter_accept_date': shouter_accept_date,
        'shouter_sent_draft_date': shouter_sent_draft_date,
        'campaign_end_date': campaign_end_date,
      }
      campaign.service_type = 'go & review'
      campaign.service_name = service_name
      campaign.service_detail = service_detail
      campaign.shouter_post_date = shouter_post_date
      campaign.campaign_phase = 7
      campaign.save()
      return redirect('create_brief', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/operation/go_review.html', context)  # operation & timeline
  return HttpResponse('404Error')


@login_required()
def create_brief(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()

  if campaign:
    if request.method == 'POST':
      fs = FileSystemStorage()

      brief_detail = request.POST['brief_detail']
      brief_photo = request.FILES["brief_photo"] if "brief_photo" in request.FILES else False
      brief_caption = request.POST["brief_caption"]
      brief_ref_photo = request.FILES['brief_ref_photo'] if 'brief_ref_photo' in request.FILES else False

      # Collect Files
      if brief_photo:
        filename_brief_photo = fs.save(media.get_unique_name_product('campaign/brief/photo/', brief_photo.name, campaign_id, counter=1),
                                       brief_photo)
        campaign.brief_photo = filename_brief_photo

      campaign.brief_detail = brief_detail
      campaign.brief_caption = brief_caption

      filename_brief_ref_photo = fs.save(media.get_unique_name_product('campaign/brief/ref/', brief_ref_photo.name, campaign_id, counter=1),
                                         brief_ref_photo)
      campaign.brief_ref_photo = filename_brief_ref_photo
      campaign.campaign_phase = 8
      campaign.save()

      return redirect('campaign_summary', campaign_id)

    context = {
      'campaign': campaign
    }
    return render(request, 'campaigns/create/brief.html', context)  # brief
  return HttpResponse('404Error')


@login_required()
def campaign_summary(request, campaign_id):
  campaign = Campaign.objects.filter(id=campaign_id).first()
  context = {
    'campaign': campaign
  }
  return render(request, 'campaigns/create/summary.html', context)