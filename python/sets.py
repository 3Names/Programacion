def registro() -> set:
    puertos:set(int) = set(())
    accion = int(input("Que accion quieres hacer: 1-Añadir puerto 2-Cerrar puerto 3-Mostrar puertos 4-Salir: "))
    while accion != 4:
        if accion == 1:
            anadir:int = int(input("Introduce el numero de puerto a añadir: "))
            puertos.add(anadir)
            print(puertos)
            accion = int(input("Que accion quieres hacer: 1-Añadir puerto 2-Cerrar puerto 3-Mostrar puertos 4-Salir: "))
        if accion == 2:
            eliminar:int = int(input("Introduce el puerto a eliminar: "))
            ports_aux = set()
            for p in puertos:
                if p != eliminar:
                    ports_aux.add(p)
            puertos = ports_aux
            print(puertos)
            accion = int(input("Que accion quieres hacer: 1-Añadir puerto 2-Cerrar puerto 3-Mostrar puertos 4-Salir: "))
        if accion == 3:
            print(puertos)
            accion = int(input("Que accion quieres hacer: 1-Añadir puerto 2-Cerrar puerto 3-Mostrar puertos 4-Salir: "))
        if accion == 4:
            print("Adios")
registro()

