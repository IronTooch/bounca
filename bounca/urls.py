"""Main URL config"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from api.urls import urlpatterns as urlpatterns_api


urlpatterns = [
    url(r'^api/', include(urlpatterns_api)),
    url(r'^auth/', include('rest_framework.urls')),
    url('^account/account_email_verification_sent', TemplateView.as_view(), name='account_email_verification_sent'),
]

if settings.DEBUG:
    # admin site is only available if running debug mode
    urlpatterns += [
        url(r'^admin/', admin.site.urls),
        url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    ]


urlpatterns += staticfiles_urlpatterns()
