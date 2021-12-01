import requests
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

def register__info_1(request):
    return render(request, 'shouters/register__info-1.html')

def register__info_2(request):
    return render(request, 'shouters/register__info-2.html')

def register__info_3(request):
    return render(request, 'shouters/register__info-3.html')

def register__info_4(request):
    return render(request, 'shouters/register__info-4.html')

def register__info_5(request):
    return render(request, 'shouters/register__info-5.html')

def register__info_6(request):
    return render(request, 'shouters/register__info-6.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check If Password Match
        # Check Username duplicate
        if User.objects.filter(username=username).exists():
            return redirect('shouters-register')
        else:
            # Look Good
            user = User.objects.create_user(username=username, password=password)
            # Login after register
            user.save()
            return redirect('shouters-login')

    else:
        return render(request, 'shouters/register.html')

@login_required(login_url='/shouters/login/')
def register__account_summary(request):
    # if request.method == 'POST':
    #     redirect('register__account_summary')
    user = request.user
    if Shouter.objects.filter(user=user).exists():
        shouter = Shouter.objects.filter(user=user).first()

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
        }

        return render(request, 'shouters/register__account-summary.html', context)
    return redirect('on_dev')

@login_required(login_url='/shouters/login/')
def register__work_selection(request):
    user = request.user
    if Shouter.objects.filter(user=user).exists():
        shouter = Shouter.objects.filter(user=user).first()

        context = {
            'ig_price_story_fc': shouter.ig_price_story_fc,
            'ig_price_story_ugc': shouter.ig_price_story_ugc,
            'ig_price_post_fc': shouter.ig_price_post_fc,
            'ig_price_post_ugc': shouter.ig_price_post_ugc,
            'ig_price_story_post_fc': shouter.ig_price_story_post_fc,
            'ig_price_story_post_ugc': shouter.ig_price_story_post_ugc,
        }

        return render(request, 'shouters/register__work-selection.html', context)
    return redirect('on_dev')

@login_required(login_url='/shouters/login/')
def register__finished(request):
    return render(request, 'shouters/register__finished.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('register__info-2')
        else:
            return redirect('shouters-login')

    else:
        return render(request, 'shouters/login.html')

def logout(request):
    auth.logout(request)
    return redirect('shouters-login')

@login_required(login_url='/shouters/login/')
def facebook_login(request):
    # check id is exist and not connect ig
    csrf_token = get_token(request)
    state = {
        'token': csrf_token,
    }
    fb_login_url = FacebookAPI().fb_auth(state=state)

    return redirect(fb_login_url)

@login_required(login_url='/shouters/login/')
def facebook_logout(request):
    user = request.user
    if Shouter.objects.filter(user=user).exists():
        shouter = Shouter.objects.filter(user=user).first()
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
            return redirect('shouter__menu__social-media')
        else:
            print(response.status_code)
            return HttpResponse('Failed')
    return redirect('on_dev')

@login_required(login_url='/shouters/login/')
def oauth2(request):
    code = request.GET.get('code')
    if request.user is not None:
        if Shouter.objects.filter(user=request.user).exists():
            Shouter.objects.filter(user=request.user).delete()

        shouter = Shouter.objects.create(user=request.user)
        shouter.save()

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

        return redirect('register__work_selection')

    else:
        return redirect('on_dev')

@login_required(login_url='/shouters/login/')
def menu(request):
    user = request.user
    if Shouter.objects.filter(user=user).exists():
        shouter = Shouter.objects.filter(user=user).first()

        context = {
            'ig_profile_picture_url': shouter.ig_profile_picture,
        }

        return render(request, 'shouters/menu.html', context)
    return redirect('on_dev')

@login_required(login_url='/shouters/login/')
def menu__social_media(request):
    user = request.user
    if Shouter.objects.filter(user=user).exists():
        shouter = Shouter.objects.filter(user=user).first()

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
        }
        return render(request, 'shouters/menu__social-media.html', context)
    return redirect('on_dev')