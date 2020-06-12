from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    """Create the Category table in the database"""

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Create the Product table in the database"""

    brand = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    nutrition_grade_fr = models.CharField(max_length=1, blank=True, null=True)
    image_nutrition_url = models.URLField(
        max_length=250, blank=True, null=True)
    url = models.URLField(max_length=250, blank=True, null=True)
    image_url = models.URLField(max_length=250, blank=True, null=True)
    openff_id = models.BigIntegerField(blank=True, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return '{}, {}'.format(self.brand, self.name)


class Favorites(models.Model):
    """Create the favorites table in the database"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.substitute)
