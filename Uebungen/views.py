from django.shortcuts import render
from . import models

def indexpage(request):
    return render(request,'Uebungen/index.html')

def ArtikelFrage(request):
    Fragen=models.Uebung.objects.all()
    return render(request, 'Uebungen/ArtikelFragenSeite.html',context={'Fragen':Fragen})