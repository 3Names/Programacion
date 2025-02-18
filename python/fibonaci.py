def fibonaci() -> int:
    N:int = input("Introduce un numero: ")
    i:int = 1
    num1 = 1
    num2 = 1
    siguiente = num2
    while i <= int(N):
        print(num2)
        i = i + 1
        num1, num2 = num2, siguiente
        siguiente = num1 + num2
fibonaci()
        
