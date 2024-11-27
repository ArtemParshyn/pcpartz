from django.shortcuts import render, get_object_or_404

from api.models import Product


def index(request):
    return render(request, "index.html")


def catalog(request):
    products = Product.objects.all()
    a = []
    for i in products:
        a.append({"name": i.name,
                  "price": i.price,
                  "descr": i.descr,
                  "image": i.image,
                  "id": i.pk})
    return render(request, "catalog.html", context={"products": products})


def cart(request):
    return render(request, "cart.html")


def product(request, id):
    Prod = get_object_or_404(Product, pk = id)
    a = {"name": Prod.name,
         "price": Prod.price,
         "descr": Prod.descr,
         "image": Prod.image.url,
         "id": Prod.pk}
    return render(request, "product.html", context={"product": a})


def routing(request):
    return render(request, "routing.html")


def map(request):
    return render(request, "map.html")
