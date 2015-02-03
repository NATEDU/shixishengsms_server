from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shixisheng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'shixisheng.views.home', name='home'),
    url(r'^display_sms/(\d+)$', 'shixisheng.views.display'),
    url(r'^d/(\d+)$', 'shixisheng.views.d'),
    url(r'^new$', 'shixisheng.views.new'),

    url(r'^admin/', include(admin.site.urls)),

)
