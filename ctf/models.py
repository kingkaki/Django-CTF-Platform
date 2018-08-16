import datetime

from django.db import models
from django.utils import timezone
from player.models import Player

# Create your models here.
class Competition(models.Model):
	name = models.CharField('赛事名称', max_length=50, default="")
	description = models.TextField('赛事描述', default="", blank=True)
	start_time = models.DateTimeField('开赛时间')
	end_time = models.DateTimeField('结束时间')

	def __str__(self):
		return self.name

class Topic(models.Model):
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
	name = models.CharField('赛题名称', max_length=50, default="")
	address = models.CharField("比赛地址", max_length=50, default="", blank=True)
	description = models.TextField('题目描述', default="", blank=True)
	score = models.IntegerField("分值", default=0)
	solve_num = models.IntegerField("解题人数", default=0)
	flag = models.CharField("flag", max_length=64, default="", blank=True)
	in_progress = models.BooleanField("是否正在进行", default=False)
	release_time= models.DateTimeField('放出时间')
	topic_type = models.CharField("题目类型", max_length=10,blank=True,choices=(
		('Web','Web'),
		('Pwn','Pwn'),
		('Reverse', 'Reverse'),
		('Crypto', 'Crpyto'),
		('Mobile', 'Mobile'),
		('Misc', 'Misc'),
	))


class Status(models.Model):
	topic = models.ForeignKey(Competition, on_delete=models.CASCADE)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	solve_time = models.DateTimeField('解题时间')
	score = models.IntegerField("题目分值", default=0)
