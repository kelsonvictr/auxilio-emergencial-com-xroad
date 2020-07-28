from django.db import models

# Create your models here.

class Requisicao_auxilio(models.Model):
    nome_completo = models.CharField(max_length=1000, blank=True)
    #dni = models.CharField(max_length=1000, blank=True)
    #data_nascimento = models.CharField(max_length=1000, blank=True)