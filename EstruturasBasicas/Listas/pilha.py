class Pilha():
    def __init__(self):
        self.listaDeElementos = []
        self.tamanho = len(self.listaDeElementos)
        self.ultimoElemento = None

    def empilha(self, elemento):
        self.ultimoElemento = elemento
        self.listaDeElementos.append(elemento)

    def estaVazia(self):
        return self.ultimoElemento is None and self.tamanho == 0

    def exibeElementos(self):
        return self.listaDeElementos

    def desempilha(self):
        self.listaDeElementos[self.tamanho] = None
        self.tamanho -= 1
        return self.ultimoElemento
