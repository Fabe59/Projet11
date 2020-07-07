from django.test import TestCase
from django.urls import reverse
import json
from food.models import Product


class Autocomplete(TestCase):

    def setUp(self):
        pizza = {
            'id': '312',
            'brand': 'Leclerc',
            'name': 'Pizza fromage',
            'nutrition_grade_fr': "e",
            'image_nutrition_url': 'https://leclercpizza4f.jpg',
            'image_url': 'https://leclercpizza4f.jpg',
        }
        pizza = Product.objects.create(**pizza)

    def test_complete_views(self):
        response = self.client.get(reverse("autocomplete:complete"), {
            "term": "piz"
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(["Pizza fromage"]))
