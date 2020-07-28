from flask import Flask, json, request, jsonify
from cef import recebe_solicitacao_cef
from mte import recebe_solicitacao_checagem_empregados_e_desempregrados
from dni import recebe_solicitacao_validacao_dni
from rfb import recebe_solicitacao_checagem_verifica_cpf, recebe_solicitacao_checagem_verifica_mei
from inss import recebe_solicitacao_checagem_contribuinte_indv_INSS

api = Flask(__name__)

@api.route('/api', methods=['POST'])
def acao_do_post():
    
    data = request.json

    response = {}

    if data["acao"] == "request_cef":
        response = jsonify(recebe_solicitacao_cef(data))
    
    elif data["acao"] == "request_dni":
        response = jsonify(recebe_solicitacao_validacao_dni(data))
    
    elif data["acao"] == "request_mte":
        response = recebe_solicitacao_checagem_empregados_e_desempregrados(data)

    elif data["acao"] == "request_rfb_cpf":

        response = recebe_solicitacao_checagem_verifica_cpf(data)

    elif data["acao"] == "request_rfb_mei":

        response = recebe_solicitacao_checagem_verifica_mei(data)

    elif data["acao"] == "request_inss":

        response = recebe_solicitacao_checagem_contribuinte_indv_INSS(data)


    return response

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000)