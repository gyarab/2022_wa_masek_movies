from django.contrib import admin

from .models import Movie
from .models import Director
from .models import Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year']
    list_display_links = ['name']
    
admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Genre)