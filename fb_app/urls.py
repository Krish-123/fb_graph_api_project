from django.urls import path
from . import views

app_name = 'fb_app'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('fblogin/',views.fb_login,name='fb_login'),
    path('postlogin/',views.login_redirect,name='login_redirect'),
    path('access_token/',views.access_token,name='access_token'),
]
