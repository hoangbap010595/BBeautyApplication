from . import views
from django.urls import path

urlpatterns = [
    path('', views.test),
    path('test_post', views.test_post),
]
