from Animal import Animal
from abc import ABC,abstractmethod

#definir clase animal Exotico
class AnimalExotico(Animal):
    def __init__(self, nombre:str, peso: float, edad: int, pais_origen:str, impuestos:float) ->None:
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos



    def getPais_origen(self) ->str:
        return self._pais_origen
    
    
    def getImpuestos(self) ->float:
        return self._impuestos
    
    def calcular_flete(self) ->float:
        return self._impuestos*self._impuestos
    
    @abstractmethod
    def  hacer_sonido (self) -> str:
        pass