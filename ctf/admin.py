from django.contrib import admin

from .models import *
# Register your models here.

class TopicInline(admin.StackedInline):
	model = Topic
	extra = 1

class CompetitionAdmin(admin.ModelAdmin):
	inlines = [TopicInline]



admin.site.register(Competition, CompetitionAdmin)