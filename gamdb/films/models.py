from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    avg_rating = models.FloatField()
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    director = models.ForeignKey("Director", blank=True, null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey("Genre", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} ({self.year})"

class Director(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    birth_year = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.birth_year})"

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField()
    

