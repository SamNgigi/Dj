from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import views

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
urlpatterns = format_suffix_patterns(urlpatterns)
