import os
entries = os.listdir('.')
ruta = input("Introduce una ruta")

for entry in entries:
    if ruta.isfile():
        print("xd")
