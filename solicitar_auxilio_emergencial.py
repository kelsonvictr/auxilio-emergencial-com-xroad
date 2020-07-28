import requests 
import json
import time

def requisicao_atraves_do_xroad(dados):
    
    try:
        headers = {
            'Content-Type': 'application/json',
            'X-Road-Client': 'DEMO/GOV/1234/SUB1',
        }

        data = str(json.dumps(dados))

        response = requests.post('http://10.206.36.253/r1/DEMO/GOV/1234/SUB2/cef/api', headers=headers, data=data)

        retorno = json.loads(response.text)
        #print (response)

        #print (response.text)


    except (Exception) as e:
        print(e)

    finally:
        return retorno

    #print (response)     


def solicita_auxilio():
    
    nome_completo = input("Digite o seu nome completo: ")
    dni = input("Digite o seu DNI: ")
    data_nascimento = input("Digite a sua data de nascimento: ")

    dados = {"acao":"request_cef", "nome_completo": str(nome_completo), "dni": str(dni), "data_nascimento": str(data_nascimento)}

    #print (requisicao_atraves_do_xroad(dados)["dni_valido"])
    
    #print (requisicao_atraves_do_xroad(dados))
    
    validacao_do_dni = json.loads(json.dumps(requisicao_atraves_do_xroad(dados)))

    if validacao_do_dni["dni_valido"] == False:
        print ("Dados recebidos dos diferentes sistemas: "+str(validacao_do_dni))
        print ("Informações ou DNI incorretos")

    else:

        print ("Coletando informações em sistemas do e-gov...")
        
        time.sleep(6)

        print ("Dados recebidos dos diferentes sistemas: "+str(validacao_do_dni))
        
        #print (validacao_do_dni)
        if validacao_do_dni["cpf_regular"] == False and validacao_do_dni["auxilio_aprovado"] == False and validacao_do_dni["empregado"] == False:
            

            print (
                "\n\nConsultando Ministério do Trabalho e Emprego: DESEMPREGADO\n\nConsultando a Receita Federal: Detectamos através do seu DNI que o seu CPF está irregular. Já enviamos uma solicitação para a Receita Federal possa regularizá-lo.\n\n\nAUXÍLIO APROVADO (Aguardando regularização do CPF na RFB para liberação do recurso na sua Conta Digital da Caixa)")

        elif validacao_do_dni["cpf_regular"] == True and validacao_do_dni["auxilio_aprovado"] == True and validacao_do_dni["empregado"] == False:

            print (
                "\n\nConsultando Ministério do Trabalho e Emprego: DESEMPREGADO\n\nConsultando a Receita Federal: CPF REGULARIZADO\n\n\nAUXÍLIO APROVADO (Em instantes você receberá o recurso através da sua Conta Digital Caixa)")

        elif validacao_do_dni["cpf_regular"] == False and validacao_do_dni["auxilio_aprovado"] == False and validacao_do_dni["empregado"] == True:

            if validacao_do_dni["eh_MEI"] == True:
                eh_MEI = "É MEI" 
            else: 
                eh_MEI = "NÃO É MEI"

            if validacao_do_dni["eh_contribuinte_indv_INSS"] == True:
                eh_contribuinte_INSS = "É CONTRIBUINTE" 
            else: 
                eh_contribuinte_INSS = "NÃO É CONTRIBUINTE"

            print (
                "\n\nConsultando Ministério do Trabalho e Emprego: EMPREGADO\n\nConsultando a Receita Federal: Detectamos através do seu DNI que o seu CPF está irregular.\n\nConsultado a Receita Federal: "+eh_MEI+"\n\nConsultado o INSS: "+eh_contribuinte_INSS+"\n\n\nAUXÍLIO NEGADO (Você não atende os pré-requisitos para receber o Auxílio Emergencial)")

        

        elif validacao_do_dni["cpf_regular"] == True and validacao_do_dni["auxilio_aprovado"] == False and validacao_do_dni["empregado"] == True:


            if validacao_do_dni["eh_MEI"] == True:
                eh_MEI = "É MEI" 
            else: 
                eh_MEI = "NÃO É MEI"

            if validacao_do_dni["eh_contribuinte_indv_INSS"] == True:
                eh_contribuinte_INSS = "É CONTRIBUINTE" 
            else: 
                eh_contribuinte_INSS = "NÃO É CONTRIBUINTE"

            print (
                "\n\nConsultando Ministério do Trabalho e Emprego: DESEMPREGADO\n\nConsultando a Receita Federal: REGULAR\n\nConsultado a Receita Federal: "+eh_MEI+"\n\nConsultado o INSS: "+eh_contribuinte_INSS+"\n\n\nAUXÍLIO NEGADO (Você não atende os pré-requisitos para receber o Auxílio Emergencial)")


        elif validacao_do_dni["cpf_regular"] == True and validacao_do_dni["auxilio_aprovado"] == True and validacao_do_dni["empregado"] == True:


            if validacao_do_dni["eh_MEI"] == True:
                eh_MEI = "É MEI" 
            else: 
                eh_MEI = "NÃO É MEI"

            if validacao_do_dni["eh_contribuinte_indv_INSS"] == True:
                eh_contribuinte_INSS = "É CONTRIBUINTE" 
            else: 
                eh_contribuinte_INSS = "NÃO É CONTRIBUINTE"

            print (
                "\n\nConsultando Ministério do Trabalho e Emprego: EMPREGADO\n\nConsultando a Receita Federal: REGULAR\n\nConsultado a Receita Federal: "+eh_MEI+"\n\nConsultado o INSS: "+eh_contribuinte_INSS+"\n\n\nAUXÍLIO APROVADO (Em instantes você receberá o recurso através da sua Conta Digital Caixa)")

        #elif validacao_do_dni["cpf_regular"] == False and validacao_do_dni["auxilio_aprovado"] == False and validacao_do_dni["empregado"] == True:

        # tudo ok! de acordo com o fluxograma do papel... fazer apenas a re-checagem se está "empregado = True" na secretária do trabalho ... estadual ... fazer dni mandar um sms para confirmar a solicitacao de aux emergencial? interoperabilidade r0x


solicita_auxilio()
