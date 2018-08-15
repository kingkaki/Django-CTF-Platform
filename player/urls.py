# -*- coding: utf-8 -*-
# @Author: kingkk
# @Date:   2018-08-15 10:24:41
# @Last Modified by:   kingkk
# @Last Modified time: 2018-08-15 17:56:40

from django.urls import path

from . import views

app_name = 'player'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('register/', views.RegisterView.as_view(), name='register'),
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
]
