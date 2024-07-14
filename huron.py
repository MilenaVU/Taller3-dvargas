from AnimalExotico import AnimalExotico

class Huron(AnimalExotico):

    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos:float) -> None:
        super().__init__(nombre,peso,edad,pais_origen,impuestos)

    def hacer_sonido(self):
        return "¡Eek Eek!"
    

    def comer(self):
        #se define vacio
        pass

    def getKilosComidos(self):
        # se define vacio
        return 0
     