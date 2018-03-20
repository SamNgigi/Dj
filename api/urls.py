from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(
        r'^apiSerializer/$',
        views.ApiTestList.as_view(),
        name='apiSerializer_list'
    ),
    url(
        r'^apiSerializerDetail/(?P<pk>[0-9]+)/$',
        views.ApiTestDetails.as_view(),
        name='apiSerializer_detail'
    ),
    # url(r'^apiSerializer/$', views.api_list, name='apiSerializer_list'),
    # url(r'^apiSerializerDetail/(?P<pk>[0-9]+)/$', views.api_detail,
    #     name='apiSerializer_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
