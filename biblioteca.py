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

    return

def consultarLista(fileLista):
    
    return

def gerarLista(fileLista):

    return

def limparCarrinho(fileLista):
    
    return
