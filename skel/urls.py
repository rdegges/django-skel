from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url


# See: https://docs.djangoproject.com/en/1.3/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skel.views.home', name='home'),
    # url(r'^skel/', include('skel.foo.urls')),

    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
