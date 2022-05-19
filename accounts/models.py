from django.db import models

# Create your models here.

class UsuarioP3(models.Model):
    rut=models.CharField(max_length=30, primary_key=True)
    email=models.CharField(max_length=300)
    nombre=models.CharField(max_length=300)
    edad=models.CharField(max_length=300)
    