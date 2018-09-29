from biblioteca import *

def main():

    sair = False

    usuario = list()
    carrinho = list()
    pratos = list()

    fileUsuario = open('./usuario.txt')
    filePratos = open('./pratos.txt')
    fileLista = open('./lista.txt')
    fileCarrinho = open('./carrinho.txt')
   
    while (not sair):
        cadastro = int(input("\nBem vindo ao SHOPLIST\nVocê já possui cadastro? (1-Sim/2-Não)"))

        if cadastro is 1:
            validaUsuario(fileUsuario)
            sair = True
        elif cadastro is 2:
            cadastrarUsuario(fileUsuario, usuario)
            sair = True
        else:
            print("Opção não disponível\n")

    sair = False

    while (not sair):
        print("\n\n##### SHOPLIST #####\n\n")
        selec = int(input("Selecione uma Opção:\n\n1) Adicionar ao carrinho\n2) Consultar carrinho\n3) Gerar lista\n4) Limpar carrinho\n5) Sair\n"))

        if selec is 1:
            print("\n## ADICIONAR PRATOS AO CARRINHO ##\n\n")
            addCarrinho(filePratos, fileCarrinho)
        elif selec is 2:
            print("\n## CONSULTAR CARRINHO ##\n\n")
            consultarCarrinho(fileCarrinho)
        elif selec is 3:
            print("\n## GERAR LISTA ##\n\n")
            gerarLista(fileCarrinho, fileLista)
        elif selec is 4:
            print("\n## LIMPAR CARRINHO ##\n\n")
            limparCarrinho(fileCarrinho)
        elif selec is 5:
            sair = True
            print("\nSaindo do programa...\n")
        else:
            print("\nOpção não disponível\n")
    
    fileUsuario.close()
    filePratos.close()
    fileLista.close()
    fileCarrinho.close()


if __name__ == "__main__":
    main()