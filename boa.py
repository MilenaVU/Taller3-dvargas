from AnimalExotico import AnimalExotico

class Boa_Constrictor(AnimalExotico):
    def __init__(self, nombre: str,peso: float,edad:int, pais_origen: str, impuestos: float, ratones:int):
        super().__init__(nombre,peso,edad,pais_origen, impuestos)
        self.ratones_comidos = ratones


    def getKilosComidos(self):
        return self.ratones_comidos
 
    def comer(self):
        self.ratones_comidos += 1

    def hacer_sonido(self):
        return "¡Tsss!"
    