# -*- coding: utf-8 -*-
# @Author: kingkk
# @Date:   2018-08-16 13:54:40
# @Last Modified by:   kingkk
# @Last Modified time: 2018-08-16 13:55:33
from django.urls import path

from . import views

app_name = 'ctf'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
]
