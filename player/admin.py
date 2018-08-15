from django.contrib import admin

from .models import *

class PlayerAdmin(admin.ModelAdmin):
	# fieldsets = [
	# 	(None,	{'fields':['username']})
	# ]
	list_display = ('username','date_joined')

class InvitationCodeAdmin(admin.ModelAdmin):
	list_display = ('code', 'is_valid', 'register_user')
	verbose_name='邀请码'


admin.site.register(Player, PlayerAdmin)
admin.site.register(InvitationCode, InvitationCodeAdmin)