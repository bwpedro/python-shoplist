def cadastrarLogin(fileLogin):
    email = input("E-mail: ")
    senha = input("Senha: ")

    from random import randint
    id = str(randint(0,10))

    fileLogin.write(id+";"+email+";"+senha)

    return id

def validaLogin(fileLogin):
    email = input("E-mail: ")
    senha = input("Senha: ")

    # passa pela validação

    print("Validando login...\n")
    print("Bem vindo de volta!\n")

    return

def addCarrinho(filePrato, fileLista):
    print("Os pratos disponíveis são: \n")
    # lista os pratos

    mais = True

    print("Adicionar ao carrinho: \n")
    prato = input("Pressione 0 para fechar suas compras.")

    while mais:
        if prato is "0":
            mais = False
        else:
            fileLista.write(prato)

    print("Pratos adicionados com sucesso!")

    return

def consultarLista(fileLista):
    print("Sua lista possui os seguintes pratos: \n")
    # listar os pratos da lista
    gerarLista(fileLista)

    return

def gerarLista(fileLista):
    gerar = True
    selec = 0

    while gerar:
        input = ("Deseja gerar sua lista de compras? (1-Sim/2-Não)\n")
        if selec is 1:
            # gera a lista
            gerar = False
        elif selec is 2:
            return
        else:
            print("Opção não disponível\n")
    
    print("Lista gerada com sucesso, consulte ingredientes.txt")

    return

def limparCarrinho(fileLista):
    # limpa a lista
    print("Carrinho limpo!")

    return
