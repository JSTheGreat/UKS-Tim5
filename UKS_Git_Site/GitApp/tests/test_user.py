
from django.test import TestCase, Client
from django.urls import reverse

from ..models import User
# # Create your tests here.


class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'user1'
        self.password = 'user1'
        self.user = User.objects.create(
            username=self.username,
            password=self.password
        )
    def test_login_positive(self):
        login_url = reverse('login')  # Replace 'login' with your actual login URL name
        response = self.client.post(login_url, {'username': self.username, 'password': self.password})
        # self.assertEqual(response.status_code, 302)  # Check for a redirect status code (302)
        # self.assertRedirects(response, reverse('index'))  # Replace 'index' with the actual URL name of the redirect target
        # self.assertFalse(response.context['user'].is_authenticated)

    # def test_login_negative(self):
    #     response = self.client.post('/login/', self.wrong_user, follow=True)
    #     self.assertFalse(response.context['user'].is_authenticated)