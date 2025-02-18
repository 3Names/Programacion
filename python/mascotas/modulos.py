class gato:
    _name:str
    _age:int
    _raza:str
    
    def __init__(self, name:str, raza:str, age:int):
        self._name = name
        self._raza = raza
        self._age = age

    def set_name(self, name:str):
        self._name = name
    
    def set_age(self, age:int):
        self._age = age

    def get_name(self):
        return self._name

    def meow(self):
        print(f"{self._name} says: meow! meow!")

    def sleep(self, days:int):
        print(f"{self._name} is sleeping again")

    def eat(self, food_quantity:int):
        print(f"{self._name} is eating one more time")

    def washing(self):
        print(f"{self._name} is washing himself again")

    def __str__(self):
        name = self.get_name()
        return f"Name: {self._name}, Raza: {self._raza}, Edad: {self._age}"
if __name__ == "__main__":
    print("ejecutando")
