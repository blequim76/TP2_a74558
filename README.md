# TP2_a74558
Repositório de Trabalho Prático 2 - ADC - Commits e Documentação - Oficina

### Para que serve este repositório?

* Este repositório compilará os módulos da aplicação de gestão de uma oficina de reparação de automóveis
* Versão 0.1

### Ambiente
**A aplicação será desenvolvida em linguagem Python.**
Para criar um ambiente virtual
```
    $ python -m venv .venv
```
Depois, é necessário ativar o ambiente virtual
```
    $ .venv\Scripts\activate
 ```
e depois instalar as livrarias necessárias
```
    $ pip install -r requirements.txt
```

### Deve ser estruturado da seguinte forma:
## src/ ##
Criar um diretório para alojar os módulos principais.
`$ mkdir src/`

Nesse diretório irão constar os módulos:

- **main.py:** Módulo de controle da aplicação.
- **io_terminal.py:** Módulo de controle de terminal - ecrán.
- **io_files.py:** Módulo de Controle de Base de Dados - No nosso caso, de ficeiros.
- **clientes:** Módulo de operações CRUD de clientes.
- **veiculos:** Módulo de operações CRUD de veículos.
- **faturas:** Módulo de operações CRUD de faturação.
* 1 Repositório para alojar a documentação da aplicação. 

## docs/ ##
Criar um diretório para alojar a documentação da aplicação:
`$ mkdir docs/`
* Sphinx
`$ cd docs/`
`$ mkdir sphinx/`

O repositório pode ser acedido através de:
[Sphinx](https://github.com/blequim76/TP2_a74558/tree/e84fac7d3eb21559116285131736210842e03369/docs_sphinx)


* Doxygen
`$ cd docs/`
`$ mkdir sphinx/`

O repositório pode ser acedido através de:
[Doxygen](https://github.com/blequim76/TP2_a74558/tree/e84fac7d3eb21559116285131736210842e03369/docs_doxygen)
