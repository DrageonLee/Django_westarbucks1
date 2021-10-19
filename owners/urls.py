from django.urls import path

from .views import OwnerListView, DogListView

#/urls.py 위치

urlpatterns = [
    #http://127.0.01:8000/products
    path("/on", OwnerListView.as_view()),
    path("/do", DogListView.as_view())
]