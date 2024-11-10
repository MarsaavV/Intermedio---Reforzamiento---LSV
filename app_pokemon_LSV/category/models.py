from django.db import models

# Create your models here.
class category(models.Model):
    Nombre = models.CharField(max_length=30)
