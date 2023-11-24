from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def cria_novo_cliente():
    """Pedir os dados de um novo cliente

    :return: dicionario com o novo cliente, {"nome": <<nome>>, "nif": <<nif>>, ...}
    """
    
    nome = input("nome? ")
    nif = input("nif? ").upper()
    # TODO: Pedir o resto dos dados do cliente, e não esquecer de os guardar no dicionario
    # ...

    cliente = {"nome": nome,
               "nif": nif}

    return cliente


def imprime_lista_de_clientes(lista_de_clientes):
    """Imprime a lista de Clientes"""

imprime_lista(cabecalho="Lista de Clientes", lista=lista_de_clientes)
