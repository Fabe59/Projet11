from django.test import TestCase
from food.models import Category, Product, Favorites
from django.contrib.auth.models import User


class ModelsTest(TestCase):

    def test_models_category(self):
        cat = Category.objects.create(name='bonbons')
        self.assertEqual(Category.objects.first(), cat)

    def test_cat_string_representation(self):
        cat = Category.objects.create(name='bonbons')
        self.assertEqual(str(cat), 'bonbons')

    def test_models_product(self):
        category = Category.objects.create(name="pizza")
        product = Product.objects.create(
            id=1,
            brand="pizzaparty",
            name="pizza jambon",
            nutrition_grade_fr="b",
        )
        product.category.add(category)
        cat = Category.objects.get(name="pizza")
        prodcat = product.category.first()
        self.assertEquals(product.id, 1)
        self.assertEquals(product.brand, "pizzaparty")
        self.assertEquals(product.name, "pizza jambon")
        self.assertEquals(prodcat, cat)

    def test_prod_string_representation(self):
        prod = Product.objects.create(brand='LU', name='BN')
        self.assertEqual(str(prod), 'LU, BN')

    def test_models_favorite_user(self):
        category = Category.objects.create(name="pizza")
        substitute = Product.objects.create(
            id=2,
            brand="pizzaparty",
            name="pizza nature",
            nutrition_grade_fr="a"
        )
        substitute.category.add(category)

        user = User.objects.create_user(
            username="UtilisateurTest",
            password="Azertyuiop2020"
        )

        Favorites.objects.create(user=user, substitute=substitute)
        favorite = Favorites.objects.all().first()
        self.assertEqual(favorite.user, user)
        self.assertEqual(favorite.substitute, substitute)

    def test_fav_string_representation(self):
        category = Category.objects.create(name="pizza")
        substitute = Product.objects.create(
            id=2,
            brand="pizzaparty",
            name="pizza nature",
            nutrition_grade_fr="a"
        )
        substitute.category.add(category)

        user = User.objects.create_user(
            username="UtilisateurTest",
            password="Azertyuiop2020"
        )

        fav = Favorites.objects.create(user=user, substitute=substitute)
        self.assertEqual(str(fav), 'pizzaparty, pizza nature')
