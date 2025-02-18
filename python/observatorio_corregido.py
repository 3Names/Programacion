temperaturas:list = []
end:bool = False

def run_options():
    option = input("Options: ")

    if option.lower() == "RT".lower():
        logger_temperature_weekly()
    elif option.lower() == "MJ".lower():
        show_average()
    elif option.lower() == "DF".lower():
        show_max_difference()
    elif option.lower() == "FI".lower():
        exit_execution()
    else:
        print("Opcion invalida. Intenta de nuevo.")

def logger_temperature_weekly():
    if(len(temperatures) + 7) > (52*7):
        print("Tenemos todas las temperaturas, No podemos ingresar mas.")
    else:
        read_temperatures()
        increment_date()
def show_average():
    if len(temperatures) > 0:
        try:
            average = average_calculation()
        except ZeroDivisionError:
            average = 0
        show_date()
        print("La media de temperaturas es: ", average, "celsius")
    else:
        print("No hay temperaturas ingresadas")
def show_max_difference():
    if len(temperatures) > 1:
        max_difference = max_difference_calculation()
        print("Hasta ahora", end=" ")
        show_date()
        print("La maxima diferencia de temperaturas es: ", max_difference,"celcius")
    else:
        print("No temperatures recorded yet.")

def exit_execution():
    global end
    end = True

def read_temperatures():
    read= input("Escribe las temeperaturas de esta semana:\n")
    for temperature in reader.split():
        temperatures.append(float(temperature))

def increment_date():
    global month, day

    days_of_month = 31
    if month == 2:
        days_of_month = 28
    elif month in (4, 6, 9, 11):
        days_of_month = 30
    else:
        days_of_month = 31

    day += 7
    if day > days_of_month:
        day -= days_of_month 
        month += 1
        if month > 12:
            month = 1

def average_calculation():
    suma = 0

    for temperature in temperatures:
        suma += temperature
    return suma/len(temperatura)

def show_date():
    print(day, "of", end='')
    month_names = {1: "Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
    print(day, "of",month_names[month])

def max_difference_calculation():
    maxim: float = temperatures[0]
    minim: float = temperatures[0]

    for temperature in temperatures:
        if temperature > maxim:
            maxim = temperature
        if temperature < minim:
            minim = temperature
    return maxim - minim
