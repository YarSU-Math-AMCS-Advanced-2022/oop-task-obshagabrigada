from dataclasses import dataclass

@dataclass
class Product:
    def __init__(self, name = '', price = 0, ingridients=[], additional=[[]], energy=0,cook_time=0):
        self.price = price
        self.name = name
        self.ingredients = ingridients
        self.energy_value = energy
        self.cooking_time = cook_time
        self.additional = additional

    def printProduct(self):
        print('блюдо: '+str(self.name))
        print('цена: '+str(self.price))
        print('ингридиенты: '+str(self.ingredients))
        print('энерг. ценность: '+str(self.energy_value))
        print('время приготовления: '+str(self.cooking_time))
        print('доп. ингридиенты к блюду: '+str(self.additional))