from django.contrib import admin
from .models import Movie, Product


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "genres")
    list_filter = ("genres", "year")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}  
    ordering = ("-year",)
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    search_fields = ("title", "descrition")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-price",)
    list_per_page = 20
