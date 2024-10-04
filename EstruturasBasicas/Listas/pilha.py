class Pilha():
    def __init__(self):
        self.listaDeElementos = []
        self.tamanho = len(self.listaDeElementos)
        self.topo = None

    def empilha(self, elemento):
        self.topo = elemento
        self.listaDeElementos.append(elemento)
        self.tamanho += 1

    def estaVazia(self):
        return self.topo is None and self.tamanho == 0

    def exibeElementos(self):
        return self.listaDeElementos

    def desempilha(self):
        if self.estaVazia():
            return "A Pilha está vazia"
        elemento = self.topo
        self.listaDeElementos.remove(elemento)
        self.tamanho -= 1
        if self.tamanho == 0:
            self.topo = None
            return elemento
        self.topo = self.listaDeElementos[self.tamanho - 1]
        return elemento

    def topo(self):
        if self.estaVazia():
            return
        return self.topo
