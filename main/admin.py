from django.contrib import admin
from main.models import Product
from main.models import Director
from main.models import Movie
from main.models import Review

# Register your models here.

admin.site.register(Product)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)