from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('forget_password/', views.forget_password, name='forget_password'),
  path('forget_password/email/<str:token>/', views.forget_password_email, name='forget_password_email'),
  path('forget_password/change/<str:token>/', views.change_password, name='change_password'),
  # path('forget_password/change/<str:token>/', views.change_password, name='change_password'),
  path('forget_password/complete/<str:token>/', views.change_password_complete, name='change_password_complete'),

  # Confirm Email
  path('email/verification/<str:token>/', views.email_verification, name='email_verification'),
  path('email/confirm/<str:token>/', views.email_confirm, name='email_confirm'),
]