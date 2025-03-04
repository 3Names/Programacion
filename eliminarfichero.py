import os
ruta = input("Directorio: ")
ruta_absoluta = str(ruta)
test = os.scandir(ruta)
recorrido = False
while recorrido != True:
    with test as it:
        for entry in it:
            if entry.name.startswith('.') and entry.is_file():
                os.remove(entry)
                print(entry)
            if entry.is_dir():
                ruta_absoluta = ruta_absoluta + "/" + entry.name
                test = os.scandir(entry)
                print(ruta_absoluta)
                print(entry)
            if not os.listdir(entry):
                recorrido = True
                os.removedirs(ruta_absoluta)
