import os
from pathlib import Path
basepath = '.'
ruta=input("Introduce ruta de un fichero: ")
#for entry in os.listdir(basepath):
#    if not os.path.isfile(os.path.join(basepath, entry)):
#        print(entry)


for entry in os.scandir(basepath):
    ruta = os.path.basename(ruta)
    if entry.is_file() and entry.name == ruta:
        print(ruta.split(basepath)[0])
        print("encontrado!!")

#docs.python.org/3/library/os.html
#docs.python.org/3/library/pathlib.html
