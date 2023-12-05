class Grafo:

    # Inicializa o grafo a partir da quantidade de vertices
    def __init__(self, vertices):
        self.vertices = vertices
        # O Grafo será representado por uma matriz, 
        # começa com zero pois nenhum vertice possui está conectado com outros ainda
        self.grafo = [[0]*vertices for x in range(vertices)]
    

    def adiciona_aresta(self, u, v):
        # Adiciona o valor na linha e coluna onde a aresta irá entrar
        self.grafo[u-1][v-1] = 1
        pass

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def tem_aresta(self, u, v):
       pass

grafo = Grafo(5)
grafo.adiciona_aresta(1, 3)
grafo.adiciona_aresta(1, 4)
grafo.adiciona_aresta(1, 5)

grafo.mostra_matriz()