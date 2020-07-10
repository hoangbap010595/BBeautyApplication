from django.urls import path, include

urlpatterns = [
    path(r'account/', include('apps.account.api.account.urls')),
]
