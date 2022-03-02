from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from brands.models import BrandProfile

# Create your views here.
def register(request):
  if request.method == 'POST':
    # Get Info
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    tel =request.POST['tel']
    company = request.POST['company']
    position = request.POST['position']
    password_1 = request.POST['password_1']
    password_2 = request.POST['password_2']
    print(email, password_1, password_2)
    # Is Password Match
    if password_1 == password_2:
      # Is Email is already taken
      if User.objects.filter(username=email).exists():
        messages.error(request, 'This email is already register')
        return redirect('register')
      else:
        # Look good
        user = User.objects.create_user(username=email, password=password_1, first_name=first_name, last_name=last_name, email=email)
        user.save()
        brand = BrandProfile.objects.create(user=user, email=email, first_name=first_name, last_name=last_name, tel=tel, company=company, position=position)
        brand.save()
        return redirect('login')
    else:
      messages.error(request, 'Password do not match')
      return redirect('register')
  return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    # Get Info
    email = request.POST['email']
    password = request.POST['password']
    user = auth.authenticate(username=email, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('brand__home')
    else:
      messages.error(request, 'Incorrect email or password')
      return redirect('login')
  return render(request, 'accounts/login.html')


def logout(request):
  auth.logout(request)
  return redirect('index')