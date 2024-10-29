# Empresa de logística de carregamento em um porto containers
from PilhaImplementacao import Pilha

containers = Pilha()


def cabecalho():
    print('=' * 40)
    print("SEJA BEM VINDO!")
    print("Escolha uma opção: ")
    print("[1] - Adicionar containers")
    print("[2] - Remover containers")
    print("[3] - Ver pilha de containers")
    print("[0] - Encerrar")
    print('=' * 40)


def empilha_container(pilha, container):
    pilha.empilha(container)


def desempilha_container(pilha):
    if pilha_vazia(pilha):
        print("Não há containers empilhados!")
        return
    return pilha.desempilha()


def pilha_vazia(pilha):
    pilha.esta_vazia()

cabecalho()
while True:
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        quantidade = int(input("Informe a quantidade que deseja adicionar: "))
        for i in range(quantidade):
            container = "C" + str(i + 1)
            print("empilhando o container: " + container)
            empilha_container(containers, container)
    elif opcao == '2':
        quantidade = int(input("Informe a quantidade que deseja remover: "))
        if quantidade == 0: print("Tente novamente")
        for i in range(quantidade):
            container = desempilha_container(containers)
            print("Desempilhando " + container)
    elif opcao == '3':
        print(containers)
    elif opcao == '0':
        break
    else:
        print("Opção inválida, tente novamente!")

print(containers)
