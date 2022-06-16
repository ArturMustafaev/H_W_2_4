from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=1000)

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    descriptions = models.TextField()

class Review(models.Model):
    text = models.TextField()

