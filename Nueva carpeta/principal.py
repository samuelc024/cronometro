from cronometro import Cronometro

c= Cronometro()
h,m,s=str(input("Ingrese las horas, minutos y segundos que desea contar respectivamente separados por un espacio (hh mm ss):\n")).split(" ")
h=int(h)
m=int(m)
s=int(s)
s= s + (h*3600) + (m*60)
input("\nPresione enter para iniciar el conteo...")
for i in range(s+1):
    if c.segundo.valor//10==0:
        if c.minuto.valor//10==0:
            if c.hora.valor//10==0:
                print("0"+str(c.hora.valor)+":0"+str(c.minuto.valor)+":0"+str(c.segundo.valor))
            else:
                print(str(c.hora.valor)+":0"+str(c.minuto.valor)+":0"+str(c.segundo.valor))
        else:
            if c.hora.valor//10==0:
                print("0"+str(c.hora.valor)+":"+str(c.minuto.valor)+":0"+str(c.segundo.valor))
            else:
                print(str(c.hora.valor)+":"+str(c.minuto.valor)+":0"+str(c.segundo.valor))
    else:
        if c.minuto.valor//10==0:
            if c.hora.valor//10==0:
                print("0"+str(c.hora.valor)+":0"+str(c.minuto.valor)+":"+str(c.segundo.valor))
            else:
                print(str(c.hora.valor)+":0"+str(c.minuto.valor)+":"+str(c.segundo.valor))
        else:
            if c.hora.valor//10==0:
                print("0"+str(c.hora.valor)+":"+str(c.minuto.valor)+":"+str(c.segundo.valor))
            else:
                print(str(c.hora.valor)+":"+str(c.minuto.valor)+":"+str(c.segundo.valor))
    if  i==s:
        print("\n\tCONTEO FINALIZADO\n")
    c.avanzar()