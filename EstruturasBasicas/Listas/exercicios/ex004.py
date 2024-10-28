# Funções desafazer e refazer de documentos
from PilhaImplementacao import Pilha

pilhaFaz = Pilha()
pilhaDesfaz = Pilha()


def empilha_acao(pilha_faz, acao):
    pilha_faz.empilha(acao)


def desfazer(pilha_desfazer, pilha_refazer):
    if pilha_refazer.esta_vazia():
        print("Todas as alterações foram desfeitas!")
        return
    pilha_desfazer.empilha(pilha_refazer.desempilha())


def refazer(pilha_desfazer, pilha_refazer):
    if pilha_desfazer.esta_vazia():
        print("Todas as alterações foram refeitas!")
        return
    pilha_refazer.empilha(pilha_desfazer.desempilha())


while True:
    texto = str(input("Informe o texto: ")).split(" ")
    if str.lower(texto[0]) == "z":
        break
    elif str.lower(texto[0]) == "d":
        desfazer(pilhaDesfaz, pilhaFaz)
    elif str.lower(texto[0]) == "r":
        refazer(pilhaDesfaz, pilhaFaz)
    else:
        for letra in texto:
            empilha_acao(pilhaFaz, letra)
    for letra in pilhaFaz.listaDeElemtos:
        print(letra, end=' ')
    print("")
