from django.db import models

# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField(default=00)
    país = models.CharField(max_length=30, default='')
    deasactivado = models.BooleanField(default=True)

