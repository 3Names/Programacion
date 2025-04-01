class Item:
    ide:int
    nom:str
    tipus:str
    valor:float
    pes:float
    
    def __init__(self,ide,nom,tipus,valor,pes):
        self.ide = ide
        self.nom = nom
        self.tipus = tipus
        self.valor = valor
        self.pes = pes

class Inventory:
    items:list = [Item]

    def addItem():        
        print(3)

    def delItem(id):     
        print("xe")

    def searchItemByName(nom):
        print(1)

    def searchItemByType(tipus):
        print(2)

    def listItems():
        print(3)

x = Item(1,"buenas","arma",20.0,10.0)
print(x.ide)
