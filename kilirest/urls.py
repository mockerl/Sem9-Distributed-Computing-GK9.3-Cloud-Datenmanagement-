from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^snippets/$', views.user_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.user_detail),
]