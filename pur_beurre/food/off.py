from food.constants import CATEGORIES_LIST, OFF_API_URL, KEYS
from food.models import Category, Product
import requests


class Database:

    def get_categories(self):
        """Add categories in database"""

        for cat in CATEGORIES_LIST:
            Category.objects.create(name=cat)

    def get_products(self):
        """Add each product from each category in database with its data"""

        for cat in CATEGORIES_LIST:
            params = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": cat,
                "page_size": 400,
                "json": 1
                }
            response = requests.get(OFF_API_URL, params=params)
            data = response.json()

            for elt in data['products']:
                product = {}
                for key in KEYS:
                    product[key] = elt.get(key)
                """Test if all 'products' keys have a value"""
                if all(product.values()):
                    """Test if a product is already present in the database"""
                    verify = Product.objects.filter(
                        openff_id=product.get('id'))
                    if not verify:
                        prod = Product(
                            brand=product.get('brands'),
                            name=product.get('product_name_fr'),
                            nutrition_grade_fr=product.get(
                                'nutrition_grade_fr'),
                            image_nutrition_url=product.get(
                                'image_nutrition_url'),
                            url=product.get('url'),
                            image_url=product.get('image_url'),
                            openff_id=product.get('id'),
                        )
                prod.save()

                """Associate each product to its categories"""
                categories = elt.get('categories')
                list_categories = categories.split(",")
                for category in list_categories:
                    category = category.strip()
                    if category in CATEGORIES_LIST:
                        category = Category.objects.get(name=category)
                        prod.category.add(category)
