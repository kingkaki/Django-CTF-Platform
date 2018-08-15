# -*- coding: utf-8 -*-
# @Author: kingkk
# @Date:   2018-08-15 12:02:17
# @Last Modified by:   kingkk
# @Last Modified time: 2018-08-15 17:59:48

from django import forms
from django.forms import widgets, ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from .models import *

class RegisterForm(forms.Form):
	username = forms.CharField(
		label="用户名", 
		required=True, 
		min_length=3, 
		max_length=20, 
		widget=widgets.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Username',
		}),
	)
	password = forms.CharField(
		label="密码", 
		required=True, 
		min_length=5, 
		max_length=20,
		widget=widgets.PasswordInput(attrs={
			'class':'form-control',
			'placeholder':'Password',
		}),
	)
	password_repeat = forms.CharField(
		label="确认密码", 
		required=True, 
		min_length=5, 
		max_length=20,
		widget=widgets.PasswordInput(attrs={
			'class':'form-control',
			'placeholder':'Repate Password',
		}),
	)
	invitation_code = forms.CharField(
		label="邀请码（联系管理员获取）", 
		required=True,
		widget=widgets.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Invitation Code',
		}),
	)

	def clean(self):
		if self.cleaned_data['password'] != self.cleaned_data['password_repeat'] :
			raise ValidationError("两次密码不一致")
		else:
			self.cleaned_data['password'] = make_password(self.cleaned_data['password'])
			return self.cleaned_data


	def clean_username(self):
		num = Player.objects.filter(username=self.cleaned_data['username']).count()
		if num != 0:
			raise ValidationError('用户已被注册')
		return self.cleaned_data['username']


	def clean_invitation_code(self):
		try :
			code = InvitationCode.objects.get(code=self.cleaned_data['invitation_code'])
		except InvitationCode.DoesNotExist:
			raise ValidationError("邀请码无效")

		if code.is_valid != True:
			raise ValidationError("邀请码已被使用")
		return code

class LoginForm(forms.Form):
	username = forms.CharField(
		label="用户名",
		required=True,
		widget=widgets.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Username',
		}),
	)

	password = forms.CharField(
		label="密码",
		required=True,
		widget=widgets.PasswordInput(attrs={
			'class':'form-control',
			'placeholder':'Password',
		}),
	)

	def clean(self):
		user = authenticate(
			username = self.cleaned_data['username'],
			password = self.cleaned_data['password']
		)
		if user is None:
			raise ValidationError("用户名或密码错误")
		else:
			return user



			
