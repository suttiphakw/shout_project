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
    path('register/choose-device/<str:token>/', views.register__choose_device, name='shouter__register__choose-device'),
    path('register/facebook-checkbox/<str:token>/', views.register__facebook_checkbox, name='shouter__register__facebook-checkbox'),
    path('register/facebook-error-1/<str:token>/', views.register__connect_facebook_error_1, name='shouter__register__connect-facebook-error-1'),
    path('register/facebook-error-2/<str:token>/', views.register__connect_facebook_error_2, name='shouter__register__connect-facebook-error-2'),
    path('register/facebook-change/<str:token>/', views.register__connect_facebook_change, name='shouter__register__connect-facebook-change'),
    path('register/choose-instagram/<str:token>/', views.register__choose_instagram, name='shouter__register__choose_instagram'),
    path('register/work-selection/<str:token>/', views.register__work_selection, name='shouter__register__work_selection'),
    path('register/account-summary/<str:token>/', views.register__account_summary, name='shouter__register__account_summary'),
    path('register/finished/<str:token>/', views.register__finished, name='shouter__register__finished'),
    path('wfa/', views.waiting_for_approve, name='wfa'),
    # IG API => Get Data
    path('register/ig-api/<str:token>/', views.register__get_ig_data, name='shouter__register__get-ig-data'),

    # Line Login and oauth
    path('line-login/', views.line_login, name='shouter__line-login'),
    path('oauth/', views.oauth, name='shouter__oauth'),

    # Facebook Login + Logout and oauth
    path('instagram-login/<str:token>/', views.facebook_login, name='shouter__facebook-login'),
    path('instagram-logout/<str:token>/', views.facebook_logout, name='shouter__facebook-logout'),
    path('oauth2/', views.oauth2, name='shouter__oauth2'),

    # Shouter Menu
    path('menu/<str:token>/', views.menu, name='shouter__menu'),
    path('menu/edit-profile/<str:token>/', views.menu__edit_profile, name='shouter__menu__edit-profile'),
    path('menu/social-media/<str:token>/', views.menu__social_media, name='shouter__menu__social-media'),
    path('menu/work-selection/<str:token>/', views.menu__work_selection, name='shouter__menu__work-selection'),
    path('menu/bank-account/<str:token>/', views.menu__bank_account, name='shouter__menu__bank-account'),

    # Your campaign
    path('campaign/<str:token>/', views.campaign, name='shouter__campaign'),

    # Your Payment
    path('payment/<str:token>/', views.payment, name='shouter__payment'),

    # Error Page
    path('not-fount-user/', views.not_found_user, name='shouter__not_fount_user')
]