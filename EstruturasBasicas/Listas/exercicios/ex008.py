# Problema do parenteses balanceados
from Listas.PilhaImplementacao import Pilha


def parentesesCheck(cadeiaString):
    pilhaParentese = Pilha()
    balanceada = True
    index = 0
    while index < len(cadeiaString) and balanceada:
        caractere = cadeiaString[index]
        if caractere == "(":
            pilhaParentese.empilha(caractere)
        else:
            if pilhaParentese.esta_vazia():
                balanceada = False
            else:
                pilhaParentese.desempilha()

        index = index + 1

    if balanceada and pilhaParentese.esta_vazia():
        return True
    else:
        return False


parenteses = input("Informe a expressão: ").split(" ")
if parentesesCheck(parenteses):
    print("Está balanceado")
else:
    print("Não está balanceado")
