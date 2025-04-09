import os

class Producte:
    nom:str
    preu:float

    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

class Client:
    id_client:int
    nom:str
    email:str

    def __init__(self, id_client, nom, email):
        self.id_client = id_client
        self.nom = nom
        self.email = email

class Comanda:
    id_comanda:int
    client:Client
    productes:list[Producte]
    quantitats:list[int]

    def __init__(self, id_comanda, cliente, productes, quantitats):
        self.id_comanda = id_comanda
        self.cliente = cliente
        self.productes = productes
        self.quantitats = quantitats
    
    def calcular_total():
        precio:int = 0 
        for producte in productes:
            precio = precio + (producte.preu * quantitats[i])
        print(precio)

def processar_comandes():
    processed_products:dict = {}
    processed_clients:dict = {}
    processed_commands:dict = {}
    indexpro:int = 0
    
    try:
        with open("productes.txt") as xd:
            for line in xd.readlines():
                print(line)
    except Exception as e:
        print(e)

    try:
        with open("clients.txt","r") as fd:
            for line in fd.readlines():
                print(line)
    except Exception as e:
        print("Problema leyendo los clientes")
    
    try:
        with open("commandes.txt") as dx:
            for line in dx.readlines():
                print(line)
    except Exception as e:
        print(e)
    try:
        with open("productes.txt") as xd:
            for k , v in xd.readlines()[1].split(",")[0]:
                processed_products[k] = v
                print(processed_products)
            print(xd.readlines()[2].split(",")[0])
            print(range(len(xd.readlines())-1))
    except Exception as xd:
        print(xd)
