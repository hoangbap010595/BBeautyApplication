from django.urls import path, include
from apps.system.views import dashboard

urlpatterns = [
    path('', dashboard.index, name='dashboard-index'),
]
