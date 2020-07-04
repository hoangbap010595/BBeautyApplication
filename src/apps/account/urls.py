from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    # path('register/', user_views.RegisterView.as_view(), name='users-register'),
    path('login/', user_views.LoginView.as_view(), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/login.html'),name='users-logout'),
]