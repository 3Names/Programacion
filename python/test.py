def generar_lista_numeros_primos(a:int, b:int) -> list:
    lista:list[int] = []
    es_primo:bool = True
    indice_lista_primos:int = 0
    numeros_a_dividir_para_saber_si_es_primo:int = 2
    cantidad_de_numeros_primos:int = 0

    # Mientras a sea menor o igual que b haremos algo.
    while a <= b:
        lista = lista[cantidad_de_numeros_primos]
        es_primo = True
        # Mientras que j sea menor o igual que la raiz cuadrada de a y sea primo 
        # haremos algo
        while numeros_a_dividir_para_saber_si_es_primo <= a ** 0.5 and es_primo == True:
            # Si a modulo j es 0 entonces 'a' no es primo
            if a % numeros_a_dividir_para_saber_si_es_primo == 0:
                es_primo = False
            # Si no, si que es primo e incrementamos un contador en uno, 
            # haciendo que la lista tenga tanto elementos como contador, pero
            # esta estara totalmente vacia, y en la posicion i introduciremos
            # el valor de 'a', luego incrementaremos i e incrementaremos j
            else:
                es_primo = True
                numeros_a_dividir_para_saber_si_es_primo = numeros_a_dividir_para_saber_si_es_primo + 1
                
        if es_primo == True:
            cantidad_de_numeros_primos = cantidad_de_numeros_primos + 1
            lista[indice_lista_primos] = a
            indice_lista_primos = indice_lista_primos + 1
        # Incrementaremos 'a' hasta llegar a 'b'
        a = a + 1

    return lista
result = generar_lista_numeros_primos(4,20)
print(result)
