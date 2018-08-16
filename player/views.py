from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import ValidationError

from .forms import *
from Django_CTF_Platform.settings  import MEDIA_ROOT
from .models import *

# Create your views here.
class IndexView(View):
	@method_decorator(login_required)
	def get(self, request):
		return render(request, 'player/index.html')



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
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data
			login(request, user)
			user.last_login = datetime.now()
			user.save()
			return HttpResponseRedirect(reverse('player:index'))
		else:
			return render(request, 'player/login.html', {'form':form})

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('player:login'))

class EditView(View):
	@method_decorator(login_required)
	def get(self, request):
		form = EditForm()
		return render(request, 'player/edit.html', {'form':form})

	@method_decorator(login_required)
	def post(self, request):
		from os import path
		form = EditForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data

			# des处理
			user = Player.objects.get(pk=request.user.id)
			user.description = data['description']
			user.save()

			# 头像上传
			if data['avatar'] != None:
				suffix = path.splitext(data['avatar'].name)[1]
				rel_path = path.join('avatars', str(user.id)+suffix)
				with open(path.join(MEDIA_ROOT, rel_path), 'wb') as f:
					for chunk in data['avatar'].chunks():
						f.write(chunk)
				user.avatar = rel_path

			user.save()
			request.user = user
			return render(request, 'player/edit.html', {'form':form})
		else:
			raise ValidationError("error")





