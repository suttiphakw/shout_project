from django.urls import path

from . import views


urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('register/', views.register, name='shouters-register'),
    path('login/', views.login, name='shouters-login'),
    path('logout/', views.logout, name='shouter-logout'),
    path('info-2/', views.register_info_2, name='info-2'),
    path('info-3/', views.register_info_3, name='info-3'),
    path('info-4/', views.register_info_4, name='info-4'),
    path('info-5/', views.register_info_5, name='info-5'),
    path('info-6/', views.register_info_6, name='info-6'),
    path('wfa/', views.waiting_for_approve, name='wfa'),
    path('facebook-login/', views.facebook_login, name='facebook-login'),
    path('oauth2/', views.oauth2, name='oauth2'),
]