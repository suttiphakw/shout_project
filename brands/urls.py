from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='brand__index'),

  # CAMPAIGN MANAGEMENT
  path('campaigns/', views.campaigns, name='brand__campaign'),
  
  # CREATE CAMPAIGN
  path('campaigns/create/name/', views.create_name, name='brand__create_name'),
  path('campaigns/create/scope_budget/', views.create_scope_budget, name='brand__create_scope_budget'),
  path('campaigns/create/content_type/', views.create_content_type, name='brand__create_content_type'),
]