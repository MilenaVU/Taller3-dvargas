from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def calcular_flete(self):
        pass

class Animal(IAnimal):
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def hacer_sonido(self):
        pass

    def calcular_flete(self):
        pass

class Animal_Exotico(Animal):
    def __init__(self, nombre, peso, pais_origen, impuestos):
        super().__init__(nombre, peso)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    def calcular_flete(self):
        return self.peso * self.impuestos

class Huron(Animal_Exotico):
    def hacer_sonido(self):
        return "¡Eek Eek!"

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre, peso, pais_origen, impuestos):
        super().__init__(nombre, peso, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def alimentar(self):
        if self.ratones_comidos >= 10:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1
