from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('product/<int:id>', views.show, name="show"),
    path('save/', views.save, name="save"),
    path('legals/', views.legals, name="legals"),
]
