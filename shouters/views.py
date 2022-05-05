from django.utils.timezone import now
from django.shortcuts import render, redirect, HttpResponse
from django.middleware import csrf
from django.core.files.storage import FileSystemStorage

from shouters.shouter_interests import shouter_interest
from shouters.models import Shouter

from shouters.lists import thailand_province, date_lists, month_lists, year_lists, education_lists, banking_lists
from shouters.lineMessagingApi.lineMessagingApi import LineApiMessage

# Import Own Utils
from .utils import error, jwt_token, media
from .utils.function import fn_work_selection, fn_ad_gaurantee_reach, fn_round_to_five
from .utils.facebook import fb_api_authentication, fb_api_bio, fb_api_permissions, fb_api_page_id
from .utils.instagram import ig_api_engagement, ig_api_active_follower, ig_api_business_account_id, ig_api_bio, ig_api_media_objects, ig_api_audience_insight
from .utils.line import line_api_authentication, line_api_bio
from .utils.predicted import predicted_post_reach, predicted_story_view
from .utils.pricing.calculate_price import IGStoryFc, IGStoryUgc, IGPostFc, IGPostUgc


# Create your views here.
def landing_page(request):
  return render(request, 'shouters/landing.html')


def waiting_for_approve(request):
  return render(request, 'shouters/wfa.html')


def not_found_user(request):
  return render(request, 'error/not_found_shouters.html')


def register__info_1(request, token):
  context = {
      'token': token
  }
  return render(request, 'shouters/register__info-1.html', context=context)


def register__info_2(request, token):
  context = {
      'token': token
  }
  return render(request, 'shouters/register__info-2.html', context=context)


def register__connect_facebook_error_1(request, token):
  context = {
    'token': token
  }
  return render(request, 'shouters/register__connect-fb-error-1.html', context=context)


def register__connect_facebook_error_2(request, token):
  context = {
    'token': token
  }
  return render(request, 'shouters/register__connect-fb-error-2.html', context=context)


def register__connect_facebook_change(request, token):
  context = {
    'token': token
  }
  return render(request, 'shouters/register__connect-fb-change.html', context=context)


def register__choose_device(request, token):
  context = {
      'token': token
  }
  return render(request, 'shouters/register__choose-device.html', context=context)

def register__facebook_checkbox(request, token):
  context = {
      'token': token
  }
  return render(request, 'shouters/register__facebook-checkbox.html', context=context)


def register(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    print(_id)
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  context = {
    'token': token,
    'line_profile_picture': shouter.line_profile_picture,
    'thailand_provinces': thailand_province(),
    'date_lists': date_lists,
    'month_lists': month_lists,
    'year_lists': year_lists,
    'education_lists': education_lists
  }

  if request.method == 'POST':
    # Get User information
    try:
      nickname = request.POST['nickname']
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      email = request.POST['email']
      tel = request.POST['tel']
      gender = request.POST['gender']
      birthday_date = request.POST['birthday_date']
      birthday_month = request.POST['birthday_month']
      birthday_year = request.POST['birthday_year']
      province = request.POST['province']
      education = request.POST['education']
      college = request.POST['college']
      interest = request.POST.getlist('interest')
    except KeyError:
      context = {
        'warning': 'Please Fulfill the information',
        'token': token,
        'line_profile_picture': shouter.line_profile_picture,
        'thailand_provinces': thailand_province(),
        'date_lists': date_lists,
        'month_lists': month_lists,
        'year_lists': year_lists,
        'education_lists': education_lists
      }
      return render(request, 'shouters/register.html', context=context)

    # Save to database
    shouter.nickname = nickname
    shouter.first_name = first_name
    shouter.last_name = last_name
    shouter.email = email
    shouter.tel = tel
    shouter.gender = gender
    shouter.birthday_date = birthday_date
    shouter.birthday_month = birthday_month
    shouter.birthday_year = birthday_year
    shouter.province = province
    shouter.education = education
    shouter.college = college
    shouter.interest = interest
    shouter.is_register = True
    shouter.save()

    redirect_url = '/shouters/register/info-2/{}/'.format(token)
    return redirect(redirect_url)

  return render(request, 'shouters/register.html', context=context)


def register__choose_instagram(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except KeyError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  if request.method == 'POST':
    encoded_token = request.POST['instagram']
    redirect_url = '/shouters/register/ig-api/{}/'.format(encoded_token)
    return redirect(redirect_url)

  context = {
    'shouter': shouter,
    'token': token,
  }
  return render(request, 'shouters/register__choose_instagram.html', context=context)


def register__account_summary(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except KeyError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  interest_list = shouter.interest
  interest = shouter_interest(interest_list=interest_list)

  context = {
    'shouter': shouter,
    'interest': interest,
    'token': token,
  }
  return render(request, 'shouters/register__account-summary.html', context)


def register__work_selection(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except KeyError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  context = {
    'shouter': shouter,
    # Token
    'token': token,
  }

  if request.method == 'POST':
    # IG Only
    is_check_ig = request.POST.getlist('is_check_ig')
    if is_check_ig:
      shouter.is_check_ig = True
      # Story
      is_check_ig_story = request.POST.getlist('is_check_ig_story')
      is_check_ig_story = fn_work_selection.is_check(is_check_ig_story)
      # Post
      is_check_ig_post = request.POST.getlist('is_check_ig_post')
      is_check_ig_post = fn_work_selection.is_check(is_check_ig_post)
      # Story + Post
      is_check_ig_story_post = request.POST.getlist('is_check_ig_story_post')
      is_check_ig_story_post = fn_work_selection.is_check(is_check_ig_story_post)
      # If not check all => is_check_main = False
      if not is_check_ig_story and not is_check_ig_post and not is_check_ig_story_post:
        shouter.is_check_ig = False
      shouter.is_check_ig_story = is_check_ig_story
      shouter.is_check_ig_post = is_check_ig_post
      shouter.is_check_ig_story_post = is_check_ig_story_post
    else:
      shouter.is_check_ig = False
      shouter.is_check_ig_story = False
      shouter.is_check_ig_post = False
      shouter.is_check_ig_story_post = False

    # IG + FB
    is_check_ig_fb = request.POST.getlist('is_check_ig_fb')
    if is_check_ig_fb:
      shouter.is_check_ig_fb = True
      # Story
      is_check_ig_fb_story = request.POST.getlist('is_check_ig_fb_story')
      is_check_ig_fb_story = fn_work_selection.is_check(is_check_ig_fb_story)
      # Post
      is_check_ig_fb_post = request.POST.getlist('is_check_ig_fb_post')
      is_check_ig_fb_post = fn_work_selection.is_check(is_check_ig_fb_post)
      # Story + Post
      is_check_ig_fb_story_post = request.POST.getlist('is_check_ig_fb_story_post')
      is_check_ig_fb_story_post = fn_work_selection.is_check(is_check_ig_fb_story_post)
      # If not check all => is_check_main = False
      if not is_check_ig_fb_story and not is_check_ig_fb_post and not is_check_ig_fb_story_post:
        shouter.is_check_ig_fb = False
      shouter.is_check_ig_fb_story = is_check_ig_fb_story
      shouter.is_check_ig_fb_post = is_check_ig_fb_post
      shouter.is_check_ig_fb_story_post = is_check_ig_fb_story_post
    else:
      shouter.is_check_ig_fb = False
      shouter.is_check_ig_fb_story = False
      shouter.is_check_ig_fb_post = False
      shouter.is_check_ig_fb_story_post = False

    # Tiktok
    is_check_tiktok = request.POST.getlist('is_check_tiktok')
    if len(is_check_tiktok) != 0:
      try:
        tiktok_name = request.POST['tiktok_name']
        tiktok_price = request.POST['tiktok_price']
      except ValueError:
        shouter.is_check_tiktok = False
        tiktok_name = None
        tiktok_price = None
      if tiktok_name == '' or tiktok_price == '':
        shouter.is_check_tiktok = False
        shouter.tiktok_name = None
        shouter.tiktok_price = None
      else:
        shouter.is_check_tiktok = True
        shouter.tiktok_name = tiktok_name
        shouter.tiktok_price = tiktok_price
    else:
      shouter.is_check_tiktok = False
      shouter.tiktok_name = None
      shouter.tiktok_price = None

    # Twitter
    is_check_twitter = request.POST.getlist('is_check_twitter')
    if len(is_check_twitter) != 0:
      try:
        twitter_name = request.POST['twitter_name']
        twitter_price = request.POST['twitter_price']
      except ValueError:
        shouter.is_check_twitter = False
        twitter_name = None
        twitter_price = None
      if twitter_name == '' or twitter_price == '':
        shouter.is_check_twitter = False
        shouter.twitter_name = None
        shouter.twitter_price = None
      else:
        shouter.is_check_twitter = True
        shouter.twitter_name = twitter_name
        shouter.twitter_price = twitter_price
    else:
      shouter.is_check_twitter = False
      shouter.twitter_name = None
      shouter.twitter_price = None

    shouter.save()
    redirect_url = '/shouters/register/account-summary/{}/'.format(token)
    return redirect(redirect_url)

  return render(request, 'shouters/register__work-selection.html', context)


def register__finished(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  shouter.is_finished_regis = True
  shouter.save()
  response_text = LineApiMessage().api__wait_for_approve_text_message(line_user_id=shouter.line_user_id)
  response_flex = LineApiMessage().api__wait_for_approve_flex_message(line_user_id=shouter.line_user_id)

  context = {
    'token': token
  }
  return render(request, 'shouters/register__finished.html', context=context)


def line_login(request):
  # /shouters/line-login?q=register/
  # /shouters/line-login?q=work_management/
  # /shouters/line-login?q=payment/
  # /shouters/line-login?q=shouter_history/
  csrf_token = csrf.get_token(request)
  q = request.GET.get('q', None)
  state = {
    'token': csrf_token,
    'q': q,
  }
  line_login_url = line_api_authentication.line_auth(state=state)
  return redirect(line_login_url)


def oauth(request):
  # Get Code
  code = request.GET.get('code')
  # Get State of Request (query string)
  # Get Query String => to check which page to redirect
  state = request.GET.get('state')
  list_state = state.split(',')
  q = list_state[1]

  # Get Access Token
  context__line_authentication = line_api_authentication.get(code)
  if not context__line_authentication:
    # Return Login Line Page Failed
    return HttpResponse('Log in line failed')
  # Get Data
  access_token = context__line_authentication['access_token']
  id_token = context__line_authentication['id_token']

  # Get User Information
  context__line_bio = line_api_bio.get(id_token)
  if not context__line_bio:
    # Return Login Line Page Failed
    return HttpResponse('Failed to get User Information / ไม่เปิดให้เก็บข้อมูล')
  # Get Data
  line_user_id = context__line_bio['line_user_id']
  line_username = context__line_bio['line_username']
  line_profile_picture = context__line_bio['line_profile_picture']

  # Save to Shouter Database
  if Shouter.objects.filter(line_user_id=line_user_id).exists():
    shouter = Shouter.objects.filter(line_user_id=line_user_id).first()
    line_access_token = shouter.line_access_token
    line_id_token = shouter.line_id_token
    if line_access_token != access_token:
        shouter.line_access_token = access_token
        shouter.line_access_token_updated = now()
    if line_id_token != id_token:
        shouter.line_id_token = id_token
        shouter.line_id_token_updated = now()
    shouter.save()

    # if user_id exist in the model => check by case
    _id = shouter.id
    # JWT ENCODED
    token = jwt_token.encode(data={}, _id=_id)

    # If shouter is not register in registration page => redirect to registration page info
    if not shouter.is_register:
      redirect_url = '/shouters/register/info-1/{}/'.format(token)
    else:
      # If shouter is already register in registration page but not connect to FB => redirect to connect to FB Page
      if not shouter.fb_is_connect:
        redirect_url = '/shouters/register/info-2/{}/'.format(token)
      # If shouter is already register in registration page but not choose work selection => redirect to work-selection page
      elif not shouter.is_finished_regis:
        redirect_url = '/shouters/register/work-selection/{}/'.format(token)
      else:
        # /shouters/line-login?q=register/
        # /shouters/line-login?q=work_management/
        # /shouters/line-login?q=payment/
        # /shouters/line-login?q=shouter_history/
        if "bank-account" in q:
          redirect_url = '/shouters/menu/bank-account/{}/'.format(token)
        elif "campaign" in q:
          redirect_url = '/shouters/campaign/{}/'.format(token)
        elif "payment" in q:
          redirect_url = '/shouters/payment/{}/'.format(token)
        elif "social" in q:
          redirect_url = '/shouters/menu/social-media/{}/'.format(token)
        else:
          redirect_url = '/shouters/menu/{}/'.format(token)

  else:
    # Create new one
    shouter = Shouter.objects.create(
      line_access_token=access_token,
      line_access_token_updated=now(),
      line_id_token=id_token,
      line_id_token_updated=now(),
      line_user_id=line_user_id,
      line_username=line_username,
      line_profile_picture=line_profile_picture,
    )
    shouter.save()

    shouter = Shouter.objects.filter(line_user_id=line_user_id).first()
    _id = shouter.id

    # JWT ENCODED
    token = jwt_token.encode(data={}, _id=_id)
    # if user_id not exist in the model and is_connect_ig = False -> go to registration form -> redirect to register
    redirect_url = '/shouters/register/info-1/{}/'.format(token)

  return redirect(redirect_url)


def facebook_login(request, token):
  csrf_token = csrf.get_token(request)
  state = {
    'csrf_token': csrf_token,
    'token': token
  }
  fb_login_url = fb_api_authentication.fb_auth(state=state)
  return redirect(fb_login_url)


def facebook_logout(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')
  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  access_token = shouter.fb_main_access_token
  logout_status = fb_api_permissions.delete(access_token)
  if not logout_status:
    return HttpResponse('Failed')
  shouter.fb_is_connect = False
  shouter.save()
  redirect_url = '/shouters/menu/social-media/{}/'.format(token)

  return redirect(redirect_url)


def oauth2(request):
  # Get Code
  code = request.GET.get('code')
  # Get Status (New or Exist)
  # Get JWT Token
  state = request.GET.get('state')
  list_state = state.split(',')
  # Get q (query string)
  token = list_state[1]
  token = token[11:-2]

  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  context = {
    'token': token
  }
  # Get Access Token
  access_token = fb_api_authentication.get(code)
  if not access_token:
    # แก้เป็นหน้าให้เปลี่ยน FB with default browser
    error.log(shouter, 'ไม่สามารถเก็บ Token จาก shouter ได้ => shouter กดปิดไประหว่างการ login (ต้องการเปลี่ยน FB หรือเปล่า?)')
    redirect_url = '/shouters/register/facebook-change/{}/'.format(token)
    return redirect(redirect_url)
  # Save to database
  shouter.fb_main_access_token = access_token
  shouter.save()

  # Get Facebook Page ID
  context__page_id = fb_api_page_id.get(access_token)
  if not context__page_id:
    redirect_url = '/shouters/register/facebook-error-1/{}/'.format(token)
    return redirect(redirect_url)
  objs = context__page_id['objs']
  is_found = False
  if objs:
    list_obj = []
    for obj in objs:
      page_name = obj['name']
      page_id = obj['id']

      # Get Instagram Business ID
      context__business_account_id = ig_api_business_account_id.get(page_id=page_id, access_token=access_token)
      if not context__business_account_id:
        continue
      business_account_id = context__business_account_id['business_account_id']
      is_found = True

      # Get Facebook Biography
      context__fb_biography = fb_api_bio.get(access_token)
      if not context__fb_biography:
        redirect_url = '/shouters/register/facebook-error-1/{}/'.format(token)
        return redirect(redirect_url)
      fb_name = context__fb_biography['fb_name']
      fb_profile_picture = context__fb_biography['fb_profile_picture']

      # Get Instagram Biography
      context__ig_biography = ig_api_bio.get(business_account_id=business_account_id, access_token=access_token)
      if not context__ig_biography:
        redirect_url = '/shouters/register/facebook-error-1/{}/'.format(token)
        return redirect(redirect_url)
      ig_username = context__ig_biography['username']
      ig_media_count = context__ig_biography['media_count']
      ig_follower_count = context__ig_biography['followers_count']
      ig_following_count = context__ig_biography['followings_count']
      ig_profile_picture = context__ig_biography['ig_profile_picture']

      data = {
        'access_token': access_token,
        'page_name': page_name,
        'page_id': page_id,
        'fb_name': fb_name,
        'fb_profile_picture': fb_profile_picture,
        'ig_business_account_id': business_account_id,
        'ig_username': ig_username,
        'ig_media_count': ig_media_count,
        'ig_follower_count': ig_follower_count,
        'ig_following_count': ig_following_count,
        'ig_profile_picture': ig_profile_picture,
      }
      encoded_token = jwt_token.encode(data, _id, state)

      # context 1 ig
      data = {
        'page_name': page_name,
        'fb_name': fb_name,
        'ig_username': ig_username,
        'ig_follower_count': ig_follower_count,
        'ig_following_count': ig_following_count,
        'ig_profile_picture': ig_profile_picture,
        'encoded_token': encoded_token,
      }
      list_obj.append(data)

    context = {
      'list_obj': list_obj,
      'token': token,
    }

    # Check user give all Permission
    permissions = fb_api_permissions.get(access_token)
    if not permissions:
      # Return To Recheck Permission
      redirect_url = '/shouters/register/facebook-error-1/{}/'.format(token)
      return redirect(redirect_url)
    count = 0
    for data in permissions['permissions']:
      if data['status'] == "granted":
        count += 1
      else:
        continue
    if count < 5:
      # Return To Recheck Permission
      redirect_url = '/shouters/register/facebook-error-1/{}/'.format(token)
      return redirect(redirect_url)

    if is_found:
      return render(request, 'shouters/register__choose_instagram.html', context)
    else:
      redirect_url = '/shouters/register/facebook-error-1/{}/'.format(token)
      return redirect(redirect_url)

  redirect_url = '/shouters/register/facebook-error-1/{}/'.format(token)
  return redirect(redirect_url)


def register__get_ig_data(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    access_token = decoded_token['access_token']
    fb_page_name = decoded_token['page_name']
    fb_page_id = decoded_token['page_id']
    fb_name = decoded_token['fb_name']
    fb_profile_picture = decoded_token['fb_profile_picture']
    ig_business_account_id = decoded_token['ig_business_account_id']
    ig_username = decoded_token['ig_username']
    ig_media_count = decoded_token['ig_media_count']
    ig_follower_count = decoded_token['ig_follower_count']
    ig_following_count = decoded_token['ig_following_count']
    ig_profile_picture = decoded_token['ig_profile_picture']
    pass
  except KeyError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  # Go to Not Found Shouter
  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user', token)

  shouter = Shouter.objects.filter(id=_id).first()
  # Get Info
  shouter.fb_access_token_created = now()
  shouter.fb_page_name = fb_page_name
  shouter.fb_page_id = fb_page_id
  shouter.fb_name = fb_name
  shouter.fb_profile_picture = fb_profile_picture
  shouter.ig_business_account_id = ig_business_account_id
  shouter.ig_username = ig_username
  shouter.ig_media_count = ig_media_count
  shouter.ig_follower_count = ig_follower_count
  shouter.ig_following_count = ig_following_count
  shouter.ig_profile_picture = ig_profile_picture
  shouter.save()

  ##########################################################################################################################
  # Get Instagram Active Follower
  if ig_follower_count == 0:
    ig_follower_count = 1
  context__active_follower = ig_api_active_follower.get(business_account_id=ig_business_account_id, access_token=access_token, followers_count=ig_follower_count)
  if not context__active_follower:
    error.log(shouter, 'ไม่สามารถเก็บ IG Active Follower ได้')
    return HttpResponse('IG Active Follower Failed')
  shouter.ig_response_active_follower = context__active_follower['data']
  shouter.ig_active_follower = context__active_follower['geometric_active_follower']
  shouter.ig_active_follower_harmonic = context__active_follower['harmonic_active_follower']
  shouter.ig_active_follower_percent = context__active_follower['ig_active_follower_percent']
  shouter.save()
  ##########################################################################################################################

  ##########################################################################################################################
  # Get Media Objects => Return ค่าออกมา 3 อย่าง คือ ig_average_total_like, ig_story_view, ig_average_post_reach
  context__media_objects = ig_api_media_objects.get(business_account_id=ig_business_account_id, access_token=access_token)
  try:
    ig_response_media_objects = context__media_objects['data']
    media_objects = context__media_objects['media_objects']
  except KeyError:
    ig_response_media_objects = {}
    media_objects = []
  if not context__media_objects or len(media_objects) == 0:
    ig_average_total_like = 0
    ig_story_view = 0
    ig_average_post_reach = 0
    ig_reach_source = 'no media'
    # error.log(shouter, 'ไม่สามารถเก็บ Post Reach ของ user ได้')
  else:
    # context__like_engagement return เป็น dict => dict['list_like'] = list และ dict['mean'] = average like after cut outlier
    context__like_engagement = ig_api_engagement.get_like(media_objects=media_objects, access_token=access_token)
    # return =>
    # {
    #   'final_dict': [{id: like_count}, ... ],
    #   'ig_average_total_like' : ...
    # }
    # if no final dict => context__like_engagement return False
    if not context__like_engagement:
      ig_average_total_like = 0
      ig_story_view = 0
      ig_average_post_reach = 0
      ig_reach_source = 'all media like < 10'
    else:
      # AVERAGE LIKE & STORY VIEW
      final_dict = context__like_engagement['final_dict']
      ig_average_total_like = context__like_engagement['ig_average_total_like']
      ig_story_view = predicted_story_view.get(ig_follower_count=ig_follower_count, ig_average_total_like=ig_average_total_like)

      # เก็บ POST REACH เพื่อดูว่าเก็บไก้มากกว่า 3 ไหม
      context__post_reach = ig_api_engagement.get_reach(final_dict=final_dict, access_token=access_token)
      if 'ig_average_post_reach' in context__post_reach.keys():
        reach_list = context__post_reach['reach_list']
        # Media < 3 -> like = average, story_view = 0, post_reach = 0
        if len(media_objects) < 3 or len(reach_list) < 3:
          ig_average_post_reach = predicted_post_reach.get(ig_average_total_like=ig_average_total_like, ig_story_view=ig_story_view)
          ig_reach_source = 'predicted'
        else:
          # AVERAGE POST REACH
          ig_average_post_reach = context__post_reach['ig_average_post_reach']
          ig_reach_source = 'api'
      else:
        ig_average_post_reach = predicted_post_reach.get(ig_average_total_like=ig_average_total_like, ig_story_view=ig_story_view)
        ig_reach_source = 'predicted'
  ##########################################################################################################################

  ##########################################################################################################################
  # ANALYSIS => Return ค่า Engagement โดยการนำค่า 3 ค่าที่ได้จากก่อนหน้ามาคำนวน
  ig_engagement_percent = (ig_average_total_like / ig_follower_count) * 100
  ig_engagement_percent = round(ig_engagement_percent, 2)

  shouter.ig_response_media_objects = ig_response_media_objects
  shouter.ig_average_total_like = ig_average_total_like
  shouter.ig_engagement_percent = ig_engagement_percent
  shouter.ig_story_view = ig_story_view
  shouter.ig_average_post_reach = ig_average_post_reach
  shouter.ig_reach_source = ig_reach_source
  shouter.save()

  # Cal AD and Guarantee Reach
  context__ad_gaurantee = fn_ad_gaurantee_reach.get(ig_story_view=ig_story_view, ig_average_post_reach=ig_average_post_reach)
  shouter.ig_predicted_ad_post_reach = context__ad_gaurantee['ig_predicted_ad_post_reach']
  shouter.ig_post_reach_guarantee = context__ad_gaurantee['ig_post_reach_guarantee']
  shouter.ig_story_view_guarantee = context__ad_gaurantee['ig_story_view_guarantee']
  shouter.ig_ad_post_reach = ig_ad_post_reach = context__ad_gaurantee['ig_ad_post_reach']
  shouter.save()

  # Cal Price
  # instagram story + post
  ig_price_story_fc = fn_round_to_five.get(IGStoryFc().cal_price(ig_story_view))
  ig_price_story_ugc = fn_round_to_five.get(IGStoryUgc().cal_price(ig_story_view))
  ig_price_post_fc = fn_round_to_five.get(IGPostFc().cal_price(ig_ad_post_reach))
  ig_price_post_ugc = fn_round_to_five.get(IGPostUgc().cal_price(ig_ad_post_reach))
  ig_price_story_post_fc = (ig_price_story_fc + ig_price_post_fc) * 0.9
  ig_price_story_post_ugc = (ig_price_story_ugc + ig_price_post_ugc) * 0.9
  shouter.ig_price_story_fc = ig_price_story_fc
  shouter.ig_price_story_ugc = ig_price_story_ugc
  shouter.ig_price_post_fc = ig_price_post_fc
  shouter.ig_price_post_ugc = ig_price_post_ugc
  shouter.ig_price_story_post_fc = fn_round_to_five.get(ig_price_story_post_fc)
  shouter.ig_price_story_post_ugc = fn_round_to_five.get(ig_price_story_post_ugc)
  # facebook story + post
  shouter.ig_fb_price_story_fc = fn_round_to_five.get(ig_price_story_fc * 1.1)
  shouter.ig_fb_price_story_ugc = fn_round_to_five.get(ig_price_story_ugc * 1.1)
  shouter.ig_fb_price_post_fc = fn_round_to_five.get(ig_price_post_fc * 1.1)
  shouter.ig_fb_price_post_ugc = fn_round_to_five.get(ig_price_post_ugc * 1.1)
  shouter.ig_fb_price_story_post_fc = fn_round_to_five.get(ig_price_story_post_fc * 1.1)
  shouter.ig_fb_price_story_post_ugc = fn_round_to_five.get(ig_price_story_post_ugc * 1.1)
  shouter.save()
  ##########################################################################################################################

  ##########################################################################################################################
  # IG INSIGHT
  shouter.ig_response_audience_insight = ig_api_audience_insight.get(business_account_id=ig_business_account_id, access_token=access_token)
  ##########################################################################################################################
  shouter.fb_is_connect = True
  shouter.save()
  ##########################################################################################################################

  # If shouter is already connect to facebook => redirect to social_media page
  if not shouter.is_finished_regis:
    redirect_url = '/shouters/register/work-selection/{}/'.format(token)
  else:
    redirect_url = '/shouters/menu/social-media/{}/'.format(token)
  return redirect(redirect_url)


def menu(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  context = {
    'shouter': shouter,
    'token': token,
  }
  return render(request, 'shouters/menu.html', context)


def menu__social_media(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  context = {
    'shouter': shouter,
    'token': token,
  }
  return render(request, 'shouters/menu__social-media.html', context)


def menu__bank_account(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  context = {
      'banking_lists': banking_lists,
      'shouter': shouter,
      'token': token
  }

  if request.method == 'POST':
    # Import FS
    # max_size = (500, 500)
    fs = FileSystemStorage()
    # Get data from form input
    id_card = request.FILES["id_card"] if "id_card" in request.FILES else False
    book_bank = request.FILES["book_bank"] if "book_bank" in request.FILES else False
    bank_name = request.POST['bank_name']
    bank_username = request.POST['bank_username']
    bank_account_number = request.POST['bank_account_number']
    # Change File name of photo
    if not id_card and not book_bank:
      shouter.bank_name = bank_name
      shouter.bank_username = bank_username
      shouter.bank_account_number = bank_account_number
      shouter.save()
    elif not id_card:
      filename_book_bank = fs.save(media.get_unique_name('book_bank/', book_bank.name, shouter), book_bank)
      shouter.book_bank_photo = filename_book_bank
      shouter.bank_name = bank_name
      shouter.bank_username = bank_username
      shouter.bank_account_number = bank_account_number
      shouter.save()
    elif not book_bank:
      filename_id_card = fs.save(media.get_unique_name('id_card/', id_card.name, shouter), id_card)
      shouter.id_card_photo = filename_id_card
      shouter.bank_name = bank_name
      shouter.bank_username = bank_username
      shouter.bank_account_number = bank_account_number
      shouter.save()
    else:
      # Save Image
      filename_id_card = fs.save(media.get_unique_name('id_card/', id_card.name, shouter), id_card)
      filename_book_bank = fs.save(media.get_unique_name('book_bank/', book_bank.name, shouter), book_bank)
      # Save to Database
      shouter.id_card_photo = filename_id_card
      shouter.book_bank_photo = filename_book_bank
      shouter.bank_name = bank_name
      shouter.bank_username = bank_username
      shouter.bank_account_number = bank_account_number
      shouter.is_connect_bank = True
      shouter.save()

    redirect_url = '/shouters/menu/{}/'.format(token)
    return redirect(redirect_url)

  return render(request, 'shouters/menu__bank-account.html', context=context)


def menu__edit_profile(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  context = {
    'shouter': shouter,
    'thailand_provinces': thailand_province(),
    'date_lists': date_lists,
    'month_lists': month_lists,
    'year_lists': year_lists,
    'education_lists': education_lists,
    'token': token
  }

  if request.method == 'POST':
    # Get User information
    try:
      nickname = request.POST['nickname']
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      email = request.POST['email']
      tel = request.POST['tel']
      gender = request.POST['gender']
      birthday_date = request.POST['birthday_date']
      birthday_month = request.POST['birthday_month']
      birthday_year = request.POST['birthday_year']
      province = request.POST['province']
      education = request.POST['education']
      college = request.POST['college']
      interest = request.POST.getlist('interest')
    except ValueError:
      context = {
        'warning': 'Please Fulfill the information',
        'shouter': shouter,
        'thailand_provinces': thailand_province(),
        'date_lists': date_lists,
        'month_lists': month_lists,
        'year_lists': year_lists,
        'education_lists': education_lists,
        'token': token,
      }
      return render(request, 'shouters/menu__edit-profile.html', context=context)

    # Save to database
    shouter.nickname = nickname
    shouter.first_name = first_name
    shouter.last_name = last_name
    shouter.email = email
    shouter.tel = tel
    shouter.gender = gender
    shouter.birthday_date = birthday_date
    shouter.birthday_month = birthday_month
    shouter.birthday_year = birthday_year
    shouter.province = province
    shouter.education = education
    shouter.college = college
    shouter.interest = interest
    shouter.is_register = True
    shouter.save()

    redirect_url = '/shouters/menu/{}/'.format(token)
    return redirect(redirect_url)

  return render(request, 'shouters/menu__edit-profile.html', context)


def menu__work_selection(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()

  context = {
    'shouter': shouter,
    'token': token,
  }

  if request.method == 'POST':
    # IG Only
    is_check_ig = request.POST.getlist('is_check_ig')
    if is_check_ig:
      shouter.is_check_ig = True
      # Story
      is_check_ig_story = request.POST.getlist('is_check_ig_story')
      is_check_ig_story = fn_work_selection.is_check(is_check_ig_story)
      # Post
      is_check_ig_post = request.POST.getlist('is_check_ig_post')
      is_check_ig_post = fn_work_selection.is_check(is_check_ig_post)
      # Story + Post
      is_check_ig_story_post = request.POST.getlist('is_check_ig_story_post')
      is_check_ig_story_post = fn_work_selection.is_check(is_check_ig_story_post)
      # If not check all => is_check_main = False
      if not is_check_ig_story and not is_check_ig_post and not is_check_ig_story_post:
        shouter.is_check_ig = False
      shouter.is_check_ig_story = is_check_ig_story
      shouter.is_check_ig_post = is_check_ig_post
      shouter.is_check_ig_story_post = is_check_ig_story_post
    else:
      shouter.is_check_ig = False
      shouter.is_check_ig_story = False
      shouter.is_check_ig_post = False
      shouter.is_check_ig_story_post = False

    # IG + FB
    is_check_ig_fb = request.POST.getlist('is_check_ig_fb')
    print(is_check_ig_fb)
    if is_check_ig_fb:
      shouter.is_check_ig_fb = True
      # Story
      is_check_ig_fb_story = request.POST.getlist('is_check_ig_fb_story')
      is_check_ig_fb_story = fn_work_selection.is_check(is_check_ig_fb_story)
      # Post
      is_check_ig_fb_post = request.POST.getlist('is_check_ig_fb_post')
      is_check_ig_fb_post = fn_work_selection.is_check(is_check_ig_fb_post)
      # Story + Post
      is_check_ig_fb_story_post = request.POST.getlist('is_check_ig_fb_story_post')
      is_check_ig_fb_story_post = fn_work_selection.is_check(is_check_ig_fb_story_post)
      # If not check all => is_check_main = False
      if not is_check_ig_fb_story and not is_check_ig_fb_post and not is_check_ig_fb_story_post:
          shouter.is_check_ig_fb = False
      shouter.is_check_ig_fb_story = is_check_ig_fb_story
      shouter.is_check_ig_fb_post = is_check_ig_fb_post
      shouter.is_check_ig_fb_story_post = is_check_ig_fb_story_post
    else:
      shouter.is_check_ig_fb = False
      shouter.is_check_ig_fb_story = False
      shouter.is_check_ig_fb_post = False
      shouter.is_check_ig_fb_story_post = False

    # Tiktok
    is_check_tiktok = request.POST.getlist('is_check_tiktok')
    # print(is_check_tiktok)
    if len(is_check_tiktok) != 0:
      try:
        tiktok_name = request.POST['tiktok_name']
        tiktok_price = request.POST['tiktok_price']
      except ValueError:
        shouter.is_check_tiktok = False
        tiktok_name = None
        tiktok_price = None
      if tiktok_name == '' or tiktok_price == '':
        shouter.is_check_tiktok = False
        shouter.tiktok_name = None
        shouter.tiktok_price = None
      else:
        shouter.is_check_tiktok = True
        shouter.tiktok_name = tiktok_name
        shouter.tiktok_price = tiktok_price
    else:
      shouter.is_check_tiktok = False
      shouter.tiktok_name = None
      shouter.tiktok_price = None

    # Twitter
    is_check_twitter = request.POST.getlist('is_check_twitter')
    if len(is_check_twitter) != 0:
      try:
        twitter_name = request.POST['twitter_name']
        twitter_price = request.POST['twitter_price']
      except ValueError:
        shouter.is_check_twitter = False
        twitter_name = None
        twitter_price = None
      if twitter_name == '' or twitter_price == '':
        shouter.is_check_twitter = False
        shouter.twitter_name = None
        shouter.twitter_price = None
      else:
        shouter.is_check_twitter = True
        shouter.twitter_name = twitter_name
        shouter.twitter_price = twitter_price
    else:
      shouter.is_check_twitter = False
      shouter.twitter_name = None
      shouter.twitter_price = None

    shouter.save()
    redirect_url = '/shouters/menu/{}/'.format(token)
    return redirect(redirect_url)

  return render(request, 'shouters/menu__work-selection.html', context)


def campaign(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token['_id']
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()
  context = {
    'shouter': shouter,
    'token': token,
  }

  return render(request, 'shouters/campaign.html', context)


def payment(request, token):
  try:
    decoded_token = jwt_token.decode(token)
    _id = decoded_token.get('_id')
    pass
  except ValueError:
    # Go to Token Failed Page
    return HttpResponse('Token Failed')

  if not Shouter.objects.filter(id=_id).exists():
    return redirect('shouter__not_fount_user')
  shouter = Shouter.objects.filter(id=_id).first()
  context = {
    'shouter': shouter,
    'token': token,
  }

  return render(request, 'shouters/payment.html', context)
