from django.conf.urls import patterns, url
from django.contrib.flatpages import views
from blog.views import archive

urlpatterns = patterns('',
    url(r'^$', archive),
)