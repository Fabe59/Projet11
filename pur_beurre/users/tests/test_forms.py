from django.test import TestCase
from users.forms import CustomUserCreationForm


class Users_Form_TestCase(TestCase):

    def test_user_creation_forms_is_valid(self):
        form = CustomUserCreationForm(data={
            "username": "Paulo",
            "email": "paulo@free.fr",
            "password1": "Purbeurre2020",
            "password2": "Purbeurre2020"
            })
        self.assertTrue(form.is_valid())

    def test_user_creation_forms_is_not_valid(self):
        form = CustomUserCreationForm(data={
            "username": "Paulo",
            "email": "paulo@free.fr",
            "password1": "Purbeurre2020",
            "password2": "Azerty"
        })
        self.assertFalse(form.is_valid())

    def test_user_creation_forms_email_is_not_valid(self):
        form = CustomUserCreationForm(data={
            "username": "Paulo",
            "email": "Paulo.fr",
            "password1": "Purbeurre2020",
            "password2": "Purbeurre2020"
        })
        self.assertFalse(form.is_valid())
