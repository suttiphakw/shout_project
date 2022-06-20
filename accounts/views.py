import jwt
import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.mail import send_mail
from django.template.loader import render_to_string
from brands.models import BrandProfile


# Create your views here.
def register(request):
  if request.method == 'POST':
    # Get Info
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    tel = request.POST['tel']
    company = request.POST['company']
    position = request.POST['position']
    password_1 = request.POST['password_1']
    password_2 = request.POST['password_2']
    # Is Password Match
    if password_1 != password_2:
      messages.error(request, 'Password do not match')
      return redirect('register')

    # Is Email is already taken
    if User.objects.filter(username=email).exists():
      messages.error(request, 'This email is already register')
      return redirect('register')
    # Look good
    user = User.objects.create_user(username=email, password=password_1, first_name=first_name, last_name=last_name, email=email)
    user.is_active = False
    user.save()
    brand = BrandProfile.objects.create(user=user, email=email, first_name=first_name, last_name=last_name, tel=tel, company=company, position=position)
    brand.save()
    # Send Email + Token Encode
    data = {
      'email': brand.email,
      'exp': datetime.datetime.now() + datetime.timedelta(days=1),
    }
    token = jwt.encode(data, 'U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw', algorithm='HS256')
    confirm_link = 'https://shoutsolution.com/accounts/email/confirm/' + token + '/'
    msg_html = render_to_string('emails/confirm_account.html', {'confirm_link': confirm_link})
    send_mail('Email Verification', 'Account Activation', 'noreply@shoutsolution.com', [brand.email], html_message=msg_html)
    redirect_url = '/accounts/email/verification/{}/'.format(token)
    # Redirect to Confirm Email Page
    return redirect(redirect_url)
      
  return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    # Get Info
    email = request.POST['email']
    password = request.POST['password']
    # Brand email exists but not active
    brand = BrandProfile.objects.filter(email=email).first()
    if brand and not brand.is_active:
      context = {
        'message': 'กรุณาทำการยืนยัน Email ใน Inbox {}'.format(email)
      }
      # Return Message Actvate your email plz
      return render(request, 'accounts/login.html', context)
    # Authenticate user
    user = auth.authenticate(username=email, password=password)
    if user is not None:   
      auth.login(request, user)
      return redirect('brand__index')
    context = {
      'message': 'Incorrect email or password'
    }
    return render(request, 'accounts/login.html', context)
  return render(request, 'accounts/login.html')


def logout(request):
  auth.logout(request)
  return redirect('index')


def forget_password(request):
  # Request Method = Post
  if request.method == 'POST':
    email = request.POST['email']
    # Check Email is Exist
    brand = BrandProfile.objects.filter(email=email)
    if brand.exists():
      # Send Email + Token Encode
      data = {
        'email': email,
        'exp': datetime.datetime.now() + datetime.timedelta(days=1),
      }
      token = jwt.encode(data, 'U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw', algorithm='HS256')
      confirm_link = 'https://shoutsolution.com/accounts/forget_password/change/' + token + '/'
      msg_html = render_to_string('emails/forget_password.html', {'confirm_link': confirm_link})
      send_mail('Forget Password', 'Forget Password', 'noreply@shoutsolution.com', [email], html_message=msg_html)
      redirect_url = '/accounts/forget_password/email/{}/'.format(token)
      return redirect(redirect_url)
    context = {
      'message': 'Incorrect Email'
    }
    return render(request, 'accounts/forget_password.html', context)
  # Sent Email with token to reset password
  return render(request, 'accounts/forget_password.html')


def forget_password_email(request, token):
  decoded_token = jwt.decode(token, 'U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw', algorithms='HS256')
  email = decoded_token['email']
  context = {
    'email': email
  }
  return render(request, 'accounts/forget_password_email.html', context)


def change_password(request, token):
  # return render(request, 'accounts/change_password.html')
  decoded_token = jwt.decode(token, 'U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw', algorithms='HS256')
  email = decoded_token['email']
  brand = User.objects.filter(email=email)
  context = {
    'token': token
  }
  # Found Brand
  if brand.exists():
    if request.method == 'POST':
      password_1 = request.POST['password_1']
      password_2 = request.POST['password_2']
      if password_1 != password_2:
        # Return with message
        context = {
          'token': token,
          'message': 'รหัสผ่านไม่ตรงกัน กรุณากรอกใหม่'
        }
        return render(request, 'accounts/change_password.html', context)
      
      # Check Pass
      brand = brand.first()
      brand.set_password(password_1)
      brand.save()
      return redirect('change_password_complete', token)
    return render(request, 'accounts/change_password.html', context)
  return HttpResponse('Not Found Brand')
  

def change_password_complete(request, token):
  context = {
    'token': token
  }
  return render(request, 'accounts/change_password_complete.html', context)


def email_verification(request, token):
  decoded_token = jwt.decode(token, 'U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw', algorithms='HS256')
  email = decoded_token['email']
  return render(request, 'accounts/email_verification.html', context={'email': email})


def email_confirm(request, token):
  # Decode Token
  decoded_token = jwt.decode(token, 'U0hPVVRFUl9BQ0NFU1NfVE9LRU5fc2hvdXRzb2x1dGlvbkAyMDIw', algorithms='HS256')
  email = decoded_token['email']

  # User
  user = User.objects.filter(username=email).first()
  user.is_active = True
  user.save()

  # Brand
  brand = BrandProfile.objects.filter(email=email).first() 
  brand.is_active = True
  brand.save()

  return render(request, 'accounts/email_confirm.html', context={'email': email})
