import json
from collections import namedtuple


""" Program that passes the Drinks class to parse drinks.json and returns
the ingredients needed to make a certain drink based on what kind of liquor
"""
f = open ('/Users/gabrielcrowell/Documents/Dev/Learning/Python/Drinks/drinks.json', "r") 

def drinkDecoder(drinkDict):
    return namedtuple('X', drinkDict.keys())(*drinkDict.values())

data = json.loads(f.read()) 
#user = str(input())
print(type(data))

# TODO: add prompt for users to see name of drinks
class Drinks:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def ingredients(self):
       print(f"The drink {self.name} is made with {self.ingredients}")

# TODO: add more drinks into json file and display in a cleaner way
class Rum(Drinks):
    def ingredients(self):
        return super().ingredients()


class Whisky(Drinks):
    pass 

class Tequila(Drinks):
    pass 

