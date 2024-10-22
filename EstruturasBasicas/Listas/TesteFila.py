from Fila import Fila
fila = Fila()

fila.enqueue(2)
fila.enqueue(5)
fila.enqueue(8)
fila.enqueue(9)

fila.exibe_fila()

print(fila.dequeue())


fila.exibe_fila()

print(fila.mostrar_calda())
print(fila.mostrar_cabeca())