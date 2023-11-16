from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class LoginTestCase(TestCase):


    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='pass')
        self.client.login(username='user', password='pass')


    def test_login_view(self):
        response = self.client.get(reverse('login'))
        print(response)
        self.assertEqual(response.status_code, 200)

        