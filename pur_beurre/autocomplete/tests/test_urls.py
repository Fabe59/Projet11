from django.test import TestCase
from autocomplete.views import complete
from django.urls import reverse, resolve


class Autocomplete_Url_Test(TestCase):

    def test_complete_url_view(self):
        suggestion = resolve(reverse("autocomplete:complete"))
        self.assertEqual(suggestion.func, complete)