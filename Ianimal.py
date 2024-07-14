from abc import ABC, abstractmethod

class IAnimal(ABC):
 @abstractmethod
 def comer (self, kilos):
  pass
 
 @abstractmethod
 def getKilosComidos (self, kilos):
  pass
 
@abstractmethod
def hacer_sonido(self):
  pass

 
