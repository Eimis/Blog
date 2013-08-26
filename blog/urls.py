from django.conf.urls import patterns, include, url
from blog.views import Hello
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', Hello),
    url(r'^admin/', include(admin.site.urls)),
)