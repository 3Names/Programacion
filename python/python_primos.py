def numeroprimo() -> None:
    x = int(input("Numero a verificar si es primo: "))
    i: int = 2
    es_primo: bool = True
    while x < 2:
        print("Introduce un numero valido")
        x = int(input("Introduce un numero mayor que 1: "))

    while i <= x ** 0.5 and es_primo == True:
        if x % i == 0:
            es_primo = False
        else:
            es_primo = True
        i = i + 1

    if es_primo == True:
        print("Es primo")
    else:
        print("No es primo")
numeroprimo()
