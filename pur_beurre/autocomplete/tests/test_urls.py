from django.test import TestCase
from autocomplete.views import complete
from django.urls import reverse, resolve


class Autocomplete_Url_Test(TestCase):

    def test_complete_url_view(self):
        url = reverse("autocomplete:complete")
        self.assertEquals(resolve(url).func, complete)
