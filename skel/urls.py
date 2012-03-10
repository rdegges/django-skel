from dajaxice.core import dajaxice_autodiscover
from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url


# See: https://docs.djangoproject.com/en/1.3/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: http://docs.dajaxproject.com/dajaxice/installation.html#configure-dajaxice-url
dajaxice_autodiscover()


# See: https://docs.djangoproject.com/en/1.3/topics/http/urls/
urlpatterns = patterns('',
    # AJAX URLs:
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
