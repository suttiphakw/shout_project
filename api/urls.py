from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='api_index'),
  path('login/', views.login, name='api_login'),

  path('flex/', views.flex, name='api_flex'),
  path('flex/main/campaign_detail_delivery/', views.main_campaign_detail_delivery, name='flex_main_campaign_detail_delivery'),
  path('flex/main/campaign_detail_no_delivery/', views.main_campaign_detail_no_delivery, name='flex_main_campaign_detail_no_delivery'),
  path('flex/main/wait_delivery/', views.main_wait_delivery, name='flex_main_wait_delivery'),
  path('flex/main/delivery_complete/', views.main_delivery_complete, name='flex_main_delivery_complete'),
  path('flex/main/draft/', views.main_draft, name='flex_main_draft'),
  path('flex/main/sent_draft/', views.main_sent_draft, name='flex_main_sent_draft'),
  path('flex/main/revise_draft/', views.main_revise_draft, name='flex_main_revise_draft'),
  path('flex/main/approve_draft/', views.main_approve_draft, name='flex_main_approve_draft'),
  path('flex/main/sent_work/', views.main_sent_work, name='flex_main_sent_work'),
  path('flex/main/wait_check_work/', views.main_wait_check_work, name='flex_main_wait_check_work'),
  path('flex/main/finish/', views.main_finish, name='flex_main_finish'),
  path('flex/main/payment/', views.main_payment, name='flex_main_payment'),

  path('flex/add/reject_work/', views.add_reject_work, name='flex_add_reject_work'),
  path('flex/add/cancel_work/', views.add_cancel_work, name='flex_add_cancel_work'),
  path('flex/add/reconnect/', views.add_reconnect, name='flex_add_reconnect'),
  path('flex/add/text/', views.add_text_message, name='flex_add_text_message'),

  path('upload/campaign_detail_logo/', views.upload_campaign_detail_logo, name='upload_campaign_detail_logo'),
  path('upload/campaign_detail_reference/', views.upload_campaign_detail_reference, name='upload_campaign_detail_reference'),

  path('insights/story/', views.insights_story, name='api_insights_story'),
  path('insights/post/', views.insights_post, name='api_insights_post'),
  path('insights/reel/', views.insights_reel, name='api_insights_reel'),
]