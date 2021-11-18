# import json
# import requests
#
# from django.utils.timezone import now
# from django.shortcuts import render, redirect, HttpResponse
# from django.middleware.csrf import get_token
#
# from shouters.utils import LineAPI, FacebookAPI
# from shouters.models import Shouter
# from orders.models import Order

# def register(request, _id):
#     qs = Shouter.objects.filter(id=_id)
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         gender = request.POST['gender']
#         email = request.POST['email']
#         age = request.POST['age']
#         phone = request.POST['phone']
#         interest = request.POST.getlist('interest')
#
#         if qs.exists() and qs.count() == 1:
#             user = qs.first()
#             user.first_name = first_name
#             user.last_name = last_name
#             user.gender = gender
#             user.email = email
#             user.age = age
#             user.phone = phone
#             user.interest = interest
#             user.is_register = True
#             user.save()
#
#             return HttpResponse('<a href="/shouters/{}/fb_login/">Connect IG</a>')
#
#     return render(request, 'shouters/register.html', context={'id': _id})

# def login(request):
#     csrf_token = get_token(request)
#     q = request.GET.get('q', None)
#     order_id = request.GET.get('order_id', None)
#     state = {
#         'token': csrf_token,
#         'q': q,
#         'order_id': order_id
#     }
#     line_login_url = LineAPI().line_auth(state=state)
#
#     return redirect(line_login_url)
#
# def fb_login(request, _id):
#     csrf_token = get_token(request)
#     state = {
#         'token': csrf_token,
#         '_id': _id
#     }
#     fb_login_url = FacebookAPI().fb_auth(state=state)
#
#     return redirect(fb_login_url)
#
# def Oauth(request):
#
#     # Get Code from redirect url
#     code = request.GET.get('code')
#     state = request.GET.get('state')
#     list_state = state.split(',')
#     # Get q
#     q = list_state[1]
#     q = q[7:-2]
#     # Get Order ID
#     order_id = list_state[2]
#
#     # Get Access Token + ID Token
#     access_token, id_token = LineAPI().get_access_token(code=code)
#
#     # Get User Information
#     context = LineAPI().get_profile_user(id_token=id_token)
#     user_id = context.get('user_id')
#     username = context.get('username')
#     profile_picture = context.get('profile_picture')
#
#     # Save to Shouter Database
#     if Shouter.objects.filter(line_user_id=user_id).exists():
#         qs = Shouter.objects.filter(line_user_id=user_id).first()
#         line_access_token = qs.line_access_token
#         line_id_token = qs.line_id_token
#         if line_access_token != access_token:
#             qs.line_access_token = access_token
#             qs.line_access_token_updated = now()
#         if line_id_token != id_token:
#             qs.line_id_token = id_token
#             qs.line_id_token_updated = now()
#
#         qs.save()
#
#         # if user_id exist in the model but is_connect_ig = False -> go to ig_connect
#         _id = qs.id
#         if qs.is_register is False:
#             return redirect('/shouters/{}/register/'.format(_id))
#         else:
#             if qs.is_connect_ig is False:
#                 return redirect('/shouters/{}/fb_login/'.format(_id))
#             else:
#                 # if user_id exist in the model and is_connect_ig = True -> go to main page ...
#                 # if q = register
#                 if q == 'accept_or_reject':
#                     # return redirect('/orders/{}/choose/'.format(order_id))
#                     return HttpResponse('<h1>Accept Or Reject Page</h1>')
#                 elif q == 'work_management':
#                     # return redirect('/orders/{}/'.format(order_id))
#                     return HttpResponse('<h1>Work Management</h1>')
#                 elif q == 'payment':
#                     # return redirect('/shouters/{}/payment/'.format(_id))
#                     return HttpResponse('<h1>Payment</h1>')
#                 elif q == 'shouter_history':
#                     # return redirect('/shouters/{}/history'.format(_id))
#                     return HttpResponse('<h1>Shouter History</h1>')
#
#     else:
#         # Create new one
#         # print(access_token, now, id_token, user_id, user_id, profile_picture)
#         shouter = Shouter.objects.create(
#             line_access_token=access_token,
#             line_access_token_updated=now(),
#             line_id_token=id_token,
#             line_id_token_updated=now(),
#             line_user_id=user_id,
#             line_username=username,
#             line_profile_picture=profile_picture,
#         )
#         shouter.save()
#
#         # if user_id not exist in the model and is_connect_ig = False -> go to registration form -> redirect
#         to register
#         return redirect('shouters_register')
#
# def Oauth2(request):
#
#     # Get Code from redirect url
#     code = request.GET.get('code')
#     state = request.GET.get('state')
#     list_state = state.split(',')
#     _id = list_state[1]
#     # Get Shouter ID
#     _id = int(_id[8:-1])
#
#     user = Shouter.objects.filter(id=_id).first()
#
#     # Get access token for facebook login
#     access_token = FacebookAPI().get_access_token(code=code)
#
#     # Get FB Page ID
#     page_id = FacebookAPI().get_facebook_page_id(access_token=access_token)
#
#     # Get IG Page ID
#     business_account_id = FacebookAPI().get_business_account_id(page_id=page_id, access_token=access_token)
#
#     # Save Access Token and Page ID to database
#     user.fb_access_token = access_token
#     user.fb_access_token_created = now()
#     user.fb_page_id = page_id
#     user.ig_business_account_id = business_account_id
#     user.save()
#
#     # Get Biography of User Instagram
#     biography = FacebookAPI().get_ig_biography(business_account_id=business_account_id,
#                                                access_token=access_token)
#
#     profile_picture_url = biography.get('profile_picture_url')
#
#     print(profile_picture_url)
#
#     user.ig_username = biography.get('username')
#     user.ig_follower_count = biography.get('followers')
#     user.save()
#
#     # Get Engagement Insight
#     media_objects = FacebookAPI().get_ig_media_objects(business_account_id=business_account_id,
#                                                        access_token=access_token)
#     engagement = FacebookAPI().get_engagement_insight(media_objects=media_objects,
#                                                       access_token=access_token,
#                                                       followers_count=biography.get('followers'))
#     total_likes = engagement.get('total_likes')
#     average_total_like = engagement.get('average_total_like')
#     like_engagement = engagement.get('like_engagement')
#
#     user.ig_total_like = total_likes
#     user.ig_average_total_like = average_total_like
#     user.ig_like_engagement = like_engagement
#
#     audience = FacebookAPI().get_audience_insight(business_account_id=business_account_id,
#                                                   access_token=access_token)
#
#     # Save IG Insight to Database
#     user.ig_insight = audience.get('insight')
#     user.ig_max_total_people = audience.get('max_total')
#     user.ig_two_most_common_city = audience.get('two_most_common_city')
#     user.ig_two_most_common_country = audience.get('two_most_common_country')
#     user.ig_two_most_common_gender_age = audience.get('two_most_common_gender_age')
#     user.ig_audience_male_percent = audience.get('audience_male_percentage')
#     user.ig_audience_female_percent = audience.get('audience_female_percentage')
#     user.ig_age_range_13_17 = audience.get('audience_age_13_17_percentage')
#     user.ig_age_range_18_24 = audience.get('audience_age_18_24_percentage')
#     user.ig_age_range_25_34 = audience.get('audience_age_25_34_percentage')
#     user.ig_age_range_35_44 = audience.get('audience_age_35_44_percentage')
#     user.ig_age_range_45_54 = audience.get('audience_age_45_54_percentage')
#     user.ig_age_range_55_64 = audience.get('audience_age_55_64_percentage')
#     user.save()
#
#     active_follower = FacebookAPI().get_active_follower(business_account_id=business_account_id,
#                                                         access_token=access_token)
#
#     user.ig_active_follower = active_follower.get('geometric_active_follower')
#     user.ig_active_follower_harmonic = active_follower.get('harmonic_active_follower')
#
#     return HttpResponse('test')
#
# def payment(request, _id):
#     return None
#
# def history(request, _id):
#     return None
#
# def setting(request, _id):
#     return None
