from rest_framework import serializers
from .models import *

class Requisicao_auxilioSerializer(serializers.Serializer):
    nome_completo = serializers.CharField(max_length=1000)
    #dni = serializers.CharField(max_length=1000)
    #data_nascimento = serializers.CharField(max_length=1000)