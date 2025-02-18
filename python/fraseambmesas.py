end:bool = False
contador:int = 0
frasesmax:str = ""
maximo:int = 0

def main():
    while not end:
        menu()

def menu():
    global end
    frase:str = input("Escribe una frase: \n")
    if frase == "fi":
        end = True
    else:
        contar(frase)
    print("La frase con mas 'a' es: ",frasesmax,"tiene",maximo,"a's")

def contar(frase:str):

    global contador
    global maximo
    global frasesmax
    contador = 0
    for letra in frase:
        if letra.lower() == "A".lower():
            contador += 1
    if contador > maximo:
        frasesmax = frase
        maximo = contador
    return maximo
main()

