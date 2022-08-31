from django.urls import path

from . import views

urlpatterns = [
  path('draft/', views.campaign_draft, name='campaign_draft'),
  path('in_progress/', views.campaign_in_progress, name='campaign_in_progress'),
  path('finished/', views.campaign_finished, name='campaign_finished'),
  
  # CREATE CAMPAIGN
  path('create/name/', views.create_name, name='create_name'),
  path('create/scope_budget/<int:campaign_id>/', views.create_scope_budget, name='create_scope_budget'),
  path('create/content_type/<int:campaign_id>/', views.create_content_type, name='create_content_type'),
  path('create/product/<int:campaign_id>/', views.create_product, name='create_product'),
  path('create/target/<int:campaign_id>/', views.create_target, name='create_target'),
  path('create/shouter_selection/<int:campaign_id>/', views.create_shouter_selection, name='create_shouter_selection'),
  path('create/shouter_selection_2/<int:campaign_id>/', views.create_shouter_selection, name='create_shouter_selection_2'),
  path('create/operation/brand_delivery/<int:campaign_id>/', views.create_operation_brand_delivery, name='create_operation_brand_delivery'),
  path('create/operation/shout_delivery/<int:campaign_id>/', views.create_operation_shout_delivery, name='create_operation_shout_delivery'),
  path('create/operation/self_buy/<int:campaign_id>/', views.create_operation_self_buy, name='create_operation_self_buy'),
  path('create/operation/web_app/<int:campaign_id>/', views.create_operation_web_app, name='create_operation_web_app'),
  path('create/operation/go_review/<int:campaign_id>/', views.create_operation_go_review, name='create_operation_go_review'),
  path('create/brief/<int:campaign_id>/', views.create_brief, name='create_brief'),

  path('create/summary/<int:campaign_id>/', views.campaign_summary, name='campaign_summary'),
]
