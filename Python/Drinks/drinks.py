import json
from collections import namedtuple

f = open ('/Users/gabrielcrowell/Documents/Dev/Learning/Python/Drinks/drinks.json', "r") 

def drinkDecoder(drinkDict):
    return namedtuple('X', drinkDict.keys())(*drinkDict.values())

data = json.loads(f.read()) 
#user = str(input())
print(type(data))
class Drinks:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def ingredients(self):
       print(f"The drink {self.name} is made with {self.ingredients}")


class Rum(Drinks):
    def ingredients(self):
        return super().ingredients()


class Whisky(Drinks):
    pass 

class Tequila(Drinks):
    pass 

