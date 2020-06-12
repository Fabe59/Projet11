from django.test import TestCase
from food.views import home, search, show, save, legals
from django.urls import reverse, resolve


class Food_Url_Test(TestCase):

    def test_home_url_resolves(self):
        url = reverse('food:home')
        self.assertEquals(resolve(url).func, home)

    def test_search_url_resolves(self):
        url = reverse('food:search')
        self.assertEquals(resolve(url).func, search)

    def test_show_url_resolves(self):
        url = reverse('food:show', args=['123'])
        self.assertEquals(resolve(url).func, show)

    def test_save_url_resolves(self):
        url = reverse('food:save')
        self.assertEquals(resolve(url).func, save)

    def test_legals_url_resolves(self):
        url = reverse('food:legals')
        self.assertEquals(resolve(url).func, legals)
