from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(requests):
  return render(requests, 'brands/index.html')


@login_required()
def campaigns(requests):
  return render(requests, 'brands/campaigns.html')


@login_required()
def create_name(requests):
  return render(requests, 'brands/create/name.html')

@login_required()
def create_scope_budget(requests):
  return render(requests, 'brands/create/scope_budget.html')

@login_required()
def create_content_type(requests):
  return render(requests, 'brands/create/content_type.html')