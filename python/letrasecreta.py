import random

finalizado:bool = False
letras:str
def pistas(respuesta):
    
def randomwords():
    numero:int = random.randint(0,4)
    print(numero)

def idk():
    xd:int = 0

def gestion():
    global letras
    global finalizado
    respuesta:str = input("Escribe 5 letras minusculas: ")
    if respuesta == letras:
        finalizado = True
    else pistas(respuesta)

def main():
    randomwords()
    print("Adivina la secuencia de letras")
    while finalizado == False:
        gestion()
    if finalizado == True:
        print("Enhorabuena, has ganado!!")
main()
