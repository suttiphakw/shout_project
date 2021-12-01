from django.urls import path

from . import views


urlpatterns = [
    # Shouter Pages
    path('', views.landing_page, name='landing-page'),
    # Register and Login
    path('login/', views.login, name='shouters-login'),
    path('logout/', views.logout, name='shouter-logout'),
    path('register/', views.register, name='shouters-register'),
    path('register/info-1/', views.register__info_1, name='register__info-1'),
    path('register/info-2/', views.register__info_2, name='register__info-2'),
    path('register/info-3/', views.register__info_3, name='register__info-3'),
    path('register/info-4/', views.register__info_4, name='register__info-4'),
    path('register/info-5/', views.register__info_5, name='register__info-5'),
    path('register/info-6/', views.register__info_6, name='register__info-6'),
    path('register/account_summary/', views.register__account_summary, name='register__account_summary'),
    path('register/work_selection/', views.register__work_selection, name='register__work_selection'),
    path('register/finished/', views.register__finished, name='register__finished'),
    path('wfa/', views.waiting_for_approve, name='wfa'),


    # Line Login and oauth
    #
    # Facebook Login + Logout and oauth
    path('facebook-login/', views.facebook_login, name='facebook-login'),
    path('facebook-logout/', views.facebook_logout, name='facebook-logout'),
    path('oauth2/', views.oauth2, name='oauth2'),
    # Shouter Menu
    path('menu/', views.menu, name='shouter__menu'),
    path('menu/social-media/', views.menu__social_media, name='shouter__menu__social-media'),


]