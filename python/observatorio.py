import datetime as dt
creado:bool = False
estado:bool = True
class registro:
    semana:list
    def __init__(self,a:int, b:int, c:int, d:int, e:int, f:int, g:int):
        self.semana = [a,b,c,d,e,f,g]
    def mostrar(self):
        for i in range(0,7):
            print(self.semana[i])
        print(self.semana)
while estado == True:
    print("Bienvenido al registro de temperaturas")
    print("--------------------------------------")
    accion:str = input("""[RT] = Registrar temperaturas semanales\n
[MJ] Consultar media de temperaturas\n
[DF] Consultar diferencia maxima\n
[FI] Salir \n
Opcion: """)
    if accion == "RT":
        miregistro = registro(21,32,41,12,32,43,15).mostrar()
        creado = True
    if accion == "MJ" and creado == True:
        print("2")
    if accion == "DF" and creado == True:
        print("3")
    if accion == "FI":
        print("Adios")
        estado = False
