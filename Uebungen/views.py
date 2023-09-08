from django.shortcuts import render

def indexpage(request):
    return render(request,'Uebungen/index.html')
