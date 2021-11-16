from django.urls import path
from shouters.views import \
    register, \
    login, \
    Oauth, \
    Oauth2, \
    fb_login, \
    payment, \
    history, \
    setting

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('login/', login, name='shouters_login'),
    path('Oauth/', Oauth, name='line_api'),
    path('Oauth2/', Oauth2, name='fb_api'),
    # path('<str:user_id>/'),
    path('<int:_id>/register/', register, name='shouters_register'),
    path('<int:_id>/fb_login/', fb_login, name='fb_login'),
    path('<int:_id>/payment/', payment, name='payment'),
    path('<int:_id>/history/', history, name='history'),
    path('<int:_id>/setting/', setting, name='setting'),
]