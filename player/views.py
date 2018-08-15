from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from .forms import *
from .models import *

# Create your views here.
class IndexView(View):
	def get(self, request):
		return HttpResponse('hello %s!' % request.user.username) 

class RegisterView(View):
	def get(self, request):
		form = RegisterForm()
		return render(request, 'player/register.html',{
			'form':form,
		})

	def post(self, request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data

			# 注册用户
			player = Player()
			player.username = data['username']
			player.password = data['password']
			player.save()

			# 注册码
			code = data['invitation_code']
			code.register_user = data['username']
			code.is_valid = False
			code.save()

			return HttpResponseRedirect(reverse('player:login'))
		else:
			message = 'error'
			return render(request, 'player/register.html', {
				'form': form,
				'message': message,
			})


class LoginView(View):
	def get(self, request):
		form = LoginForm()
		return render(request, 'player/login.html', {'form':form})

	def post(self, request):
		form = form = LoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data
			login(request, user)
			return HttpResponseRedirect(reverse('player:index'))
		else:
			return render(request, 'player/login.html', {'form':form})

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponse('登出')