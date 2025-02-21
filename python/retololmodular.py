champs:list = ["Guerrero","Mago","Tanque","Asesino"]
i:int = 0
correcto:bool = False

def efectividad(ch_atk:str, ch_def:str, atk:int, dfc:int):
    if ch_atk == "Guerrero" and ch_def == "Mago":
        print("Es super efectivo")
        calcular_dano(atk*2,dfc)
    elif ch_atk == "Mago" and ch_def == "Tanque":
        print("Es super efectivo")
        calcular_dano(atk*2,dfc)
    elif ch_atk == "Tanque" and ch_def == "Asesino":
        print("Es super efectivo")
        calcular_dano(atk*2,dfc)
    elif ch_atk == "Asesino" and ch_def == "Guerrero":
        print("Es super efectivo")
        calcular_dano(atk*2,dfc)
    else:
        calcular_dano(atk,dfc)

def seleccion():
    global correcto
    ch_atk:str = input("Elige un tipo de Campeon atacante: ")
    ch_def:str = input("Elige un tipo de Campeon defensor: ")
    atk:int = int(input("Daño del atacante(10-200): "))
    dfc:int = int(input("Defensa del defensor(5-150): "))
    while correcto != True:
        if ch_atk not in champs or ch_def not in champs:
            print("Por favor seleccione un tipo de Campeon valido\n")
            ch_atk = input("Campeon atacante: ")
            ch_def = input("Campeon defensor: ")
        elif atk > 200 or atk < 10 or dfc < 5 or dfc > 150:
            print("Elija un valor valido\n")
            atk = int(input("Daño del atacante(10-200): "))
            dfc = int(input("Defensa del defensor(5-150): "))
        else:
            correcto = True
            efectividad(ch_atk,ch_def,atk,dfc)

def calcular_dano(atk:int, dfc:int):
    dano:int = 100 * (atk/dfc)
    print("Daño: "+ str(dano))

def main():
    print("Elije un enfrentamiento!!\nTipos de campeones: Guerrero, Mago, Tanque, Asesino.\n")
    seleccion()
main()
