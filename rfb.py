import requests
import json
from base_de_dados import base_rfb_mei, base_rfb_regularidade_dos_cpfs

def recebe_solicitacao_checagem_verifica_cpf(dados):

    cpf_regular = ([i for i in base_rfb_regularidade_dos_cpfs() if i["cpf"] == int(dados["cpf"]) and i['regularizado'] == True] or [None])[0]

    if cpf_regular is not None:
        return {"cpf_regular": cpf_regular["regularizado"]}
    else:
        recebe_solcitacao_regularizar_cpf(dados["cpf"])
        return {"cpf_regular": False}


def recebe_solcitacao_regularizar_cpf(dados):

    print (dados)

    f = open("cpfs_para_regularizar.txt", "a")

    f.writelines(str(dados)+"\n")

    f.close() 
                                                                                            

def recebe_solicitacao_checagem_verifica_mei(dados):

    mei = ([i for i in base_rfb_mei() if i["cpf"] == int(dados["cpf"]) and i['eh_MEI'] == True] or [None])[0]

    if mei is not None:
        return {"eh_MEI": mei["eh_MEI"]}
    else:
        return {"eh_MEI": False}


