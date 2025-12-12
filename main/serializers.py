from rest_framework import serializers
from .models import Product, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ("slug",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("slug",)
        