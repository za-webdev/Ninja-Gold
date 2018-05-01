from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index),
	url(r'^gold_here$',views.gold_here),
	url(r'^reset$',views.reset)
]