from cronometro import Cronometro

c = Cronometro()

for i in range(999):
    print(c.hora.valor ,c.minuto.valor, c.segundo.valor )
    c.avanzar()