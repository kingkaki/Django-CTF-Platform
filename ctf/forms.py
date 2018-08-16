# -*- coding: utf-8 -*-
# @Author: kingkk
# @Date:   2018-08-16 17:15:33
# @Last Modified by:   kingkk
# @Last Modified time: 2018-08-16 17:16:51
from django import forms
from django.forms import widgets, ValidationError
from .models import *

class TopicForm(forms.Form):
	flag = forms.CharField(
		required=True,
		widget=widgets.TextInput(attrs={
			'class':'form-control',
		}),
	)
