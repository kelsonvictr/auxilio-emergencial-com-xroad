# BASE FICTÍCIA EM MEMÓRIA RAM APENAS PARA FINS DE TESTES
# DADOS FICTÍCIOS

def base_tse_dni():

    base = [
        {"dni": 123321123,
        "nome_completo": "Joao Silva",
        "cpf": 548812655,
        "rg": 215154124,
        "ctps": 48441548484485,
        "titulo_de_eleitor": 123131221,
        "estado_civil": "SOLTEIRO",
        "endereco":{"logradouro": "rua projetada, 14",
                    "cidade": "Joao Pessoa", 
                    "estado": "PB"},
        "data_nascimento": "03/01/1985"},
        {"dni": 123325553,
        "nome_completo": "Maria Sampaio",
        "cpf": 648812677,
        "rg": 333154133,
        "ctps": 78941548484485,
        "titulo_de_eleitor": 333131221,
        "estado_civil": "CASADA",
        "endereco":{"logradouro": "rua projetada, 16",
                    "cidade": "Brasília", 
                    "estado": "DF"},
        "data_nascimento": "12/12/1955"},
        {"dni": 123325669,
        "nome_completo": "Joana Marques",
        "cpf": 648812455,
        "rg": 333154105,
        "ctps": 78941548486688,
        "titulo_de_eleitor": 333139090,
        "estado_civil": "SOLTEIRO",
        "endereco":{"logradouro": "rua projetada, 19",
                    "cidade": "Recife", 
                    "estado": "PE"},
        "data_nascimento": "05/02/1985"},
        {"dni": 123325784,
        "nome_completo": "Alvaro Pereira",
        "cpf": 648810000,
        "rg": 333154108,
        "ctps": 78941548480078,
        "titulo_de_eleitor": 333137070,
        "estado_civil": "CASADO",
        "endereco":{"logradouro": "rua projetada, 777",
                    "cidade": "Coritiba", 
                    "estado": "PR"},
        "data_nascimento": "04/11/1990"}
    ]

    return base

def base_mte_empregados():

    base = [
        {"cpf": 123321123,
        "empregado": False},
        {"cpf": 648812677,
        "empregado": False},
        {"cpf": 648812455,
        "empregado": True},
        {"cpf": 648810000,
        "empregado": True}
    ]

    return base

def base_rfb_regularidade_dos_cpfs():

    base = [
        {"cpf": 123321123,
        "regularizado": False},
        {"cpf": 648812677,
        "regularizado": True},
        {"cpf": 648812455,
        "regularizado": False},
        {"cpf": 648810000,
        "regularizado": True}
    ]

    return base

def base_rfb_mei():

    base = [
            {"cpf": 123321123,
            "eh_MEI": True},
            {"cpf": 648812677,
            "eh_MEI": True},
            {"cpf": 648812455,
            "eh_MEI": False},
            {"cpf": 648810000,
            "eh_MEI": True}
        ]

    return base

def base_inss_contribuintes_indv():

    base = [
            {"cpf": 123321123,
            "eh_contribuinte": True},
            {"cpf": 648812677,
            "eh_contribuinte": True},
            {"cpf": 648812455,
            "eh_contribuinte": False},
            {"cpf": 648810000,
            "eh_contribuinte": True}
        ]

    return base
