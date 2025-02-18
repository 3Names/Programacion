seguir:bool = True
alumnos:dict = {}

def mediaNotas() -> int:
    resultado:float = 0
    for key in alumnos:
        resultado = resultado + alumnos[key]
    resultado = resultado/len(alumnos)
    print("Nota media de los estudiantes: " + str(resultado))
    print("\n")

def mostrarAlumnos():
    print("Lista de alumnos:\n")
    for key in alumnos:
        print("Nom: " + key + ", Nota: " + str(alumnos[key]))
    print("\n")

def anadirAlumno():
    nombre:str = input("Nombre del estudiante: ")
    nota:int = int(input("Nota: "))
    alumnos[nombre] = nota
    print("Alumno añadido con exito\n")

def menu() -> int:
    print("Elige una opcion\n")
    print("1.Añadir estudiante")
    print("2.Lista de estudiantes")
    print("3.Media de notas")
    print("4.Salir")
    opcion:int = input("Opcion: ")
    print("\n")
    if opcion == "1":
        anadirAlumno()
    elif opcion == "2":
        mostrarAlumnos()
    elif opcion == "3":
        mediaNotas()
    elif opcion == "4":
        global seguir
        print("Adios")
        seguir = False

def main():
    while seguir == True:
        menu()
main()
