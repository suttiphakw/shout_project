import jwt
import requests
import datetime
from django.utils.timezone import now
from django.shortcuts import render, redirect, HttpResponse
from django.middleware.csrf import get_token
# from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required

from shouters.utils import LineAPI, FacebookAPI
from shouters.shouter_interests import shouter_interest
from shouters.models import Shouter
# from orders.models import Order

from utils.cal_price import IGStoryFc, IGStoryUgc, IGPostFc, IGPostUgc
from shouters.lists import thailand_province, date_lists, month_lists, year_lists, education_lists
from shouters.lineMessagingApi.lineMessagingApi import LineApiMessage


# Create your views here.
def landing_page(request):
    return render(request, 'shouters/landing.html')


def waiting_for_approve(request):
    return render(request, 'shouters/wfa.html')


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


def register__info_3(request, token):
    context = {
        'token': token
    }
    return render(request, 'shouters/register__info-3.html', context=context)


def register__info_4(request, token):
    context = {
        'token': token
    }
    return render(request, 'shouters/register__info-4.html', context=context)


def register__info_5(request, token):
    context = {
        'token': token
    }
    return render(request, 'shouters/register__info-5.html', context=context)


def register__info_6(request, token):
    context = {
        'token': token
    }
    return render(request, 'shouters/register__info-6.html', context=context)


def register(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return HttpResponse('404Error')

    shouter = Shouter.objects.filter(id=_id).first()
    line_profile_picture = shouter.line_profile_picture

    context = {
        'token': token,
        'line_profile_picture': line_profile_picture,
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
        except:
            context = {
                'warning': 'Please Fulfill the information',
                'token': token,
                'line_profile_picture': line_profile_picture,
                'thailand_provinces': thailand_province(),
                'date_lists': date_lists,
                'month_lists': month_lists,
                'year_lists': year_lists,
                'education_lists': education_lists
            }
            return render(request, 'shouters/register.html', context=context)

        if not Shouter.objects.filter(id=_id).exists():
            return HttpResponse('404Error')

        # Save to database
        shouter = Shouter.objects.filter(id=_id).first()
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
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    if request.method == 'POST':
        encoded_token = request.POST['instagram']

        redirect_url = '/shouters/register/ig-api/{}/'.format(encoded_token)

        return redirect(redirect_url)

    shouter = Shouter.objects.filter(id=_id).first()
    context = {
        'shouter': shouter,
        'token': token,
    }
    return render(request, 'shouters/register__choose_instagram.html', context=context)


def register__account_summary(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')
    shouter = Shouter.objects.filter(id=_id).first()
    interest_list = shouter.interest

    interest = shouter_interest(interest_list=interest_list)

    context = {
        'shouter': shouter,
        'interest': interest,
        # Token
        'token': token,
    }

    return render(request, 'shouters/register__account-summary.html', context)


def register__work_selection(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()

    context = {
        'shouter': shouter,
        # Token
        'token': token,
    }

    if request.method == 'POST':
        # IG Only
        is_check_ig = request.POST.getlist('is_check_ig')
        if not is_check_ig == []:
            shouter.is_check_ig = True

            is_check_ig_story = request.POST.getlist('is_check_ig_story')
            if len(is_check_ig_story) != 0:
                is_check_ig_story = True
            else:
                is_check_ig_story = False

            is_check_ig_post = request.POST.getlist('is_check_ig_post')
            if len(is_check_ig_post) != 0:
                is_check_ig_post = True
            else:
                is_check_ig_post = False

            is_check_ig_story_post = request.POST.getlist('is_check_ig_story_post')
            if len(is_check_ig_story_post) != 0:
                is_check_ig_story_post = True
            else:
                is_check_ig_story_post = False

            if not is_check_ig_story and is_check_ig_post and is_check_ig_story_post:
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
        if not is_check_ig_fb == []:
            shouter.is_check_ig_fb = True

            is_check_ig_fb_story = request.POST.getlist('is_check_ig_fb_story')
            if len(is_check_ig_fb_story) != 0:
                is_check_ig_fb_story = True
            else:
                is_check_ig_fb_story = False

            is_check_ig_fb_post = request.POST.getlist('is_check_ig_fb_post')
            if len(is_check_ig_fb_post) != 0:
                is_check_ig_fb_post = True
            else:
                is_check_ig_fb_post = False

            is_check_ig_fb_story_post = request.POST.getlist('is_check_ig_fb_story_post')
            if len(is_check_ig_fb_story_post) != 0:
                is_check_ig_fb_story_post = True
            else:
                is_check_ig_fb_story_post = False

            if not is_check_ig_fb_story and is_check_ig_fb_post and is_check_ig_fb_story_post:
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
            except:
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
            except:
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
    context = {
        'token': token
    }

    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()
    shouter.is_finished_regis = True
    shouter.save()
    response_text = LineApiMessage().api__wait_for_approve_text_message(line_user_id=shouter.line_user_id)
    response_flex = LineApiMessage().api__wait_for_approve_flex_message(line_user_id=shouter.line_user_id)

    if response_text.status_code and response_flex.status_code != 200:
        return HttpResponse('404Error')

    return render(request, 'shouters/register__finished.html', context=context)


def line_login(request):
    # /shouters/line-login?q=register/
    # /shouters/line-login?q=work_management/
    # /shouters/line-login?q=payment/
    # /shouters/line-login?q=shouter_history/

    csrf_token = get_token(request)
    q = request.GET.get('q', None)
    state = {
        'token': csrf_token,
        'q': q,
    }

    line_login_url = LineAPI().line_auth(state=state)
    return redirect(line_login_url)


def oauth(request):
    code = request.GET.get('code')

    # Get State of Request (query string)
    state = request.GET.get('state')
    list_state = state.split(',')
    # Get q (query string)
    q = list_state[1]
    q = q[7:-2]

    access_token, id_token = LineAPI().get_access_token(code=code)

    # Get User Information
    context = LineAPI().get_profile_user(id_token=id_token)

    user_id = context.get('user_id')
    username = context.get('username')
    profile_picture = context.get('profile_picture')

    # Save to Shouter Database
    if Shouter.objects.filter(line_user_id=user_id).exists():
        qs = Shouter.objects.filter(line_user_id=user_id).first()
        line_access_token = qs.line_access_token
        line_id_token = qs.line_id_token
        if line_access_token != access_token:
            qs.line_access_token = access_token
            qs.line_access_token_updated = now()
        if line_id_token != id_token:
            qs.line_id_token = id_token
            qs.line_id_token_updated = now()

        qs.save()

        # if user_id exist in the model but is_connect_ig = False -> go to ig_connect
        _id = qs.id

        # JWT ENCODED
        encoded_token = jwt.encode(
            {'exp': datetime.datetime.now() + datetime.timedelta(days=1), '_id': _id},
            'SHOUTER_JWT_TOKEN',
            algorithm='HS256'
        )

        if not qs.is_register:
            redirect_url = '/shouters/register/info-1/{}/'.format(encoded_token)
        else:
            if not qs.fb_is_connect:
                redirect_url = '/shouters/register/info-2/{}/'.format(encoded_token)
            elif not qs.is_finished_regis:
                redirect_url = '/shouters/register/choose-instagram/{}/'.format(encoded_token)
            else:
                # /shouters/line-login?q=register/
                # /shouters/line-login?q=work_management/
                # /shouters/line-login?q=payment/
                # /shouters/line-login?q=shouter_history/
                redirect_url = '/shouters/menu/{}/'.format(encoded_token)
                # if q == 'menu':
                #     redirect_url = '/shouters/menu/{}/'.format(encoded_token)
                # elif q == 'bank_account':
                #     redirect_url = '/shouters/menu/bank-account/{}/'.format(encoded_token)
                # else:
                #     redirect_url = '/dev/'
                # # if user_id exist in the model and is_connect_ig = True -> go to main page ...
                # if q == 'accept_or_reject':
                #     # return redirect('/orders/{}/choose/'.format(order_id))
                #     return redirect('on_dev')
                # elif q == 'work_management':
                #     # return redirect('/orders/{}/'.format(order_id))
                #     return redirect('on_dev')
                # elif q == 'payment':
                #     # return redirect('/shouters/{}/payment/'.format(_id))
                #     return redirect('on_dev')
                # elif q == 'shouter_history':
                #     # return redirect('/shouters/{}/history'.format(_id))
                #     return redirect('on_dev')

        return redirect(redirect_url)

    else:
        # Create new one
        shouter = Shouter.objects.create(
            line_access_token=access_token,
            line_access_token_updated=now(),
            line_id_token=id_token,
            line_id_token_updated=now(),
            line_user_id=user_id,
            line_username=username,
            line_profile_picture=profile_picture,
        )
        shouter.save()

        qs = Shouter.objects.filter(line_user_id=user_id).first()
        _id = qs.id

        # JWT ENCODED
        encoded_token = jwt.encode(
            {'exp': datetime.datetime.now() + datetime.timedelta(days=1), '_id': _id},
            'SHOUTER_JWT_TOKEN',
            algorithm='HS256'
        )

        redirect_url = '/shouters/register/info-1/{}/'.format(encoded_token)

        # if user_id not exist in the model and is_connect_ig = False -> go to registration form -> redirect to register
        return redirect(redirect_url)


def facebook_login(request, token):
    # check id is exist and not connect ig
    csrf_token = get_token(request)
    state = {
        'csrf_token': csrf_token,
        'token': token
    }
    fb_login_url = FacebookAPI().fb_auth(state=state)

    return redirect(fb_login_url)


def facebook_logout(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()
    access_token = shouter.fb_main_access_token
    response = requests.delete('https://graph.facebook.com/v12.0/me/permissions/', params={'access_token': access_token})
    # Save Access Token and Page ID to database

    if response.status_code == 200:
        shouter.fb_access_token = ''
        shouter.fb_is_connect = False
        shouter.ig_username = ''
        shouter.ig_media_count = 0
        shouter.ig_follower_count = 0
        shouter.ig_following_count = 0
        shouter.ig_active_follower = 0
        shouter.ig_active_follower_harmonic = 0
        shouter.ig_active_follower_percent = 0
        shouter.ig_profile_picture = ''
        shouter.ig_average_total_like = 0
        shouter.ig_engagement_percent = 0

        shouter.save()

        redirect_url = '/shouters/menu/social-media/{}/'.format(token)

        return redirect(redirect_url)

    else:
        return HttpResponse('Failed')


def oauth2(request):
    code = request.GET.get('code')
    # Get token
    state = request.GET.get('state')
    list_state = state.split(',')
    # Get q (query string)
    token = list_state[1]
    token = token[11:-2]

    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return HttpResponse('404Error')
    shouter = Shouter.objects.filter(id=_id).first()

    context = {
        'token': token
    }

    # Get Access Token
    context__access_token = FacebookAPI().get_access_token(code=code)
    if context__access_token:
        access_token = context__access_token.get('access_token')

        if access_token == '':
            return HttpResponse('Failed by access token')

    else:
        return HttpResponse('Failed by access token')

    shouter.fb_main_access_token = access_token
    shouter.save()

    # Get FB Page ID
    context__page_id = FacebookAPI().get_facebook_page_id(access_token=access_token)
    is_found = False
    if context__page_id:
        objs = context__page_id['data']['data']
        list_obj = []
        for obj in objs:
            obj__access_token = obj.get('access_token')
            obj__page_name = obj.get('name')
            obj__page_id = obj.get('id')

            context__business_account_id = FacebookAPI().get_business_account_id(page_id=obj__page_id,
                                                                                 access_token=obj__access_token)

            if context__business_account_id:
                business_account_id = context__business_account_id.get('business_account_id')

                if not business_account_id == '':
                    context__active_follower = FacebookAPI().get_active_follower(business_account_id=business_account_id, access_token=obj__access_token)
                    if not context__active_follower:
                        continue
                    else:
                        is_found = True
                    # return render(request, 'shouters/register__choose_instagram.html', context)
                else:
                    continue

            else:
                return render(request, 'shouters/register__choose_instagram.html', context)

            if is_found:
                # Get FB Name
                response = requests.get('https://graph.facebook.com/v12.0/me',
                                        params={'access_token': access_token ,
                                                'fields': 'name,picture'})
                context__basic_fb = response.json()
                fb_name = context__basic_fb['name']
                fb_profile_picture = context__basic_fb['picture']['data']['url']

                # Get Bio
                context__ig_biography = FacebookAPI().get_ig_biography(business_account_id=business_account_id,
                                                                       access_token=access_token)
                if context__ig_biography:
                    ig_username = context__ig_biography.get('username')
                    ig_media_count = context__ig_biography.get('media_count')
                    ig_follower_count = context__ig_biography.get('followers')
                    ig_following_count = context__ig_biography.get('followings')
                    ig_profile_picture = context__ig_biography.get('profile_picture_url')
                else:
                    return HttpResponse('Failed by ig biography')

                data = {
                    'exp': datetime.datetime.now() + datetime.timedelta(days=1),
                    '_id': _id,
                    'access_token': obj__access_token,
                    'page_name': obj__page_name,
                    'page_id': obj__page_id,
                    'fb_name': fb_name,
                    'fb_profile_picture': fb_profile_picture,
                    'ig_business_account_id': business_account_id,
                    'ig_username': ig_username,
                    'ig_media_count': ig_media_count,
                    'ig_follower_count': ig_follower_count,
                    'ig_following_count': ig_following_count,
                    'ig_profile_picture': ig_profile_picture,
                }

                encoded_token = jwt.encode(data, 'SHOUTER_JWT_TOKEN', algorithm='HS256')

                # encode token
                data = {
                    'page_name': obj__page_name,
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
    if is_found:
        return render(request, 'shouters/register__choose_instagram.html', context)
    else:
        context = {
            'token': token
        }
        return render(request, 'shouters/register__choose_instagram.html', context)


def register__get_ig_data(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        fb_access_token = decoded_token.get('access_token')
        fb_page_name = decoded_token.get('page_name')
        fb_page_id = decoded_token.get('page_id')
        fb_name = decoded_token.get('fb_name')
        fb_profile_picture = decoded_token.get('fb_profile_picture')
        ig_business_account_id = decoded_token.get('ig_business_account_id')
        ig_username = decoded_token.get('ig_username')
        ig_media_count = decoded_token.get('ig_media_count')
        ig_follower_count = decoded_token.get('ig_follower_count')
        ig_following_count = decoded_token.get('ig_following_count')
        ig_profile_picture = decoded_token.get('ig_profile_picture')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()
    # Get Info
    shouter.fb_access_token = fb_access_token
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

    # Get Active Follower
    context__active_follower = FacebookAPI().get_active_follower(business_account_id=ig_business_account_id,
                                                                 access_token=fb_access_token)

    if context__active_follower:
        shouter.ig_response_active_follower = context__active_follower.get('data')
        shouter.ig_active_follower = context__active_follower.get('geometric_active_follower')
        shouter.ig_active_follower_harmonic = context__active_follower.get('harmonic_active_follower')
        ig_active_follower_percent = (shouter.ig_active_follower / shouter.ig_follower_count) * 100
        ig_active_follower_percent = round(ig_active_follower_percent, 2)
        shouter.ig_active_follower_percent = ig_active_follower_percent
        shouter.save()
    else:
        return HttpResponse('Failed by ig active follower')

    # Get Media Objects
    context__media_objects = FacebookAPI().get_ig_media_objects(business_account_id=ig_business_account_id,
                                                                access_token=fb_access_token)
    if context__media_objects:
        shouter.ig_response_media_objects = context__media_objects.get('data')
        shouter.save()
        media_objects = context__media_objects.get('media_objects')
    else:
        return HttpResponse('Failed by media objects')

    # Get Engagement
    context__engagement = FacebookAPI().get_engagement_insight(media_objects=media_objects,
                                                               access_token=fb_access_token,
                                                               followers=shouter.ig_follower_count)

    shouter.ig_average_total_like = context__engagement.get('average_total_like')

    ig_engagement_percent = (shouter.ig_average_total_like / shouter.ig_active_follower) * 100
    ig_engagement_percent = round(ig_engagement_percent, 2)
    ig_story_view = context__engagement.get('story_view')
    ig_average_post_reach = context__engagement.get('average_post_reach')

    shouter.ig_engagement_percent = ig_engagement_percent
    shouter.ig_story_view = ig_story_view
    shouter.ig_average_post_reach = ig_average_post_reach

    # Cal Ads Post Reach
    predicted_ad_post_reach = ig_story_view * 3
    ig_ad_post_reach = (ig_average_post_reach + predicted_ad_post_reach) / 2

    shouter.ig_predicted_ad_post_reach = predicted_ad_post_reach
    shouter.ig_ad_post_reach = ig_ad_post_reach
    # shouter.ig_like_engagement = context__engagement.get('like_engagement')
    shouter.save()

    # Cal Price
    ig_price_story_fc = round(IGStoryFc().cal_price(ig_story_view), 2)
    ig_price_story_ugc = round(IGStoryUgc().cal_price(ig_story_view), 2)
    ig_price_post_fc = round(IGPostFc().cal_price(ig_ad_post_reach), 2)
    ig_price_post_ugc = round(IGPostUgc().cal_price(ig_ad_post_reach), 2)
    shouter.ig_price_story_fc = ig_price_story_fc
    shouter.ig_price_story_ugc = ig_price_story_ugc
    shouter.ig_price_post_fc = ig_price_post_fc
    shouter.ig_price_post_ugc = ig_price_post_ugc
    shouter.save()

    ig_price_story_post_fc = (ig_price_story_fc + ig_price_post_fc) * 0.9
    ig_price_story_post_ugc = (ig_price_story_ugc + ig_price_post_ugc) * 0.9
    shouter.ig_price_story_post_fc = round(ig_price_story_post_fc, 2)
    shouter.ig_price_story_post_ugc = round(ig_price_story_post_ugc, 2)
    shouter.save()

    shouter.ig_fb_price_story_fc = round(ig_price_story_fc * 1.1, 2)
    shouter.ig_fb_price_story_ugc = round(ig_price_story_ugc * 1.1, 2)
    shouter.ig_fb_price_post_fc = round(ig_price_post_fc * 1.1, 2)
    shouter.ig_fb_price_post_ugc = round(ig_price_post_ugc * 1.1, 2)
    shouter.ig_fb_price_story_post_fc = round(ig_price_story_post_fc * 1.1, 2)
    shouter.ig_fb_price_story_post_ugc = round(ig_price_story_post_ugc * 1.1, 2)
    shouter.save()

    context__audience_insight = FacebookAPI().get_audience_insight(business_account_id=ig_business_account_id,
                                                                   access_token=fb_access_token)
    shouter.ig_response_audience_insight = context__audience_insight.get('data')

    shouter.fb_is_connect = True
    shouter.save()

    redirect_url = '/shouters/register/work-selection/{}/'.format(token)

    return redirect(redirect_url)


def menu(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()
    context = {
        'shouter': shouter,
        'token': token,
    }

    return render(request, 'shouters/menu.html', context)


def menu__social_media(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()
    context = {
        'shouter': shouter,
        'ig_username': shouter.ig_username,
        'ig_media_count': shouter.ig_media_count,
        'ig_followers': shouter.ig_follower_count,
        'ig_followings': shouter.ig_following_count,
        'ig_active_follower': shouter.ig_active_follower,
        'ig_active_follower_percent': shouter.ig_active_follower_percent,
        'ig_engagement': shouter.ig_average_total_like,
        'ig_engagement_percent': shouter.ig_engagement_percent,
        'ig_profile_picture_url': shouter.ig_profile_picture,
        'fb_connect_status': shouter.fb_is_connect,
        'token': token
    }
    return render(request, 'shouters/menu__social-media.html', context)


def menu__bank_account(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if not Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()
    return redirect('on_dev')

    # context = {
    #     'token': token
    # }
    # return render(request, 'shouters/menu__bank-account.html', context)


