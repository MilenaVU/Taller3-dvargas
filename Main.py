from boa import Boa_Constrictor
from huron import Huron

# insertar datos para cerar Boa
print("--------Datos Boa---------")
Boa1 = Boa_Constrictor("serpentina",20, 3, "Australia", 500, 2)
print(f"Nombre de la Boa: {Boa1._nombre}")  # Imprimir nombre de la boa
print(f"Flete de la Boa: {Boa1.calcular_flete()}")  
print(f"Sonido que hace la Boa : {Boa1.hacer_sonido()}")  
Boa1.comer()
print(f"Ratones comidos por la Boa: {Boa1.getKilosComidos()}")  


# insertar datos para cerar huron
print("---------Datos Huron------------")
Huron1 = Huron("Amatista", 2, 3, "USA", 500)
print(f"Nombre del Hurón: {Huron1._nombre}")
print(f"Peso del Hurón: {Huron1._peso}")
print(f"Edad del Hurón: {Huron1._edad}")
print(f"País de origen del Hurón: {Huron1._pais_origen}")
print(f"Impuestos del Hurón: {Huron1._impuestos}")
print(Huron1.hacer_sonido())  # ¡Eek Eek!
print(f"Flete del Hurón: {Huron1.calcular_flete()}") 