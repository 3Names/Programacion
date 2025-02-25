import os

entries = os.listdir('archivos')
scan = os.scandir('archivos')
print(entries)
print(scan)
for i in scan:
    print(i)

from pathlib import Path
p = Path('ejemplo_dir')

##########
#Crear fichero
##########
#try:
#    p.mkdir()
#except FileExistsError:
#    print("Ya existe el fichero")
try:
    os.rmdir('ejemplo_dir')
except FileNotFoundError as xd:
    print("No se encontro el fichero")
except OSError as dx:
    print("El directorio no esta vacio")

#Abre y cierra#
with open("archivos/xd4.txt", "w") as fd:
    for i in range(1,5):
        word = input(f"Enter word {i}: ")
        fd.write(word + '\n')

#with open("archivos/xd4.txt", "r") as fd:
#    for line in fd.readlines():
#        print(line)

try:
    with open("archivos/xd4.txt", "rb") as fd:
        print(fd.tell())
        print(fd.read())
        print(fd.tell())
        fd.seek(12, os.SEEK_SET)
        print(fd.tell())
        fd.seek(-3, os.SEEK_CUR)
        fd.seek(-2, os.SEEK_END)
        print(fd.tell())
        for line in fd.readlines():
            print(line)

        os.remove("archivos/xd4.txt")
except FileNotFoundError as kekw:
    print(kekw)


