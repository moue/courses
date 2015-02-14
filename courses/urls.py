from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from ajax_select import urls as ajax_select_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'courses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^foundation/', include('foundation.urls')),
    url(r'^$', 'catalog.views.index'),
)
