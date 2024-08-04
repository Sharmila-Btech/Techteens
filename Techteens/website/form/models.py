from django.db import models

# Create your models here.

class data (models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=300)

class table (models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=300)