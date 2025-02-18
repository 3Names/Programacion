def calculate() -> None:
    x = int(input("Primer numero: "))
    y = int(input("Segundo numero: "))
    op = int(input("Elige accion: 1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Potencia 6.Raiz cuadrada 7.Salir  :"))
    if op == 1:
        print("Resultado: ",x+y)
    else:
        if op == 2:
            print("Resultado: ",x-y)
        else:
            if op == 3:
                print("Resultado: ",x*y)
            else:
                if op == 4:
                    if y == 0:
                        print("No se puede dividir entre 0")
                    print("Resultado: ",float(x/y))
                else:
                    if op == 5:
                        print("Resultado: ",x**y)
                    else:
                        if op == 6:
                            print("Resultado: ",x**(1/2))
                        else:
                            if op == 7:
                                print("Adios")
calculate()
