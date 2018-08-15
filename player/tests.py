from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import *

# Create your tests here.
class RegisterViewTests(TestCase):

	def test_password_not_match(self):
		res = self.client.post(reverse('player:register'), data={
				'username' : 'aaaaaa',
				'password' : 'aa',
				'password_repeat' : 'aaaaaa',
				'invitation_code' : 'a',
			})
		self.assertContains(res, '邀请码无效')