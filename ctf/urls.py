# -*- coding: utf-8 -*-
# @Author: kingkk
# @Date:   2018-08-16 13:54:40
# @Last Modified by:   kingkk
# @Last Modified time: 2018-08-16 22:29:08
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'ctf'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	url(r'^competition/(?P<competition_name>.*)/$',views.CompetitionView.as_view(),name='competition'),
	url(r'^topic/(?P<topic_id>.*)/$',views.TopicView.as_view(),name='topic'),
]
