from django.test import TestCase
from django.urls import reverse
from food.models import Product, Favorites
from django.contrib.auth.models import User


class CreateViews(TestCase):

    def test_create_page(self):
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

    def test_create_account_valid(self):
        response = self.client.post(reverse('users:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users:profile')


class LoginViews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

    def test_login(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


class Logoutviews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')


class ProfileViews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

    def test_account_when_logged_in(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_account_when_logged_out(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/users/profile/')


class FavViews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

        nutella = {
            'id': '312',
            'brand': 'Ferrero',
            'name': 'Nutella',
            'nutrition_grade_fr': "e",
            'image_nutrition_url': 'https://nutnut.jpg',
            'image_url': 'https://nut.jpg',
        }
        nutella = Product.objects.create(**nutella)
        self.nutella = nutella
        food_saved = Product.objects.get(id=self.nutella.id)
        Favorites.objects.create(user=self.user, substitute=food_saved)

    def test_fav_when_logged_in(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('users:fav'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/fav.html')

    def test_fav_when_logged_out(self):
        response = self.client.get(reverse('users:fav'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/users/fav/')
