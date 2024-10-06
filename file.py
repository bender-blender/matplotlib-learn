
#TODO Файл

from random import randint
class File:

    """
    Файл
    """
    def __init__(self,name):
        self.name = name
    
    def number_generation(self,n:int):
        """
        Генерировать числа в файле
        Args:
            n (int): количество чисел в файле
        """
        with open(self.name,"a") as wf:
            for i in range(n):
                wf.write(f"{randint(-10,10)}")
                wf.write("\n")
