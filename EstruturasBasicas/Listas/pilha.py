class Pilha():
    def __init__(self):
        self.listaDeElementos = []
        self.tamanho = len(self.listaDeElementos)
        self.ultimoElemento = None

    def empilha(self, elemento):
        self.ultimoElemento = elemento
        self.listaDeElementos.append(elemento)
        self.tamanho += 1

    def estaVazia(self):
        return self.ultimoElemento is None and self.tamanho == 0

    def exibeElementos(self):
        return self.listaDeElementos

    def desempilha(self):
        elemento = self.ultimoElemento
        self.listaDeElementos.remove(self.ultimoElemento)
        self.tamanho -= 1
        self.ultimoElemento = self.listaDeElementos[self.tamanho - 1]
        return elemento

    def topo(self):
        if self.estaVazia():
            return
        return self.ultimoElemento
