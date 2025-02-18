def main():
    try:
        print(tipe((input("Primer numero: ")),(input("Segundo numero: "))))
    except TypeError as dx:
        print(dx)

def tipe(a:str,b:str) -> int:
    if a.isnumeric() == False or b.isnumeric() == False:
        raise TypeError("Uno o ambos numeros no son numericos")
    return a,b

main()
