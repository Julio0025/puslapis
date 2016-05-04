from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def duk(request):
    return render(request, 'duk.html')

