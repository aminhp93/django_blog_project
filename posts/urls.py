from django.conf.urls import url

from .views import (post_create, post_detail, post_list, post_update, post_delete)

urlpatterns = [
	url(r'^create/$', post_create, name='create'),
	url(r'^detail/$', post_detail, name='detail'),
	url(r'^$', post_list, name='list'),
	url(r'^update/$', post_update, name='update'),
	url(r'^delete/$', post_detail, name='delete'),
]