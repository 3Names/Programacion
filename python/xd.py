def longitud(elemento) -> None:
    xd:int = 0
    cadena:str = input("POn algo: ")
    i:int = 0
    for i in cadena:
        xd += 1
    print(xd)
longitud("hola")
