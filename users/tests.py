from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Profile
from .forms import UserRegisterForm

class UsersAppTests(TestCase):
    def test_registration_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('profile'))

    def test_user_register_form_valid(self):
        form_data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_model(self):
        user = User.objects.create_user(
            username='testuser3',
            email='testuser3@example.com',
            password='testpassword'
        )
        profile = Profile.objects.get(user=user)
        self.assertEqual(str(profile), 'testuser3 Profile')
