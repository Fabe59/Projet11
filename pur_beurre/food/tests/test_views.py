from django.test import TestCase
from django.urls import reverse
from food.models import Product, Favorites
from django.contrib.auth.models import User


class HomepageViews(TestCase):

    def test_homepage(self):
        response = self.client.get(reverse('food:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')


class LegalsViews(TestCase):

    def test_legals(self):
        response = self.client.get(reverse('food:legals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/legals.html')


class SearchViews(TestCase):

    def setUp(self):
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

    def test_foodsearch_valid(self):
        response = self.client.get('/search/?search=%s' % ('nutella'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/nosubstitute.html')

    def test_foodsearch_empty(self):
        response = self.client.get('/search/?search=%s' % (''))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')


class ShowViews(TestCase):

    def setUp(self):
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

    def test_foodshow_valid(self):
        id = self.nutella.id
        response = self.client.get('/product/%d' % (id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/show.html')


class SaveViews(TestCase):

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

    def test_save_substitute(self):
        self.client.login(username=self.username, password=self.password)
        url = reverse('food:save')
        data = {"elt": self.nutella.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Favorites.objects.all().exists())
