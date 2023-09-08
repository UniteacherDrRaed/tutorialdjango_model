from django.urls import path
from . import views

app_name="Uebungen"

urlpatterns = [
    path("", views.indexpage, name='indexpage'),
    path("Artikel",views.ArtikelFrage, name='ArtikelFrage' ) ,  
]
