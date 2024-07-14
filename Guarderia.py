from Animal import Huron, Boa_Constrictor

class Guarderia:
    def __init__(self):
        self.boas = [Boa_Constrictor("Boa1", 20, "Brasil", 15), Boa_Constrictor("Boa2", 25, "Peru", 20)]
        self.hurones = [Huron("Huron1", 5, "Colombia", 10), Huron("Huron2", 6, "Argentina", 12)]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.alimentar()
            return "Éxito"
        except ValueError:
            return "La boa está llena"
