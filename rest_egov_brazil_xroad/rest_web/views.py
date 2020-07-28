from django.shortcuts import render
from rest_web.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['GET', 'POST'])
#@csrf_exempt
def recebe_req(request, slug):
 
    if request.method == "GET":
        #request = recebe_req(request, *args, **kwargs)
        print("jeç")
        print (request.data)
        print (slug)

    print (request)
    solicitacao_serializer = Requisicao_auxilioSerializer(data=request.data)

    print (request.data)

    if solicitacao_serializer.is_valid():
        #print(str(solicitacao_serializer))
        #print("teste!!!")
        print (request.data["nome_completo"])
        return Response(solicitacao_serializer.data, status=status.HTTP_201_CREATED)

    else:
        print ("ops!")
        print (request.header)
        return Response(solicitacao_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

