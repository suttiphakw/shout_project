from django.urls import path

from . import views

urlpatterns = [
  path('shouter_score/<int:campaign_id>/', views.shouter_score, name='shouter_score'),
]