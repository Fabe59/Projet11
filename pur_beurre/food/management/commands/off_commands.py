
"""
Module that uses the OpenFoodFacts API to collect
all the data needed for the pur_beurre database
"""

from django.core.management.base import BaseCommand
from food.off import Database


class Command(BaseCommand):

    def handle(self, *args, **options):
        db = Database()
        db.get_categories()
        db.get_products()
