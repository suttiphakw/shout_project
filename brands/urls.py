from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='brand__index'),

  # CAMPAIGN MANAGEMENT
  path('campaigns/', views.campaigns, name='brand__campaign'),
  path('campaigns/create/', views.create_campaigns, name='brand__campaign_create'),
]