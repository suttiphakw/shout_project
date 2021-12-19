from django.urls import path

from . import views


urlpatterns = [
    # Shouter Pages
    path('', views.landing_page, name='shouter__index'),

    # Register and Login
    # path('login/', views.login, name='shouters-login'),
    # path('logout/', views.logout, name='shouter-logout'),
    path('register/<str:token>/', views.register, name='shouter__register'),
    path('register/info-1/<str:token>/', views.register__info_1, name='shouter__register__info-1'),
    path('register/info-2/<str:token>/', views.register__info_2, name='shouter__register__info-2'),
    path('register/info-3/<str:token>/', views.register__info_3, name='shouter__register__info-3'),
    path('register/info-4/<str:token>/', views.register__info_4, name='shouter__register__info-4'),
    path('register/info-5/<str:token>/', views.register__info_5, name='shouter__register__info-5'),
    path('register/info-6/<str:token>/', views.register__info_6, name='shouter__register__info-6'),
    path('register/choose-instagram/<str:token>/', views.register__choose_instagram, name='shouter__register__choose_instagram'),
    path('register/work-selection/<str:token>/', views.register__work_selection, name='shouter__register__work_selection'),
    path('register/account-summary/<str:token>/', views.register__account_summary, name='shouter__register__account_summary'),
    path('register/finished/<str:token>/', views.register__finished, name='shouter__register__finished'),
    path('wfa/', views.waiting_for_approve, name='wfa'),

    # Line Login and oauth
    path('line-login/', views.line_login, name='shouter__line-login'),
    path('oauth/', views.oauth, name='shouter__oauth'),

    # Facebook Login + Logout and oauth
    path('facebook-login/<str:token>/', views.facebook_login, name='shouter__facebook-login'),
    path('facebook-logout/<str:token>/', views.facebook_logout, name='shouter__facebook-logout'),
    path('oauth2/', views.oauth2, name='shouter__oauth2'),

    # Shouter Menu
    path('menu/<str:token>/', views.menu, name='shouter__menu'),
    path('menu/social-media/<str:token>/', views.menu__social_media, name='shouter__menu__social-media'),
    path('menu/bank-account/<str:token>/', views.menu__bank_account, name='shouter__menu__bank-account'),
]