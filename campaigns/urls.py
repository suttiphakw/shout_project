from django.urls import path

from . import views

urlpatterns = [
  path('draft/', views.campaign_draft, name='campaign_draft'),
  path('in_progress/', views.campaign_in_progress, name='campaign_in_progress'),
  path('finished/', views.campaign_finished, name='campaign_finished'),
  
  # CREATE CAMPAIGN
  path('create/name/', views.create_name, name='create_name'),
  path('create/scope_budget/', views.create_scope_budget, name='create_scope_budget'),
  path('create/content_type/', views.create_content_type, name='create_content_type'),
  path('create/product/', views.create_product, name='create_product'),
  path('create/target/', views.create_target, name='create_target'),
  path('create/shouter_selection/', views.create_shouter_selection, name='create_shouter_selection'),
]