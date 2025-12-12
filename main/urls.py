from django.urls import path
from .views import MovieAPIView, MovieCUDelete, ProductAPIView, ProductCUDelete


urlpatterns = [
    path('movies', MovieAPIView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieCUDelete.as_view(), name='movie-detail'),
    
    path('products', ProductAPIView.as_view(), name='products'),
    path('product/<int:pk>/', ProductCUDelete.as_view(), name='movie-detail'),
    
    

]