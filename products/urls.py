from django.urls import path

from .views import ProductListView

#product/urls.py 위치

urlpatterns = [
    #http://127.0.01:8000/products
    path("", ProductListView.as_view())
]