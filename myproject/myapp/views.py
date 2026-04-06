from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import ProductSerializer

from myproject.myapp.serializers import ProductSerializer

class ProductAPI(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

