import requests
import json
from base_de_dados import base_mte_empregados

def recebe_solicitacao_checagem_empregados_e_desempregrados(dados):

    empregado = ([i for i in base_mte_empregados() if i["cpf"] == int(dados["cpf"]) and i['empregado'] == True] or [None])[0]

    #print (empregado)


    if empregado is not None:
        return {"empregado": empregado["empregado"]}
    else:
        return {"empregado": False}