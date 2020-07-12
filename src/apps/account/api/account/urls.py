from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('profile', views.profile),
    path('change-password', views.chang_password),
]
