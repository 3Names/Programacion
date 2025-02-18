def sumapars() -> int:
    x:int = int(input("Cantidad de numeros pares: "))
    resultado:int = 0
    numero:int = 1
    while numero <= x*2:
        if numero % 2 == 0:
            resultado = resultado + numero
        numero = numero + 1
    print(resultado)
sumapars()
