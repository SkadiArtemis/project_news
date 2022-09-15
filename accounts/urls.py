from django.urls import path
from .views import (BaseRegisterView,
                    upgrade_me,
                    add_subscribe,
                    subscribe_user)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup_page.html'),
         name='signup_page'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('subscribe/', add_subscribe, name='subscribe'),
    path('subscribe_user/', subscribe_user, name='subscribe_user')
]