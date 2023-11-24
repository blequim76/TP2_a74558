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


# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome io_terminal*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro io_terminal.py existente, deve apagar
# todos os outros ficheiros io_terminal-*.py, e inclusive estes comentários

# ...
