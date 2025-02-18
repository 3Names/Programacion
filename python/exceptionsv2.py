def main():
    try:
        validacion(int(input("Introduce un numero: ")))
    except ValueError as dx:
        print(dx)

def validacion(a:int) -> int:
    if type(a) != int:
        raise ValueError
    return a

main()
