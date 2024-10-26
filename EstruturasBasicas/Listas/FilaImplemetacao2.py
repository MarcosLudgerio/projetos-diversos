class Fila:
    def __init__(self):
        self.__fila = []
        self.__tamanho = 0
        self.__head = None
        self.__tail = None

    @property
    def fila(self):
        return self.__fila

    def enfileirar(self, item):
        self.__fila.append(item)
        self.__tamanho = self.__tamanho + 1
        self.__tail = self.__fila[-1]
        self.__head = self.__fila[0]

    def desinfileirar(self):
        if self.__tamanho == 0:
            return
        item = self.__head
        del (self.__fila[0])
        self.__head = self.__fila[0]
        return item

    def __repr__(self):
        return str(self.__fila)

    def ver_tail(self):
        return self.__tail

    def ver_head(self):
        return self.__head

    def ver_tamanho(self):
        return self.__tamanho
    