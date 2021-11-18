from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('register/<int:_id>/', views.register, name='shouters_register'),
    path('register/info-1/', views.register_info_1, name='regis-info-1'),
    path('register/info-2/<int:_id>/', views.register_info_2, name='regis-info-2'),
    path('register/info-3/<int:_id>/', views.register_info_3, name='regis-info-3'),
    path('register/info-4/<int:_id>/', views.register_info_4, name='regis-info-4'),
    path('register/info-5/<int:_id>/', views.register_info_5, name='regis-info-5'),
    path('register/info-6/<int:_id>/', views.register_info_6, name='regis-info-6'),
    path('line-login/', views.line_login, name='shouters_login'),
    path('oauth/', views.oauth, name='line_auth'),
    path('facebook-login/', views.facebook_login, name='facebook_login'),
    # path('oauth2/', views.oauth2, name='facebook_auth'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', login, name='shouters_login'),
    # path('Oauth/', Oauth, name='line_api'),
    # path('Oauth2/', Oauth2, name='fb_api'),
    # # path('<str:user_id>/'),
    # path('<int:_id>/register/', register, name='shouters_register'),
    # path('<int:_id>/fb_login/', fb_login, name='fb_login'),
    # path('<int:_id>/payment/', payment, name='payment'),
    # path('<int:_id>/history/', history, name='history'),
    # path('<int:_id>/setting/', setting, name='setting'),
]