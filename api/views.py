from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.core.files.storage import FileSystemStorage

from shouters.models import Shouter
# Story Insights
from shouters.utils.instagram.ig_api_get_story_list import get as get_story_list
from shouters.utils.instagram.ig_api_get_permalink_story import get as get_story_id
from shouters.utils.instagram.ig_api_get_story_insights import get as get_story_insights
# Post Insights
from shouters.utils.instagram.ig_api_media_objects import get as get_post_list
from shouters.utils.instagram.ig_api_get_permalink_post import get as get_post_id
from shouters.utils.instagram.ig_api_get_post_insights import get as get_post_insights
from utils.final import \
  campaign_detail_delivery, \
  campaign_detail_no_delivery, \
  wait_delivery, \
  delivery_complete, \
  draft, \
  sent_draft, \
  revise_draft, \
  approve_draft, \
  sent_work, \
  wait_check_work, \
  finish, \
  payment, \
  reject_work, \
  cancel_work


@login_required(login_url='/api/login/')
def index(request):
  return render(request, 'api/index.html')


def login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_staff:
      auth.login(request, user)
      return redirect('api_index')

  return render(request, 'api/login.html')


@login_required(login_url='/api/login/')
def flex(request):
  return render(request, 'api/flex/index.html')


# 1.1 campaign detail (with delivery)
@login_required(login_url='/api/login/')
def main_campaign_detail_delivery(request):
  if request.method == 'POST':
    context = {
      'accept_date_time': request.POST['accept_date_time'],
      'campaign_name': request.POST['campaign_name'],
      'campaign_picture': request.POST['campaign_picture'],
      'social_media': request.POST['social_media'],
      'work_type': request.POST['work_type'],
      'price': request.POST['price'],
      'work_type_text': request.POST['work_type_text'],
      'post_count': request.POST['post_count'],
      'text': request.POST['text'],
      'accept_date': request.POST['accept_date'],
      'accept_work_date': request.POST['accept_work_date'],
      'wait_delivery_date': request.POST['wait_delivery_date'],
      'start_work_date': request.POST['start_work_date'],
      'post_date': request.POST['post_date'],
      'payment_date': request.POST['payment_date'],
      'reference_picture': request.POST['reference_picture'],
      'google_form_link': request.POST['google_form_link'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      shouter = Shouter.objects.filter(line_user_id=line_user_id).first()
      ig_username = shouter.ig_username

      # IG Only
      if context['social_media'] == 'ig' and context['work_type'] == 'story' and context['price'] == 'min':
        price = shouter.ig_price_story_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story' and context['price'] == 'max':
        price = shouter.ig_price_story_ugc
      elif context['social_media'] == 'ig' and context['work_type'] == 'post' and context['price'] == 'min':
        price = shouter.ig_price_post_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'post' and context['price'] == 'max':
        price = shouter.ig_price_post_ugc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story_post' and context['price'] == 'min':
        price = shouter.ig_price_story_post_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story_post' and context['price'] == 'max':
        price = shouter.ig_price_story_post_ugc

      # IG + FB
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story' and context['price'] == 'min':
        price = shouter.ig_fb_price_story_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story' and context['price'] == 'max':
        price = shouter.ig_fb_price_story_ugc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'post' and context['price'] == 'min':
        price = shouter.ig_fb_price_post_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'post' and context['price'] == 'max':
        price = shouter.ig_fb_price_post_ugc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story_post' and context['price'] == 'min':
        price = shouter.ig_fb_price_story_post_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story_post' and context['price'] == 'max':
        price = shouter.ig_fb_price_story_post_ugc
      else:
        failed_id.append(line_user_id)
        continue

      if context['social_media'] == 'ig':
        response = campaign_detail_delivery.ig(line_user_id=line_user_id, ig_username=ig_username, price=price, context=context)
      else:
        response = campaign_detail_delivery.ig_fb(line_user_id=line_user_id, ig_username=ig_username, price=price, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/11_campaign_detail_delivery.html')


# 1.2 campaign detail (without delivery)
@login_required(login_url='/api/login/')
def main_campaign_detail_no_delivery(request):
  if request.method == 'POST':
    context = {
      'accept_date_time': request.POST['accept_date_time'],
      'campaign_name': request.POST['campaign_name'],
      'campaign_picture': request.POST['campaign_picture'],
      'social_media': request.POST['social_media'],
      'work_type': request.POST['work_type'],
      'price': request.POST['price'],
      'work_type_text': request.POST['work_type_text'],
      'post_count': request.POST['post_count'],
      'text': request.POST['text'],
      'accept_date': request.POST['accept_date'],
      'accept_work_date': request.POST['accept_work_date'],
      'start_work_date': request.POST['start_work_date'],
      'post_date': request.POST['post_date'],
      'payment_date': request.POST['payment_date'],
      'reference_picture': request.POST['reference_picture'],
      'google_form_link': request.POST['google_form_link'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      shouter = Shouter.objects.filter(line_user_id=line_user_id).first()
      ig_username = shouter.ig_username

      # IG Only
      if context['social_media'] == 'ig' and context['work_type'] == 'story' and context['price'] == 'min':
        price = shouter.ig_price_story_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story' and context['price'] == 'max':
        price = shouter.ig_price_story_ugc
      elif context['social_media'] == 'ig' and context['work_type'] == 'post' and context['price'] == 'min':
        price = shouter.ig_price_post_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'post' and context['price'] == 'max':
        price = shouter.ig_price_post_ugc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story_post' and context['price'] == 'min':
        price = shouter.ig_price_story_post_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story_post' and context['price'] == 'max':
        price = shouter.ig_price_story_post_ugc

      # IG + FB
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story' and context['price'] == 'min':
        price = shouter.ig_fb_price_story_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story' and context['price'] == 'max':
        price = shouter.ig_fb_price_story_ugc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'post' and context['price'] == 'min':
        price = shouter.ig_fb_price_post_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'post' and context['price'] == 'max':
        price = shouter.ig_fb_price_post_ugc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story_post' and context['price'] == 'min':
        price = shouter.ig_fb_price_story_post_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story_post' and context['price'] == 'max':
        price = shouter.ig_fb_price_story_post_ugc
      else:
        failed_id.append(line_user_id)
        continue

      if context['social_media'] == 'ig':
        response = campaign_detail_no_delivery.ig(line_user_id=line_user_id, ig_username=ig_username, price=price, context=context)
        # response = campaign_detail_no_delivery.ig(line_user_id=line_user_id, ig_username='manhoolay', price=2345, context=context)
      else:
        response = campaign_detail_no_delivery.ig_fb(line_user_id=line_user_id, ig_username=ig_username, price=price, context=context)
        # response = campaign_detail_no_delivery.ig_fb(line_user_id=line_user_id, ig_username='manhoolay', price=2345, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/12_campaign_detail_no_delivery.html')


# 2.1 รอจัดส่ง (Wait Delivery)
@login_required(login_url='/api/login/')
def main_wait_delivery(request):
  if request.method == 'POST':
    context = {
      'campaign_name': request.POST['campaign_name'],
      'location': request.POST['location'],
      'tel': request.POST['tel'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:

      response = wait_delivery.all_social(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/21_wait_delivery.html')


# 2.2 จัดส่งแล้ว (Delivery Complete)
@login_required(login_url='/api/login/')
def main_delivery_complete(request):
  if request.method == 'POST':
    context = {
      'campaign_name': request.POST['campaign_name'],
      'tracking_num': request.POST['tracking_num'],
      'google_form_link': request.POST['google_form_link'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:

      response = delivery_complete.all_social(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/22_delivery_complete.html')


# 3. กำลังทำงาน (Draft)
@login_required(login_url='/api/login/')
def main_draft(request):
  if request.method == 'POST':
    context = {
      'sent_date': request.POST['sent_date'],
      'campaign_name': request.POST['campaign_name'],
      'social_media': request.POST['social_media'],
      'work_type': request.POST['work_type'],
      'work_type_text': request.POST['work_type_text'],
      'post_count': request.POST['post_count'],
      'text': request.POST['text'],
      'reference_picture': request.POST['reference_picture'],
      'google_form_link': request.POST['google_form_link'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:

      if context['social_media'] == 'ig':
        response = draft.ig(line_user_id=line_user_id, context=context)
      else:
        response = draft.ig_fb(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/30_draft.html')


# 4.1 ส่งดราฟแล้ว (Sent Draft)
@login_required(login_url='/api/login/')
def main_sent_draft(request):
  if request.method == 'POST':
    context = {
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:

      response = sent_draft.all_social(line_user_id=line_user_id)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/41_sent_draft.html')


# 4.2 แก้ไขดราฟ (Revise Draft)
@login_required(login_url='/api/login/')
def main_revise_draft(request):
  if request.method == 'POST':
    context = {
      'sent_date': request.POST['sent_date'],
      'comment_story': request.POST['comment_story'],
      'comment_post': request.POST['comment_post'],
      'campaign_name': request.POST['campaign_name'],
      'social_media': request.POST['social_media'],
      'work_type': request.POST['work_type'],
      'work_type_text': request.POST['work_type_text'],
      'post_count': request.POST['post_count'],
      'reference_picture': request.POST['reference_picture'],
      'google_form_link': request.POST['google_form_link'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      if context['social_media'] == 'ig':
        response = revise_draft.ig(line_user_id=line_user_id, context=context)
      else:
        response = revise_draft.ig_fb(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/42_revise_draft.html')


# 4.3 อนุมัติดราฟ (Approve Draft)
@login_required(login_url='/api/login/')
def main_approve_draft(request):
  if request.method == 'POST':
    context = {
      'sent_date': request.POST['sent_date'],
      'campaign_name': request.POST['campaign_name'],
      'social_media': request.POST['social_media'],
      'work_type': request.POST['work_type'],
      'work_type_text': request.POST['work_type_text'],
      'post_count': request.POST['post_count'],
      'reference_picture': request.POST['reference_picture'],
      'google_form_link': request.POST['google_form_link'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      if context['social_media'] == 'ig':
        response = approve_draft.ig(line_user_id=line_user_id, context=context)
      else:
        response = approve_draft.ig_fb(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/43_approve_draft.html')


# 5. ส่งงานแล้ว (Sent Work)
@login_required(login_url='/api/login/')
def main_sent_work(request):
  if request.method == 'POST':
    context = {
      'sent_date': request.POST['sent_date'],
      'campaign_name': request.POST['campaign_name'],
      'google_form_link': request.POST['google_form_link'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      response = sent_work.all_social(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/50_sent_work.html')


# 6. รอตรวจสอบงาน (Wait For Check Work)
@login_required(login_url='/api/login/')
def main_wait_check_work(request):
  if request.method == 'POST':
    context = {
      'campaign_name': request.POST['campaign_name'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      response = wait_check_work.all_social(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/60_wait_check_work.html')


# 7. เสร็จสิ้น
@login_required(login_url='/api/login/')
def main_finish(request):
  if request.method == 'POST':
    context = {
      'campaign_name': request.POST['campaign_name'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      response = finish.all_social(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/70_finish.html')


# 8. ชำระเงินเรียบร้อย
@login_required(login_url='/api/login/')
def main_payment(request):
  if request.method == 'POST':
    context = {
      'campaign_name': request.POST['campaign_name'],
      'name': request.POST['name'],
      'price': request.POST['price'],
      'payment_date': request.POST['payment_date'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      response = payment.all_social(line_user_id=line_user_id, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/main/80_payment.html')


# 1. Reject Work
@login_required(login_url='/api/login/')
def add_reject_work(request):
  if request.method == 'POST':
    context = {
      'campaign_name': request.POST['campaign_name'],
      'campaign_picture': request.POST['campaign_picture'],
      'social_media': request.POST['social_media'],
      'work_type': request.POST['work_type'],
      'price': request.POST['price'],
      'work_type_text': request.POST['work_type_text'],
      'post_count': request.POST['post_count'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      shouter = Shouter.objects.filter(line_user_id=line_user_id).first()

      # IG Only
      if context['social_media'] == 'ig' and context['work_type'] == 'story' and context['price'] == 'min':
        price = shouter.ig_price_story_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story' and context['price'] == 'max':
        price = shouter.ig_price_story_ugc
      elif context['social_media'] == 'ig' and context['work_type'] == 'post' and context['price'] == 'min':
        price = shouter.ig_price_post_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'post' and context['price'] == 'max':
        price = shouter.ig_price_post_ugc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story_post' and context['price'] == 'min':
        price = shouter.ig_price_story_post_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story_post' and context['price'] == 'max':
        price = shouter.ig_price_story_post_ugc

      # IG + FB
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story' and context['price'] == 'min':
        price = shouter.ig_fb_price_story_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story' and context['price'] == 'max':
        price = shouter.ig_fb_price_story_ugc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'post' and context['price'] == 'min':
        price = shouter.ig_fb_price_post_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'post' and context['price'] == 'max':
        price = shouter.ig_fb_price_post_ugc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story_post' and context['price'] == 'min':
        price = shouter.ig_fb_price_story_post_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story_post' and context['price'] == 'max':
        price = shouter.ig_fb_price_story_post_ugc
      else:
        failed_id.append(line_user_id)
        continue

      if context['social_media'] == 'ig':
        response = reject_work.ig(line_user_id=line_user_id, price=price, context=context)
      else:
        response = reject_work.ig_fb(line_user_id=line_user_id, price=price, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/add/10_reject_work.html')


# 2. Cancel Work
@login_required(login_url='/api/login/')
def add_cancel_work(request):
  if request.method == 'POST':
    context = {
      'campaign_name': request.POST['campaign_name'],
      'campaign_picture': request.POST['campaign_picture'],
      'social_media': request.POST['social_media'],
      'work_type': request.POST['work_type'],
      'price': request.POST['price'],
      'work_type_text': request.POST['work_type_text'],
      'post_count': request.POST['post_count'],
      'list_line_user_id': request.POST['list_line_user_id'],
    }

    # Sent Flex
    success_id = []
    failed_id = []
    if "," in context['list_line_user_id']:
      list_line_user_id = context['list_line_user_id'].split(",")
    else:
      list_line_user_id = [context['list_line_user_id']]
    for line_user_id in list_line_user_id:
      shouter = Shouter.objects.filter(line_user_id=line_user_id).first()

      # IG Only
      if context['social_media'] == 'ig' and context['work_type'] == 'story' and context['price'] == 'min':
        price = shouter.ig_price_story_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story' and context['price'] == 'max':
        price = shouter.ig_price_story_ugc
      elif context['social_media'] == 'ig' and context['work_type'] == 'post' and context['price'] == 'min':
        price = shouter.ig_price_post_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'post' and context['price'] == 'max':
        price = shouter.ig_price_post_ugc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story_post' and context['price'] == 'min':
        price = shouter.ig_price_story_post_fc
      elif context['social_media'] == 'ig' and context['work_type'] == 'story_post' and context['price'] == 'max':
        price = shouter.ig_price_story_post_ugc

      # IG + FB
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story' and context['price'] == 'min':
        price = shouter.ig_fb_price_story_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story' and context['price'] == 'max':
        price = shouter.ig_fb_price_story_ugc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'post' and context['price'] == 'min':
        price = shouter.ig_fb_price_post_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'post' and context['price'] == 'max':
        price = shouter.ig_fb_price_post_ugc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story_post' and context['price'] == 'min':
        price = shouter.ig_fb_price_story_post_fc
      elif context['social_media'] == 'ig_fb' and context['work_type'] == 'story_post' and context['price'] == 'max':
        price = shouter.ig_fb_price_story_post_ugc
      else:
        failed_id.append(line_user_id)
        continue

      if context['social_media'] == 'ig':
        response = cancel_work.ig(line_user_id=line_user_id, price=price, context=context)
      else:
        response = cancel_work.ig_fb(line_user_id=line_user_id, price=price, context=context)

      if not response:
        failed_id.append(line_user_id)
        continue

      success_id.append(line_user_id)

    context = {
      'success_id': success_id,
      'failed_id': failed_id
    }
    return render(request, 'api/flex/result.html', context=context)

  return render(request, 'api/flex/add/20_cancel_work.html')


# 3. Reconnect IG
@login_required(login_url='/api/login/')
def add_reconnect(request):
  return render(request, 'api/flex/add/30_reconnect.html')


# Upload Campaign Detail Logo
@login_required(login_url='/api/login/')
def upload_campaign_detail_logo(request):
  if request.method == "POST":
    request_file = request.FILES["logo_file"] if "logo_file" in request.FILES else False
    filename = request.POST["filename"]

    if request_file:
      default_name = request_file.name
      ext = default_name.split(".", 1)[1]

      fs = FileSystemStorage()
      file = fs.save("flex/logo/" + filename + "." + ext, request_file)
      file_url = fs.url(file)
      context = {
        "file_url": "https://www.shoutsolution.com" + file_url
      }

      return render(request, 'api/upload/result.html', context=context)

  return render(request, 'api/upload/campaign_detail_logo.html')


# Upload Campaign Detail Reference
@login_required(login_url='/api/login/')
def upload_campaign_detail_reference(request):
  if request.method == "POST":
    request_file = request.FILES["reference_file"] if "reference_file" in request.FILES else False
    filename = request.POST["filename"]

    if request_file:
      default_name = request_file.name
      ext = default_name.split(".", 1)[1]

      fs = FileSystemStorage()
      file = fs.save("flex/reference/" + filename + "." + ext, request_file)
      file_url = fs.url(file)
      context = {
        "file_url": "https://www.shoutsolution.com" + file_url
      }

      return render(request, 'api/upload/result.html', context=context)

  return render(request, 'api/upload/campaign_detail_reference.html')


@login_required(login_url='/api/login/')
def insights_story(request):
  if request.method == "POST":
    url = request.POST['url']
    ig_username = request.POST['ig_username']

    shouter = Shouter.objects.filter(ig_username=ig_username).first()
    business_account_id = shouter.ig_business_account_id
    access_token = shouter.fb_main_access_token

    # Find Story ID
    context_list = get_story_list(business_account_id, access_token)
    if not context_list:
      return render(request, 'api/insights/insights_story.html')
    story_list = context_list['data']

    # For Loop
    story_id = get_story_id(story_list, access_token, url)
    if not story_id:
      return render(request, 'api/insights/insights_story.html')

    # Get Insights
    insight = get_story_insights(story_id, access_token)

    context = {}

    for obj in insight:
      context[obj['name']] = obj['values'][0]['value']

    return render(request, 'api/insights/insights_story.html', context)

  return render(request, 'api/insights/insights_story.html')


@login_required(login_url='/api/login')
def insights_post(request):
  if request.method == "POST":
    url = request.POST['url']
    ig_username = request.POST['ig_username']

    shouter = Shouter.objects.filter(ig_username=ig_username).first()
    business_account_id = shouter.ig_business_account_id
    access_token = shouter.fb_main_access_token

    # Find Post ID
    context_list = get_post_list(business_account_id, access_token)
    if not context_list:
      return render(request, 'api/insights/insights_post.html')
    post_list = context_list['data']['data']

    # For loop
    post_id, like_count, comments_count = get_post_id(post_list, access_token, url)
    if not post_id:
      return render(request, 'api/insights/insights_post.html')

    # Get Insights
    insight = get_post_insights(post_id, access_token)

    context = {
      'like_count': like_count,
      'comments_count': comments_count
    }

    for obj in insight:
      context[obj['name']] = obj['values'][0]['value']

    return render(request, 'api/insights/insights_post.html', context)

  return render(request, 'api/insights/insights_post.html')
