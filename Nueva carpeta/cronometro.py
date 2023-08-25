from hora import Hora 
from minuto import Minuto 
from segundo import Segundo 
import time 
class Cronometro():
    def __init__(self):
        self.hora=Hora()
        self.minuto=Minuto()
        self.segundo=Segundo()
    def avanzar(self):
        time.sleep(1)
        self.segundo.avanzar()
        if self.segundo.valor ==0:
            self.minuto.avanzar()
            if self.minuto.valor ==0 :
                self.hora.avanzar()
