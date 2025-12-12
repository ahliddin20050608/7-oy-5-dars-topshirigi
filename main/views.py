from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Movie, Product
from .serializers import MovieSerializer, ProductSerializer
class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieCUDelete(APIView):
    def get_object(self, pk):
        return get_object_or_404(Movie, pk=pk)
    
    def get(self, request, pk):
        movie = self.get_object(pk=pk) 
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductCUDelete(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)
    
    def get(self, request, pk):
        product = self.get_object(pk=pk) 
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
