from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    # path('register/', user_views.RegisterView.as_view(), name='users-register'),
    path('profile/', user_views.profile, name='account-profile'),
    path('login/', user_views.LoginView.as_view(), name='account-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'),
         name='account-logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html',
                                                                subject_template_name='account/password_reset_subject.txt',
                                                                html_email_template_name='account/password_reset_email.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete')
]
