questions:list = ["Cuanto es 24x25?","Cual es la capital de Grecia?","Como se escribe 46 en hexadecimal?","Cuantos dias tiene Marzo?","Cuantos minutos hay en 15 dias?"]
answer:list = ["600","Atenas","2E","31","21600"]

#####################
playing:bool = False
indice:int = 0
score:int = 0
##################
seed:int = int(input("Introduce un numero: "))
seed = (seed*997)%1000
random:int = (seed*503)%1000/1000
index:int = int(random*(len(questions)))
print(index)
##################
#idk:int =input("Elija una opcion: 1)Jugar 2)Salir\n")
#if idk == "1":
#    playing = True
#else:
#    playing = False
#    print("Adios")
#while playing == True:
    
if index <= 8:
    indice = 0
    print(questions[indice])
    input("Respuesta: ")
if index > 8 and index <= 16:
    indice = 1
    print(questions[indice])
    input("Respuesta: ")
if index > 16 and index <= 24:
    indice = 2
    print(questions[indice])
    input("Respuesta: ")

if index > 24 and index <= 32:
    indice = 3
    print(questions[indice])
    input("Respuesta: ")

if index > 32:
    indice = 4
    print(questions[indice])
    input("Respuesta: ")
