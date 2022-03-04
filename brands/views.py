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
def create_campaigns(requests):
  return render(requests, 'brands/campaigns_create.html')