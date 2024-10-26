from FilaImplementacao import Fila

filaTeste = Fila()

filaTeste.enfileira(2)
filaTeste.enfileira(4)
filaTeste.enfileira(6)


filaTeste.exibeFila()
print(filaTeste.desinfileriar())
print(filaTeste.desinfileriar())


filaTeste.enfileira(8)
filaTeste.enfileira(10)

filaTeste.exibeFila()

print(filaTeste.head())
print(filaTeste.tail())

