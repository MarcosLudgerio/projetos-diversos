class Fila:
    def __init__(self):
        self.listaElementos = []
        self.tamanho = 0
    
    def enfileira(self, elemento):
        self.listaElementos.append(elemento)
        self.tamanho += 1
    
    def desinfileriar(self):
        if self.tamanho == 0:
            return
        elemento = self.listaElementos.pop(0)
        self.tamanho -= 1
        return elemento
    
    def head(self):
        if self.tamanho == 0:
            return
        return self.listaElementos[0]
    
    def tail(self):
        if self.tamanho == 0:
            return
        return self.listaElementos[-1]
    
    def exibeFila(self):
        print(self.listaElementos)