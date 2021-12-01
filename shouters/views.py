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

def register__account_summary(request):
    if request.method == 'POST':
        redirect('register__account_summary')
    return render(request, 'shouters/register__account-summary.html')

def register__work_selection(request):
    return render(request, 'shouters/register__work-selection.html')

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
        shouter.save()
        return redirect('shouter-menu')
    else:
        print(response.status_code)
        return HttpResponse('Failed')

@login_required(login_url='/shouters/login/')
def oauth2(request):
    code = request.GET.get('code')
    if request.user is not None:
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

        return redirect('register__work_selection')

    else:
        return redirect('on_dev')

@login_required(login_url='/shouters/login/')
def menu(request):
    return render(request, 'shouters/menu.html')

@login_required(login_url='/shouters/login/')
def social_media(request):
    user = request.user
    if Shouter.objects.filter(user=user).exists():
        shouter = Shouter.objects.filter(user=user).first()
        if not shouter.fb_is_connect:
            context = {
                'is_connect': False,
            }
        else:
            context = {
                'is_connect': True,
            }
        return render(request, 'shouters/menu__social-media.html', context)
    return redirect('on_dev')