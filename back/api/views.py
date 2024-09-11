from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def catalog(request):
    return render(request, "catalog.html")


def cart(request):
    return render(request, "cart.html")


def product(request):
    return render(request, "product.html")
