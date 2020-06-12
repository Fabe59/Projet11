from django.test import TestCase
from django.urls import reverse, resolve
from users.views import create, profile, fav, delete_fav
from django.contrib.auth import views as auth_views


class Users_Url_Test(TestCase):

    def test_create_url_resolves(self):
        url = reverse('users:create')
        self.assertEquals(resolve(url).func, create)

    def test_profile_url_resolves(self):
        url = reverse('users:profile')
        self.assertEquals(resolve(url).func, profile)

    def test_fav_url_resolves(self):
        url = reverse('users:fav')
        self.assertEquals(resolve(url).func, fav)

    def test_delete_fav_url_resolves(self):
        url = reverse('users:delete_fav')
        self.assertEquals(resolve(url).func, delete_fav)

    def test_login_url_resolves(self):
        url = reverse('users:login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_resolves(self):
        url = reverse('users:logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)
