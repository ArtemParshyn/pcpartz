from django.conf.urls.static import static
from django.urls import path
from api import views

from back import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('cart', views.cart, name='cart'),
    path('product/<int:id>', views.product, name='product'),
    path('routing', views.routing, name='routing'),
    path('map', views.map, name="map"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
