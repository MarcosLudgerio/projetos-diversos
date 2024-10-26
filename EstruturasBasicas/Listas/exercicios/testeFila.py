from FilaImplemetacao2 import Fila


alunos = Fila()

alunos.enfileirar("João")
alunos.enfileirar("Maria")
alunos.enfileirar("Paula")
alunos.enfileirar("Joana")
alunos.enfileirar("Renan")
alunos.enfileirar("Nilzah")
alunos.enfileirar("Micaele")

print(alunos)

print(alunos.ver_head())
print(alunos.ver_tail())

print(alunos.desinfileirar())
print(alunos.desinfileirar())
print(alunos.desinfileirar())


print(alunos)

