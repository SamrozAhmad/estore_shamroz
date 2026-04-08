from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

from django.shortcuts import get_object_or_404

class ProductAPI(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #helper function
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk=None):
        
        #http://127.0.0.1:8000/products/6/
        if pk:
            product = self.get_object(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            #http://127.0.0.1:8000/products/
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPriceRangeAPI(APIView):
    def get(self, request):
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        products = Product.objects.all()#fetch all product fropm db for applying filter

        if min_price and max_price:
            products = products.filter(price__range=(min_price, max_price))
        elif min_price:
            products = products.filter(price__gte=min_price)
        elif max_price:
            products = products.filter(price__lte=max_price)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)