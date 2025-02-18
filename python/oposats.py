def oposito(a:str, b:str) -> bool:
    a_lista = list(a)
    b_lista = list(b)
    if a == "" or a == " ":
        return False
    if b == "" or a == " ":
        return False
    if len(a) != len(b):
        return False
    for i in range(len(a_lista)):
        if a_lista[i].lower() != b_lista[i].lower():
            return False
        if a_lista[i] == b_lista[i]:
            return False
        if a_lista[i].islower():
            a_lista[i] = a_lista[i].upper()
        else:
            a_lista[i] = a_lista[i].lower()
    a = ''.join(a_lista)

    return a == b
print(oposito("XD","xd"))
