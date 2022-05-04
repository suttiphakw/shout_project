from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
  path('insights/', views.insights, name='api_insights'),
]