from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
	description = models.TextField('个人简介', default="")
	avatar = models.ImageField('头像',upload_to='avatars/', default='avatars/default.jpg',max_length=100)
	last_login = models.DateTimeField('最后登录时间', default=datetime.now())

	def __str__(self):
		return self.username


class InvitationCode(models.Model):
	code = models.CharField('邀请码', max_length=64)
	register_user = models.CharField('注册人', max_length=20, default="", blank=True)
	is_valid = models.BooleanField('是否有效', default=True)