from django.urls import path
from .views import ProductAPI, ProductPriceRangeAPI

urlpatterns = [
    path('products/', ProductAPI.as_view()),
    path('products/<int:pk>/', ProductAPI.as_view()),
    path('products/range/', ProductPriceRangeAPI.as_view()),
]
