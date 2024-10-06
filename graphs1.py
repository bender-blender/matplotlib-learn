

#TODO  Чтения файла и создания графика

import matplotlib.pyplot as plt
from file import File

class Graphs:

    """
    График
    """
    def __init__(self):
        self.file = File("file.txt") # файл
        self.name = self.file.name # имя файла
        self.file.number_generation(10) # генерация чисел
    
    def __get_data(self):
        """
        Получить данные 
        """
        with open(self.name,mode="r") as rf:
            data = rf.readlines()

            return data
    
    def draw(self):
        data = self.__get_data()
        lst = [int(i[0:-1]) for i in data]
        
        plt.grid(True)
        plt.plot(lst,"--",marker="+")



a = Graphs()
a.draw()
plt.show()