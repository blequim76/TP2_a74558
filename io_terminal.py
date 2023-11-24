from tabulate import tabulate


def pergunta_id(questao, lista, mostra_lista=False):
    """TODO: documentação

    :param questao:
    :param lista:
    :param mostra_lista:
    :return:
    """

    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")


def pause():
    """Faz uma pausa no programa e espera que o utilizador pressione ENTER"""

    input("Pressione ENTER para continuar...")



def pergunta_id(questao, lista, mostra_lista=False):
    """TODO: documentação

    :param questao:
    :param lista:
    :param mostra_lista:
    :return:
    """

    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")
