

#TODO Создание нескольких графиков на примере продуктов в магазине

import matplotlib.pyplot as plt
from random import randint
from dataclasses import dataclass

class Shope:
    """
    Магазин
    """
    shope = {}
    def __init__(self,*args):
        self.args = args
    
    def draw(self):
        a,picture = plt.subplots(len(self.args),2)
        
        count = 0
        for k in self.shope.keys():
            picture[count,0].plot(self.shope[k]["prize"], color="red")
            picture[count,1].plot(self.shope[k]["quantity"], color="green")
            count += 1

@dataclass
class Product:
    """
    Продукт
    """
    name : str
    prize: list
    quantity: list

    def __post_init__(self):
        Shope.shope[self.name] = {"prize":self.prize,"quantity":self.quantity}

s = Shope(Product("Мука",[randint(10,100) for i in range(10)],[randint(10,100) for i in range(10)]),
          Product("Сахар",[randint(10,100) for i in range(10)],[randint(10,100) for i in range(10)]),
          Product("Соль",[randint(10,100) for i in range(10)],[randint(10,100) for i in range(10)]),
          Product("Чай",[randint(10,100) for i in range(10)],[randint(10,100) for i in range(10)]))

s.draw()
plt.show()