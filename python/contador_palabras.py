def contar(frase:str) -> int:
    palabra:int = 1
    contador:int = 1
    i:int = 0
    frase_aux:str = [None]
    while frase_aux != list(frase):
        frase_aux = [None]*contador
        i = 0
        palabra = 1 
        while i < contador:
            frase_aux[i] = frase[i]
            if frase[i] == ' ':
                palabra = palabra + 1
            i = i +1
        contador = contador + 1
    return palabra

num_palabras = contar(" ")
print("Numero de palabras: " + str(num_palabras))
