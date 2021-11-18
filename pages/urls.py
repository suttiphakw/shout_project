from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
  path('dev/', views.dev, name='on_dev')
]