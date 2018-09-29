class Usuario:
    ide = 0
    email = ""
    senha = ""
    nome = ""

    def __init__(self, ide, email, senha, nome):
        self.ide = ide
        self.email = email
        self.senha = senha
        self.nome = nome

class Ingredientes:
    prato = ""
    ingredientes = ""

    def __init__(self, prato, ingredientes):
        self.prato = prato
        self.ingredientes = ingredientes

def cadastrarUsuario(fileUsuario, usuario):
    from random import randint
    ide = str(randint(0,10))

    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    usuario = Usuario(ide, email, senha, nome)

    fileUsuario.write(usuario.ide+";"+usuario.nome+";"+usuario.email+";"+usuario.senha+"\n")

def validaUsuario(fileUsuario):
    email = input("E-mail: ")
    senha = input("Senha: ")

    valida = fileUsuario.readline()
    
    print(valida)

    print("Validando login...\n")

    return

def addCarrinho(filePratos, fileCarrinho):
    print("Os pratos disponíveis são: \n")
    # lista os pratos

    mais = True

    print("Adicionar ao carrinho: \n")
    prato = input("Pressione 0 para fechar suas compras.")

    while mais:
        if prato is "0":
            mais = False
        else:
            fileCarrinho.write(prato)

    print("Pratos adicionados com sucesso!")

    return

def consultarCarrinho(fileCarrinho):
    print("Sua lista possui os seguintes pratos: \n")
    # listar os pratos da lista

    return

def gerarLista(fileCarrinho, fileLista):
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
    
    print("Lista gerada com sucesso, consulte lista.txt")

    return

def limparCarrinho(fileCarrinho):
    # limpa a lista
    print("Carrinho limpo!")

    return
