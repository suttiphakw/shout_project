from django.urls import path

from .views import campaigns

urlpatterns = [
  path('campaigns/create/name/', campaigns.api_name, name='api_name_post'),
  path('campaigns/create/scope_budget/<int:campaign_id>/', campaigns.api_scope_budget, name='api_scope_budget'),
  path('campaigns/create/content_type/<int:campaign_id>/', campaigns.api_content_type, name='api_content_type'),

  # path('campaigns/create/name/', campaigns.api_name, name='api_name'),
  # path('campaigns/create/scope_budget/<int:campaign_id>/', campaigns.api_scope_budget, name='api_scope_budget')
]
