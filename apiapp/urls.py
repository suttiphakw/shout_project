from django.urls import path

from .views import campaigns

urlpatterns = [
  path('campaigns/create/name/', campaigns.api_name, name='api_name_post'),
  path('campaigns/create/scope_budget/<int:campaign_id>/', campaigns.api_scope_budget, name='api_scope_budget'),
  # path('campaigns/create/name/', campaigns.CampaignNameView.as_view(), name='test_apiapp'),
  # path('campaigns/create/name/', campaigns.api_name, name='api_name'),
  # path('campaigns/create/scope_budget/<int:campaign_id>/', campaigns.api_scope_budget, name='api_scope_budget')
]
