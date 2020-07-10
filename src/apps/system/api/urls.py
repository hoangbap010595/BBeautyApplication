from django.urls import path, include

urlpatterns = [
    path(r'test/', include('apps.system.api.test.urls')),
]
