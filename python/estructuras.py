a:tuple = ("pedro","dos","tres",8,7,8)
b:tuple = ("diego","veinte","treinta",1,9,8)
c:tuple = ("vicente","doscientos","trescientos",3,5,9)
j:int = 0
dx:int = 0
trio:list = [a,b,c]
primero:list = ["Media superior a 7","\n"]
segundo:list = ["Nota superior a 8 en cualquier prueba","\n"]
def calcular(alumne:tuple) -> int:
    media:int = (alumne[3] * 30 / 100) + (alumne[4] * 40 / 100) + (alumne[5] * 30 / 100)
    return media
for i in trio:
    xd = calcular(i)
    if xd > 7:
        primero.append(trio[j][0] + " " + str(xd))
    j = j + 1
for i in trio:
    if i[3] > 8 or i[4] > 8 or i[5] > 8:
        segundo.append(trio[dx][0])
    dx = dx + 1    
for k in primero:
    print(k)
for w in segundo:
    print(w)
