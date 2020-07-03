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

        choco = {
            'id': '313',
            'brand': 'Auchan',
            'name': 'Choco',
            'nutrition_grade_fr': "d",
            'image_nutrition_url': 'https://nutchoco.jpg',
            'image_url': 'https://choco.jpg',
        }
        choco = Product.objects.create(**choco)
        self.choco = choco

        cacao = {
            'id': '314',
            'brand': 'Carrefour',
            'name': 'Cacao',
            'nutrition_grade_fr': "c",
            'image_nutrition_url': 'https://nutcacao.jpg',
            'image_url': 'https://cacao.jpg',
        }
        cacao = Product.objects.create(**cacao)
        self.cacao = cacao

        self.liste_prod = Product.objects.all()

    def test_foodsearch_valid(self):
        response = self.client.get('/search/?search=%s' % ('nutella'))
        self.assertEqual((response.context['research']), 'nutella')
        self.assertEqual((response.context['name']), self.nutella.name)
        self.assertEqual((response.context['image']), self.nutella.image_url)
        self.assertEqual((response.context['search']), self.liste_prod)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/search.html')

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
