from django.db import models
from django.utils.text import slugify  
class GenreChoices(models.TextChoices):
    ACTION = "action", "Action"
    DRAMA = "drama", "Drama"
    COMEDY = "comedy", "Comedy"
    HORROR = "horror", "Horror"
    SCIFI = "sci-fi", "Sci-Fi"
    ROMANCE = "romance", "Romance"
    THRILLER = "thriller", "Thriller"
    FANTASY = "fantasy", "Fantasy"
    ADVENTURE = "adventure", "Adventure"
    ANIMATION = "animation", "Animation"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    year = models.PositiveIntegerField(default=2025)
    genres = models.CharField(choices=GenreChoices.choices, default=GenreChoices.ANIMATION)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) 
    image =  models.FileField(upload_to="products")
    descrition = models.TextField()
    price = models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.title