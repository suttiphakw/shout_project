import jwt
import requests
import datetime
from django.utils.timezone import now
from django.shortcuts import render, redirect, HttpResponse
from django.middleware.csrf import get_token
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from shouters.utils import LineAPI, FacebookAPI
from shouters.models import Shouter
# from orders.models import Order

from utils.cal_price import IGStoryFc, IGStoryUgc, IGPostFc, IGPostUgc
from shouters.lists import thailand_province


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
        'objs': thailand_province(),
        'line_profile_picture': line_profile_picture,
    }

    if request.method == 'POST':
        # Get User information
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

        context = {
            'nickname': nickname,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'tel': tel,
            'gender': gender,
            'birthday_date': birthday_date,
            'birthday_month': birthday_month,
            'birthday_year': birthday_year,
            'province': province,
            'education': education,
            'college': college,
            'interest': interest
        }

        print(context)

        if not Shouter.objects.filter(id=_id).exists():
            return HttpResponse('404Error')

        # Save to database
        shouter = Shouter.objects.filter().first()
        shouter.first_name = first_name
        shouter.is_register = True
        shouter.save()

        redirect_url = '/shouters/register/info-2/{}/'.format(token)
        return redirect(redirect_url)

    return render(request, 'shouters/register.html', context=context)


def register__account_summary(request, token):
    # if request.method == 'POST':
    #     redirect('register__account_summary')

    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')
    shouter = Shouter.objects.filter(id=_id).first()

    context = {
        'ig_username': shouter.ig_username,
        'ig_media_count': shouter.ig_media_count,
        'ig_profile_picture_url': shouter.ig_profile_picture,
        'ig_followers': shouter.ig_follower_count,
        'ig_followings': shouter.ig_following_count,
        'ig_active_follower': shouter.ig_active_follower,
        'ig_active_follower_percent': shouter.ig_active_follower_percent,
        'ig_engagement': shouter.ig_average_total_like,
        'ig_engagement_percent': shouter.ig_engagement_percent,
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
        'ig_price_story_fc': shouter.ig_price_story_fc,
        'ig_price_story_ugc': shouter.ig_price_story_ugc,
        'ig_price_post_fc': shouter.ig_price_post_fc,
        'ig_price_post_ugc': shouter.ig_price_post_ugc,
        'ig_price_story_post_fc': shouter.ig_price_story_post_fc,
        'ig_price_story_post_ugc': shouter.ig_price_story_post_ugc,
        'token': token,
    }

    return render(request, 'shouters/register__work-selection.html', context)


def register__finished(request, token):
    context = {
        'token': token
    }

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
    # print(q)

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

        if qs.is_register is False:
            redirect_url = '/shouters/register/info-1/{}/'.format(encoded_token)
        else:
            if qs.is_connect_ig is False:
                redirect_url = '/shouters/register/info-2/{}/'.format(encoded_token)
            else:
                redirect_url = '/shouters/menu/{}/'.format(encoded_token)
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
        # print(access_token, now, id_token, user_id, user_id, profile_picture)
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
    access_token = shouter.fb_access_token
    response = requests.delete('https://graph.facebook.com/v12.0/me/permissions/',
                               params={
                                   'access_token': access_token
                               })
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
        # shouter.ig_like_engagement = ''
        # shouter.ig_total_like = 0
        shouter.ig_average_total_like = 0
        shouter.ig_engagement_percent = 0

        shouter.save()

        redirect_url = '/shouters/menu/social-media/{}/'.format(token)

        return redirect(redirect_url)

    else:
        print(response.status_code)
        return HttpResponse('Failed')


def oauth2(request):
    code = request.GET.get('code')
    # Get token
    state = request.GET.get('state')
    list_state = state.split(',')
    print('list_state :', list_state)
    # Get q (query string)
    token = list_state[1]
    # print('token :', token)
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

    access_token = FacebookAPI().get_access_token(code=code)

    # Get FB Page ID
    page_id = FacebookAPI().get_facebook_page_id(access_token=access_token)

    # Get IG Page ID
    business_account_id = FacebookAPI().get_business_account_id(page_id=page_id, access_token=access_token)

    # Save Access Token and Page ID to database
    shouter.fb_access_token = access_token
    shouter.fb_access_token_created = now()
    shouter.fb_is_connect = True
    shouter.fb_page_id = page_id
    shouter.ig_business_account_id = business_account_id
    shouter.save()

    # Get Bio
    context__ig_biography = FacebookAPI().get_ig_biography(business_account_id=business_account_id,
                                                           access_token=access_token)

    shouter.ig_username = context__ig_biography.get('username')
    shouter.ig_media_count = context__ig_biography.get('media_count')
    shouter.ig_follower_count = context__ig_biography.get('followers')
    shouter.ig_following_count = context__ig_biography.get('followings')
    shouter.ig_profile_picture = context__ig_biography.get('profile_picture_url')
    shouter.save()

    # Get Active Follower
    context__active_follower = FacebookAPI().get_active_follower(business_account_id=business_account_id,
                                                                 access_token=access_token)

    shouter.ig_active_follower = context__active_follower.get('geometric_active_follower')
    shouter.ig_active_follower_harmonic = context__active_follower.get('harmonic_active_follower')
    ig_active_follower_percent = (shouter.ig_active_follower / shouter.ig_follower_count) * 100
    ig_active_follower_percent = round(ig_active_follower_percent, 2)
    shouter.ig_active_follower_percent = ig_active_follower_percent
    shouter.save()

    # Get Media Objects
    media_objects = FacebookAPI().get_ig_media_objects(business_account_id=business_account_id,
                                                       access_token=access_token)

    # Get Engagement
    context__engagement = FacebookAPI().get_engagement_insight(media_objects=media_objects,
                                                               access_token=access_token,
                                                               followers=shouter.ig_follower_count)

    shouter.ig_average_total_like = context__engagement.get('average_total_like')

    ig_engagement_percent = (shouter.ig_average_total_like / shouter.ig_active_follower) * 100
    ig_engagement_percent = round(ig_engagement_percent, 2)

    shouter.ig_engagement_percent = ig_engagement_percent
    shouter.ig_story_view = context__engagement.get('story_view')
    shouter.ig_average_post_reach = context__engagement.get('average_post_reach')
    # shouter.ig_like_engagement = context__engagement.get('like_engagement')
    shouter.save()

    shouter.ig_price_story_fc = round(IGStoryFc().cal_price(shouter.ig_story_view), 2)
    shouter.ig_price_story_ugc = round(IGStoryUgc().cal_price(shouter.ig_story_view), 2)
    shouter.ig_price_post_fc = round(IGPostFc().cal_price(shouter.ig_story_view), 2)
    shouter.ig_price_post_ugc = round(IGPostUgc().cal_price(shouter.ig_story_view), 2)

    ig_price_story_post_fc = (IGStoryFc().cal_price(shouter.ig_story_view) +
                              IGPostFc().cal_price(shouter.ig_story_view)) * 0.9
    ig_price_story_post_fc = round(ig_price_story_post_fc, 2)

    ig_price_story_post_ugc = (IGStoryUgc().cal_price(shouter.ig_story_view) +
                               IGPostUgc().cal_price(shouter.ig_story_view)) * 0.9
    ig_price_story_post_ugc = round(ig_price_story_post_ugc, 2)

    shouter.ig_price_story_post_fc = ig_price_story_post_fc
    shouter.ig_price_story_post_ugc = ig_price_story_post_ugc
    shouter.save()

    redirect_url = '/shouters/register/work_selection/{}/'.format(token)

    return redirect(redirect_url)


def menu(request, token):
    try:
        decoded_token = jwt.decode(token, 'SHOUTER_JWT_TOKEN', algorithms='HS256')
        _id = decoded_token.get('_id')
        pass
    except:
        return HttpResponse('404Error')

    if Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()
    context = {
        'ig_profile_picture_url': shouter.ig_profile_picture,
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

    if Shouter.objects.filter(id=_id).exists():
        return redirect('on_dev')

    shouter = Shouter.objects.filter(id=_id).first()
    context = {
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

