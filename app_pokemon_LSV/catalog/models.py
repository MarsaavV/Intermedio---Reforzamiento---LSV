from django.db import models

# Create your models here.
class Catalog(models.Model):
    Nombre = models.CharField(max_length=30)
    Descipción = models.TextField(max_length=100)