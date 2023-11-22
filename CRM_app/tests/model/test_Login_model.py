from django.test import TestCase
from django.contrib.auth.models import User


class LoginTestCase(TestCase):
    def loginModelTest(self):
        user = User.objects.create_user(username='user', password='pass')

        self.assertEqual(user.username, 'user')
        self.assertEqual(user.password, 'pass')
        