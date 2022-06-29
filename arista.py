from nodo import Nodo

class Arista:
    def __init__(self, n1:Nodo, n2:Nodo) -> None:
        self.__par = [n1, n2] 

    def get_par(self) -> list:
        return self.__par

    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]}) ?------Arista------? (Nodo: {self.get_par()[1]})"

    def dirigido(self) -> bool:
        return False

    def ponderado(self) -> bool:
        return True

    def __eq__(self, o: object) -> bool:
        return self.get_par()[0] == o.get_par()[0] and self.get_par()[1] == o.get_par()[1]

class ArsitaNoDirigida(Arista):
    def __init__(self, n1: Nodo, n2: Nodo) -> None:
        super().__init__(n1, n2)

    def dirigido(self) -> bool:
        return False

    def ponderado(self) -> bool:
        return False 

    def get_Nodo1(self) -> Nodo:
        return self.get_par()[0]

    def get_Nodo2(self) -> Nodo:
        return self.get_par()[1] 

    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]}) <------Arista------> (Nodo: {self.get_par()[1]})"

class Ponderada:
    def __init__(self, peso) -> None:
        self.__peso = peso 

    @property
    def peso(self):
        return self.__peso

class AristaNoDirigidaPonderada(ArsitaNoDirigida, Ponderada):
    def __init__(self, n1: Nodo, n2: Nodo, peso) -> None:
        ArsitaNoDirigida.__init__(self, n1, n2)
        Ponderada.__init__(self, peso)

    def ponderado(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]}) <------Arista: {self.peso}------> (Nodo: {self.get_par()[1]})"

class AristaDirigidaPonderada(Arista, Ponderada):
    def __init__(self, n1: Nodo, n2: Nodo, peso) -> None:
        Arista.__init__(self, n1, n2)
        Ponderada.__init__(self, peso)

    def ponderado(self) -> bool:
        return True

    def dirigido(self) -> bool:
        return True

    def get_Nodo1(self) -> Nodo:
        return self.get_par()[0]

    def get_Nodo2(self) -> Nodo:
        return self.get_par()[1] 

    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]}) Arista: {self.peso}------> (Nodo: {self.get_par()[1]})"
