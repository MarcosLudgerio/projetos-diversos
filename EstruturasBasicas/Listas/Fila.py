class Fila:
    def __init__(self):
        self.lista = []
        self.tamanho = 0

    def enfileirar(self, elemento):
        self.lista.append(elemento)
        self.tamanho += 1

    def desenfileirar(self):
        if self.tamanho == 0:
            return
        elemento = self.lista.pop(0)
        self.tamanho -= 1
        return elemento

    def mostrar_cabeca(self):
        if self.tamanho == 0:
            return
        return self.lista[0]

    def mostrar_calda(self):
        if self.tamanho == 0:
            return
        return self.lista[-1]

    def exibe_fila(self):
        print(self.lista)

    def ver_tamanho(self):
        return self.tamanho


