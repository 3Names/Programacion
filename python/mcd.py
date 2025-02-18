def mcd() -> int:
    print("Introduce dos numeros, primero el mas grande, luego el mas pequeño" + "\n")
    num1:int = input("Introduce primer numero: ")
    num2:int = input("Introduce segundo numero: ")
    save:int = num2
    if num2 > num1:
        print("Por favor introduce primero el numero mas grande" + "\n")
    if num1 >= num2:
        while num2 != 0:
            if num2 == 0:
                return num1
            num1 = num2
            num2 = save
            save = num1 % num2
    print("El MCD es: " + str(num1))
mcd()

