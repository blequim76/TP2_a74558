import pickle

from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas
from veiculos import nome_ficheiro_lista_de_veiculos

def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """Guarda os dados recebidos num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)
