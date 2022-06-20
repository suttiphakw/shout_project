from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BrandProfile


# Create your views here.
@login_required()
def index(request):
  return render(request, 'brands/index.html')


@login_required()
def settings(request):
  user = request.user

  # Query BrandProfile
  brand = BrandProfile.objects.filter(user=user)
  if brand.count() == 1:
    brand = brand.first()
  context = {
    'brand': brand
  }

  # request method == post
  if request.method == "POST":
    brand.first_name = request.POST['first_name']
    brand.last_name = request.POST['last_name']
    brand.tel = request.POST['tel']
    brand.company = request.POST['company']
    brand.position = request.POST['position']
    brand.save()
    messages.success(request, 'Your profile have been change')

  return render(request, 'brands/settings.html', context)


@login_required()
def change_password(request):
  user = request.user

  # Query BrandProfile
  brand = BrandProfile.objects.filter(user=user)
  if brand.count() == 1:
    brand = brand.first()
  context = {
    'brand': brand
  }

  if request.method == "POST":
    old_password = request.POST['old_password']
    new_password_1 = request.POST['new_password_1']
    new_password_2 = request.POST['new_password_2']
    if new_password_1 != new_password_2:
      messages.error(request, 'New password do not match')
      return redirect('brand__setttings_change_password')
    if not user.check_password(old_password):
      messages.error(request, 'Wrong password')
      return redirect('brand__setttings_change_password')

    user.set_password(new_password_1)
    user.save()
    messages.success(request, 'Your password have been change')

  return render(request, 'brands/change_password.html', context)
