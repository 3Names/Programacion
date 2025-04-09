def conversor(binario:int) -> int:
    resultado:int = 0
    i:int = 0

    resultado = resultado + (binario % 10) * (2**i)
    binario = binario // 10
    i = i + 1
    while binario != 0:
        resultado = resultado + (binario % 10) * 2 **i
        binario = binario // 10
        i = i + 1
    return resultado
numero = conversor(10110011010)
print("Decimal: " + str(numero))
