from Listas.PilhaImplementacao import Pilha
from Listas.FilaImplemetacao2 import Fila

numeros = Pilha()

numeros.empilha(10)
numeros.empilha(15)
print(numeros.desempilha())
numeros.empilha(23)
print(numeros.esta_vazia())
print(numeros.desempilha())
print(numeros.desempilha())
numeros.empilha(45)
print(numeros.ver_topo())
print(numeros.desempilha())
print(numeros)

times = Pilha()

times.empilha("Botafogo")
times.empilha("Palmeiras")
times.empilha("Fortaleza")
times.empilha("Flamengo")
print(times.desempilha())
print(times.ver_topo())
print(times.desempilha())
print(times.ver_tamanho())
times.empilha("São Paulo")
print(times.desempilha())
print(times)

pacientes = Fila()

pacientes.enfileirar("Adriana")
pacientes.enfileirar("Joana")
pacientes.enfileirar("Carlos")
print(pacientes.ver_tail())
pacientes.enfileirar("Dionisio")
print(pacientes.desenfileirar())
print(pacientes.desenfileirar())
pacientes.enfileirar("Edu")
pacientes.enfileirar("Flácido")
print(pacientes.ver_head())
print(pacientes.desenfileirar())
print(pacientes.desenfileirar())
pacientes.enfileirar("José")

print(pacientes)
