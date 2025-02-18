matriu = [[1, 2, 3], [3, 8], [1, 8, 7]]

print("Matriu inicial")
for fila in matriu:
    for element in fila:
        print(element, end=" ")
    print()

#Les vostres modificacions comencen aqui

i:int = 0
for fila in matriu:
    j:int = 0
    for element in fila:
        matriu[i][j] = element + 1
        j = j + 1
    i = i + 1

    
#Aqui ja han acabat les vostres modificacions


print("Matriu final:")
for fila in matriu:
    for element in fila:
        print(element, end=" ")
    print()
