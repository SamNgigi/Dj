from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^$', views.band, name='band'),
    url(r'^(?P<id>\d+)$', views.single, name='single'),
    url(r'^api/(?P<pk>\d+)$',
        views.BandDetail.as_view(), name='band_details_api'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
