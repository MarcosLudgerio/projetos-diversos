from PilhaImplementacao import NossaPilha

pilhaTeste = NossaPilha()



# Criar uma função que verifica se uma cadeia de caractere é um anpalidromo usando pilha
def e_palidromo(palavra):
    direta = NossaPilha()
    for letra in palavra:
        direta.empilha(letra)
    for letra in palavra:
        letraI = direta.desempilha()
        if letra != letraI:
            return False
    return True



print(e_palidromo('a mae te ama'))
print(e_palidromo('radar'))
print(e_palidromo('mae te ama'))



