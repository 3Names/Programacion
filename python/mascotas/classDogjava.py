class Dogo:
    name:str

    def __init__(self, name:str):
        self.name = name

    def bark(self):
        return "woof"

x = Dogo("xd")
print(x.bark())
