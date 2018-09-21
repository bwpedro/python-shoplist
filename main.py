from biblioteca import *

def main():

    sair = False

    fileLogin = open('login.txt', 'w')
    filePratos = open('pratos.txt', 'w')
    fileIngredientes = open('ingredientes.txt', 'w')
    fileLista = open('lista.txt', 'w')

    while (not sair):
        cadastro = int(input("\nBem vindo ao SHOPLIST\nVocê já possui cadastro? (1-Sim/2-Não)"))

        if cadastro is 1:
            validaLogin(fileLogin)
            sair = True
        elif cadastro is 2:
            cadastrarLogin(fileLogin)
            sair = True
        else:
            print("Opção não disponível\n")

    sair = False

    while (not sair):
        print("\n\n##### SHOPLIST #####\n\n")
        selec = int(input("Selecione uma Opção:\n\n1) Adicionar ao carrinho\n2) Consultar lista\n3) Gerar lista\n4) Limpar carrinho\n5) Sair\n"))

        if selec is 1:
            print("\n## ADICIONAR PRATOS AO CARRINHO ##\n\n")
            addCarrinho(filePrato, fileLista)
        elif selec is 2:
            print("\n## CONSULTAR LISTA ##\n\n")
            consultarLista(fileLista)
        elif selec is 3:
            print("\n## GERAR LISTA ##\n\n")
            gerarLista(fileLista)
        elif selec is 4:
            print("\n## LIMPAR CARRINHO ##\n\n")
            limparCarrinho(fileLista)
        elif selec is 5:
            sair = True
            print("\nSaindo do programa...\n")
        else:
            print("\nOpção não disponível\n")
    
    fileLogin.close()
    fileIngredientes.close()
    fileLista.close()
    filePratos.close()


if __name__ == "__main__":
    main()