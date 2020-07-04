from django.conf.urls import include, url
from apps.system.urls import dashboard

app_name = 'system'

urlpatterns = [
    url('', include(dashboard)),
    # url(r'^dashboard/', include(dashboard)),
]
