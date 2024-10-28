class Pilha:
    def __init__(self):
        self.listaDeElemtos = []
        self.tamanho = 0
        self.topo = None

    def __repr__(self):
        return str(self.listaDeElemtos)

    def empilha(self, elemento):
        self.topo = elemento
        self.listaDeElemtos.append(elemento)
        self.tamanho += 1

    def esta_vazia(self):
        return self.tamanho == 0

    def desempilha(self):
        if self.esta_vazia():
            return
        elemento = self.topo

        # elemento = self.listaDeElemtos[self.tamanho - 1]
        del (self.listaDeElemtos[self.tamanho - 1])
        self.tamanho -= 1
        if self.tamanho > 0:
            self.topo = self.listaDeElemtos[self.tamanho - 1]
        return elemento

    def ver_topo(self):
        if self.esta_vazia():
            return
        return self.topo

    def ver_tamanho(self):
        if self.esta_vazia():
            return 0
        return self.tamanho

    def limparPilha(self):
        self.listaDeElemtos = []
