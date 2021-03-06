from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('login.urls', namespace='account')),
]
