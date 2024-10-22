# nome = input("Informe seu nome: ")

# para 
# lista

#nomes = ["Marcos", "Maria", "Ana", "Nairim", "João", "Paula"]
# 0, 1, 2, 3

# Para cada nome em nomes, você printe
# [0, 1, 2,3, 4, 5..99]
# length - tamanho, quantidade
#for cont in range(len(nomes)):
#    print(nomes[cont])

# s ou n
maisUma = "s"
notas = []
# enquanto - teste (if) True ou False
while maisUma == "s":
    nota = float(input("informe uma nota: "))
    notas.append(nota)
    maisUma = input("Você quer adicionar uma nova nota? [s/n]")

soma = 0
for nota in notas:
    soma = soma + nota 
print(soma)


#for i in range(10):
#    nota = float(input("Informe uma nota#: "))






