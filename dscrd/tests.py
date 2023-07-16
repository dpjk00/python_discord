from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Channel, Topic, Message

# Create your tests here.

class ViewsTestCase(TestCase):
    def test_url(self):
        response = self.client.get("/channels")
        self.assertEqual(response.status_code, 404)

class SignInTest(TestCase):
    def set_up(self):
        self.user = User.objects.create_user(username="test", password="strong123")
        self.user.save()

    def tear_down(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='user', password='strong123')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)