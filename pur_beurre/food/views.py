from django.shortcuts import render
from .models import Product, Favorites
from django.core.paginator import Paginator


def home(request):
    """Function to display the home page template"""

    return render(request, 'food/home.html')


def search(request):
    """Function to manage the search and its display"""

    research = request.GET['search']

    if not research:
        return render(request, 'food/home.html')

    query = Product.objects.filter(name__icontains=research)
    if query:
        categories = query[0].category.all()
        name = query[0].name
        image = query[0].image_url
        nutriscore = query[0].nutrition_grade_fr

        liste_prod = []
        for cat in categories:
            liste_prod = cat.product_set.filter(
                nutrition_grade_fr__lt=nutriscore
                ).order_by('name')

        if not liste_prod:
            return render(
                request,
                'food/nosubstitute.html',
                {'research': research, 'name': name, 'image': image}
                )

    else:
        query = None
        return render(request, 'food/noproduct.html', {'research': research})

    paginator = Paginator(liste_prod, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'food/search.html',
        {
            'research': research,
            'name': name,
            'image': image,
            'search': liste_prod,
        }
        )


def show(request, id):
    """Function to display the food specific information page"""

    article = Product.objects.get(id=id)
    return render(request, 'food/show.html', {'article': article})


def save(request):
    """Function which allows the user to save a substitute in his database"""

    if request.method == "POST":
        current_user = request.user
        food = request.POST.get('elt')
        food_saved = Product.objects.get(id=food)
        Favorites.objects.get_or_create(
            user=current_user,
            substitute=food_saved
            )
    return render(request, 'food/home.html')


def legals(request):
    """Function to display the legals template"""

    return render(request, 'food/legals.html')
