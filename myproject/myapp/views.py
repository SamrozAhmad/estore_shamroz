# from django.shortcuts import render

# Create your views here.
from rest_framework import APIView
from rest_framework.response import Response 
from rest_framework import status
from .serializers import ProductSerializer
# from .models import Product

from django.shortcuts import get_object_or_404
class ProductView(APIView):
     def post(self, request):
          serializer = ProductSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     