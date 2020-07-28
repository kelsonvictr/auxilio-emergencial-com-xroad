from base_de_dados import base_inss_contribuintes_indv

def recebe_solicitacao_checagem_contribuinte_indv_INSS(dados):

    contribuinte = ([i for i in base_inss_contribuintes_indv() if i["cpf"] == int(dados["cpf"])] or [None])[0]


    if contribuinte is not None:
        return {"eh_contribuinte": contribuinte["eh_contribuinte"]}
    else:
        return {"eh_contribuinte": False} 