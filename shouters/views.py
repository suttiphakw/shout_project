import json
import requests

# from rest_framework_simplejwt.tokens import RefreshToken

from django.utils.timezone import now
from django.shortcuts import render, redirect, HttpResponse
from django.middleware.csrf import get_token

from shouters.utils import LineAPI, FacebookAPI
from shouters.models import Shouter
# from orders.models import Order
from shouters.lists import thailand_province

# Create your views here.

def landing_page(request):
    return render(request, 'shouters/landing.html')

def register_info_1(request):
    return render(request, 'shouters/regis-info-1.html')

def register_info_2(request, _id):
    context = {
        'id': _id
    }
    return render(request, 'shouters/regis-info-2.html', context)

def register_info_3(request, _id):
    context = {
        'id': _id
    }
    return render(request, 'shouters/regis-info-3.html', context)

def register_info_4(request, _id):
    context = {
        'id': _id
    }
    return render(request, 'shouters/regis-info-4.html', context)

def register_info_5(request, _id):
    context = {
        'id': _id
    }
    return render(request, 'shouters/regis-info-5.html', context)

def register_info_6(request, _id):
    context = {
        'id': _id
    }
    return render(request, 'shouters/regis-info-6.html', context)

def register(request, _id):
    context = {
        'id': _id,
        'objs': thailand_province(),
    }

    if Shouter.objects.filter(id=_id).exists():
        shouter = Shouter.objects.filter(id=_id).first()
        if shouter.first_name != '':
            redirect('on_dev')
        if request.method == 'GET':
            return render(request, 'shouters/register.html', context)
        first_name = request.POST['first_name']
        shouter.first_name = first_name
        shouter.save()
        return redirect('/shouters/register/info-2/{}/'.format(_id))
    else:
        return redirect('on_dev')

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

def facebook_login(request, _id):
    # check id is exist and not connect ig
    csrf_token = get_token(request)
    state = {
        'token': csrf_token,
        '_id': _id,
    }
    fb_login_url = FacebookAPI().fb_auth(state=state)

    return redirect(fb_login_url)

def oauth(request):
    code = request.GET.get('code')

    """Get State of request"""
    state = request.GET.get('state')
    list_state = state.split(',')
    # Get q
    q = list_state[1]
    q = q[7:-2]

    print(q)

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
        if qs.is_register is False:
            return redirect('/shouters/register/{}/'.format(_id))
        else:
            if qs.is_connect_ig is False:
                return redirect('/shouters/register/info-2/{}/'.format(_id))
            else:
                # if user_id exist in the model and is_connect_ig = True -> go to main page ...
                if q == 'accept_or_reject':
                    # return redirect('/orders/{}/choose/'.format(order_id))
                    return redirect('on_dev')
                elif q == 'work_management':
                    # return redirect('/orders/{}/'.format(order_id))
                    return redirect('on_dev')
                elif q == 'payment':
                    # return redirect('/shouters/{}/payment/'.format(_id))
                    return redirect('on_dev')
                elif q == 'shouter_history':
                    # return redirect('/shouters/{}/history'.format(_id))
                    return redirect('on_dev')

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

        # if user_id not exist in the model and is_connect_ig = False -> go to registration form -> redirect to register
        return redirect('/shouters/register/{}/'.format(_id))

    # """JWT Access Token and Refresh Token"""
    # refresh = refresh = RefreshToken.for_user(shouter_save)
    # data['token'] = {
    #     'refresh': str(refresh),
    #     'access': str(refresh.access_token),
    # }



