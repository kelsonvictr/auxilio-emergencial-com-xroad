import requests
import json
from base_de_dados import base_tse_dni


def recebe_solicitacao_validacao_dni(dados):

    #print (dados)

    dni_valido = ([i for i in base_tse_dni() if i["dni"] == int(dados["dni"]) and i['nome_completo'] == dados["nome_completo"] and i["data_nascimento"] == dados["data_nascimento"]] or [None])[0]


    if dni_valido is not None:
        return {"dni_valido": True, "dni": dni_valido["dni"], "cpf": dni_valido["cpf"]}

    else:
        return {"dni_valido": False}
