from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import Main, Posts, post, About, Contact, Thanks
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Main),
    url(r'^blog/$', Posts),
    url(r'^about/$', About),
    url(r'^contact/$', Contact),
    url(r'^contact/thanks/$', Thanks),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/(?P<slug>[-\w]+)/$', post),
	url(r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()