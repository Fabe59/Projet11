from django.shortcuts import render
from django.http import JsonResponse

from food.models import Product


def complete(request):
    searched_term = request.GET.get("term")
    products = Product.objects.filter(name__icontains=searched_term)
    autocomplete_products = [product.name for product in products][:10]
    return JsonResponse(autocomplete_products, safe=False)