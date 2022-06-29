from arista import Arista
from nodo import Nodo
from collections import deque
from queue import PriorityQueue

class Grafo: 
    def __init__(self) -> None:
        self.__aristas = []
        self.__ady = {}

    def agregar_aristas(self, arista:Arista):
        if arista not in self.__aristas:
            self.__aristas.append(arista)

    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])

    def eliminar_arista(self, arista:Arista):
        self.__aristas.remove(arista)

    def get_lista_ady(self) -> dict:
        self.__ady.clear()

        for arista in self.__aristas:
            if arista.dirigido():
                n1 = arista.get_Nodo1()
                n2 = arista.get_Nodo2()
                peso = arista.peso

                self.agregar_dict(n1, n2, peso)
            else:
                n1 = arista.get_Nodo1()
                n2 = arista.get_Nodo2() 

                self.agregar_dict(n1, n2, arista.peso)
                self.agregar_dict(n2, n1, arista.peso)
        return self.__ady

    def print_ady(self):
        self.get_lista_ady()
        for key in self.__ady.keys():
            print(key, "----->")
            for value in self.__ady[key]:
                nodo = value[0]
                peso = value[1]
                print(f"[{nodo}, {peso}]", ",",  end="")
            print("\n")

    def print_plaintext(self, grafo: dict):
        cadena = ""
        for key in grafo.keys():
            cadena = cadena + str(key) + "------>"
            for value in grafo[key]:
                nodo = value[0]
                peso = value[1]
                cadena = cadena + "[" + str(nodo) + str(int(peso)) + ")" + "]" + "  "
            cadena = cadena + "\n"
        return cadena

    def print_grafo(self, grafo: dict):
        cadena = ""
        for key in grafo.keys():
            cadena = cadena + str(key) + "------>"
            for value in grafo[key]:
                nodo = value[0]
                cadena = cadena + str(nodo)
            cadena = cadena + "\n"
        return cadena

    def agregar_dict(self, n1, n2, peso):
        if n1 in self.__ady:
            self.__ady[n1].append([n2, peso])
        else:
            self.__ady[n1] = [[n2, peso]]

    def recorrido_profundidad(self, origen: Nodo):
        pila = deque()
        visitados = []
        recorrido = []

        grafo = self.get_lista_ady()

        if origen not in grafo:
            return recorrido

        pila.append(origen)
        visitados.append(origen)

        while len(pila) > 0:
            vertice = pila.pop()
            recorrido.append(vertice)
            for ady in grafo[vertice]:
                if ady[0] not in visitados:
                    pila.append(ady[0])
                    visitados.append(ady[0])
        return recorrido

    def recorrido_anchura(self, origen: Nodo):
        cola = deque()
        visitados = []
        recorrido = []

        grafo = self.get_lista_ady()

        if origen not in grafo:
            return recorrido

        cola.append(origen)
        visitados.append(origen)

        while len(cola) > 0:
            vertice = cola.popleft()
            recorrido.append(vertice)
            for ady in grafo[vertice]:
                if ady[0] not in visitados:
                    cola.append(ady[0])
                    visitados.append(ady[0])
        return recorrido
        
    def alg_prim(self, inicio: Nodo):
        g_resultante = {}
        visitados = []
        grafo_r = []
        pq = PriorityQueue()

        visitados.append(inicio)

        for ady in self.__ady[inicio]:
            pq.put((ady[1], inicio, ady[0]))

        while not pq.empty():
            arista = pq.get()
            peso = arista[0]
            origen = arista[1]
            destino = arista[2]

            if destino not in visitados:
                visitados.append(destino)
                for ady in self.__ady[destino]:
                    if ady[0] not in visitados:
                        pq.put((ady[1], destino, ady[0]))

                grafo_r.append(arista)
                if origen in g_resultante:
                    g_resultante[origen].append([destino, peso])
                else:
                    g_resultante[origen] = [[destino, peso]]

                if destino in g_resultante:
                    g_resultante[destino].append([origen, peso])
                else:
                    g_resultante[destino] = [[origen, peso]]
        return g_resultante, grafo_r

    def kruskal(self, grafo: dict):
        arbol = []
        lista = []
        g_resultante = {}

        for nodo, adyacentes in grafo.items():
            for ady in adyacentes:
                peso = ady[1]
                destino = ady[0]
                arista = peso, nodo, destino
                lista.append(arista)

        lista.sort(key=lambda arista:arista[0])

        ds = self.make_set(grafo)
        print("Conjunto: " + self.imprimir_1ds(ds))

        while len(lista) > 0:
            arista = lista[-1] 
            lista.pop()

            peso = arista[0]
            origen = arista[1]
            destino = arista[2]

            if self.find_set(origen, ds) != self.find_set(destino, ds):
                arbol.append(arista)
                self.union(origen, destino, ds)
                print("arista: " + "(" + str(peso) + ",", str(origen), str(destino) + ")")
                print(self.imprimir_ds(ds))

                if origen in g_resultante:
                    g_resultante[origen].append([destino, peso])
                else:
                    g_resultante[origen] = [[destino, peso]]
                if destino in g_resultante:
                    g_resultante[destino].append([origen, peso])
                else:
                    g_resultante[destino] = [[origen, peso]]

        return arbol, g_resultante

    def dijkstra(self, inicio: Nodo):
        distancias = {}
        camino = {}

        for nodo in self.__ady:
            distancias[nodo] = 10000
            camino[nodo] = ""

        distancias[inicio] = 0
        camino[inicio] = inicio

        pq = PriorityQueue()
        pq.put((0, inicio))

        while not pq.empty():
            nodo = pq.get()
            n = nodo[1] 

            for arista in self.__ady[n]:
                distancia = arista[1] + nodo[0]
                destino = arista[0]

                if distancia < distancias[destino]:
                    distancias[destino] = distancia
                    camino[destino] = n
                    pq.put((distancia, destino))
        return distancias, camino 

    def make_set(self, grafo):
        ds = []

        for nodo in grafo:
            ds.append([nodo])

        return ds

    def find_set(self, nodo, ds):
        i = 0
        while i < len(ds):
            if nodo in ds[i]:
                return i
            i += 1

    def union(self, origen, destino, ds):
        i = self.find_set(origen, ds)
        j = self.find_set(destino, ds)

        lista_origen = ds[i]
        lista_destino = ds[j] 
        lista_union = lista_origen + lista_destino

        ds.remove(lista_origen)
        ds.remove(lista_destino)
        ds.append(lista_union)

    def imprimir_ds(self, ds: list):
        cadena = "[ "
        for arista in ds:
            cadena += "["
            for nodo in arista:
                cadena += str(nodo)
            cadena += "] " 
        cadena += "]" + "\n"
        return cadena

    def imprimir_1ds(self, ds: list):
        cadena = "[ "
        for arista in ds:
            for nodo in arista:
                cadena += "[" + str(nodo) + "] "
                StopIteration()
        cadena += "]" + "\n"
        return cadena 