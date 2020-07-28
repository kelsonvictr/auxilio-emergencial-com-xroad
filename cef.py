import requests
import json

def requisicao_atraves_do_xroad(dados):
    try:
        headers = {
            'Content-Type': 'application/json',
            'X-Road-Client': 'DEMO/GOV/1234/SUB1',
        }

        data = str(json.dumps(dados))

        if dados["acao"] == "request_dni":
            response = requests.post('http://10.206.36.253/r1/DEMO/GOV/1234/SUB3/dni-tse/api', headers=headers, data=data)

        elif dados["acao"] == "request_mte":
            response = requests.post('http://10.206.36.253/r1/DEMO/GOV/1234/SUB4/mte/api', headers=headers, data=data)

        elif dados["acao"] == "request_rfb_cpf" or dados["acao"] == "request_rfb_mei":            
            response = requests.post('http://10.206.36.253/r1/DEMO/GOV/1234/SUB5/rfb/api', headers=headers, data=data)

        elif dados["acao"] == "request_inss":
            response = requests.post('http://10.206.36.253/r1/DEMO/GOV/1234/SUB6/inss/api', headers=headers, data=data)

    except (Exception) as e:
        print(e)

    finally:
        return response.text


def validacao_do_auxilio(dados):

    #primeiro, validar o DNI

    dados_a_validar_no_DNI = {"nome_completo":dados["nome_completo"], "dni":dados["dni"], "data_nascimento":dados["data_nascimento"],"acao":"request_dni"}

    validacao_do_dni = json.loads(requisicao_atraves_do_xroad(dados_a_validar_no_DNI))

    resposta = {}

    auxilio_aprovado = None

    if validacao_do_dni["dni_valido"] == True:
        # verificar aqui os outros sistemas via X-Road
        # MTE, RFB, INSS
        # fazer um dict geral para todas as condições/respostas

        # first, consulta se é empregado na base de dados do MTE (via X-Road)

        dados_a_validar_no_MTE = {"cpf": validacao_do_dni["cpf"], "acao": "request_mte"}

        validacao_se_possui_emprego = json.loads(requisicao_atraves_do_xroad(dados_a_validar_no_MTE))

        dados_a_validar_cpf_na_RFB = {"cpf": validacao_do_dni["cpf"], "acao": "request_rfb_cpf"}

        validacao_se_o_cpf_esta_regular = json.loads(requisicao_atraves_do_xroad(dados_a_validar_cpf_na_RFB))

        if validacao_se_possui_emprego["empregado"] == False:

            if validacao_se_o_cpf_esta_regular["cpf_regular"] == True:
                auxilio_aprovado = True
            else:
                auxilio_aprovado = False

            #print (validacao_se_o_cpf_esta_regular)

            validacao_se_eh_MEI = {"eh_MEI": None}
            validacao_se_eh_contribuinte_indv_INSS = {"eh_contribuinte": None}

        else: # se tiver emprego (MEIs, Informais, Contribuintes Individuais INSS)

            dados_a_validar_MEI_RFB = {"cpf": validacao_do_dni["cpf"], "acao": "request_rfb_mei"}

            validacao_se_eh_MEI = json.loads(requisicao_atraves_do_xroad(dados_a_validar_MEI_RFB))

            print (validacao_se_eh_MEI)

            dados_a_validar_contribuinte_indv_INSS = {"cpf": validacao_do_dni["cpf"], "acao": "request_inss"}

            validacao_se_eh_contribuinte_indv_INSS = json.loads(requisicao_atraves_do_xroad(dados_a_validar_contribuinte_indv_INSS))

            if validacao_se_o_cpf_esta_regular["cpf_regular"] == True and (validacao_se_eh_MEI["eh_MEI"] == True or validacao_se_eh_contribuinte_indv_INSS["eh_contribuinte"] == True):

                auxilio_aprovado = True

            else:
                auxilio_aprovado = False

            
        resposta = {
                    "dni": validacao_do_dni["dni"],
                    "dni_valido": validacao_do_dni["dni_valido"],
                    "empregado": validacao_se_possui_emprego["empregado"],
                    "cpf_regular": validacao_se_o_cpf_esta_regular["cpf_regular"],
                    "eh_MEI": validacao_se_eh_MEI["eh_MEI"],
                    "eh_contribuinte_indv_INSS": validacao_se_eh_contribuinte_indv_INSS["eh_contribuinte"],
                    "auxilio_aprovado": auxilio_aprovado
                    }

        #retorno = json.loads(json.dumps(resposta))

    else:
        resposta = {
                    "dni_valido": validacao_do_dni["dni_valido"]
                    }
        
        #retorno = validacao_do_dni




    #enviando para o sistema do DNI para validação (via x-Road)
    #print(requisicao_atraves_do_xroad(dados_a_validar_no_DNI))

    #return requisicao_atraves_do_xroad(dados_a_validar_no_DNI)
    return json.loads(json.dumps(resposta))


def recebe_solicitacao_cef(dados):
    
    print("Recebendo os dados no Sistema da CEF")


    return validacao_do_auxilio(dados)

    
    