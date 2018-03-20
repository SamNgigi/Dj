from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^apiSerializer/$', views.api_list, name='apiSerializer_list'),
    url(r'^apiSerializerDetail/(?P<pk>[0-9]+)/$', views.api_detail,
        name='apiSerializer_detail'),
]
