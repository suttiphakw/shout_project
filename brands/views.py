from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
  return render(request, 'brands/index.html')

@login_required()
def settings(request):
  return render(request, 'brands/settings.html')

@login_required()
def change_password(request):
  return render(request, 'brands/change_password.html')

# @login_required()
# def create_name(request):
#   return render(request, 'brands/create/name.html')

# @login_required()
# def create_scope_budget(request):
#   return render(request, 'brands/create/scope_budget.html')

# @login_required()
# def create_content_type(request):
#   return render(request, 'brands/create/content_type.html')