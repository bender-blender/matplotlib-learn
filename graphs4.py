

#TODO Добавляем легенду на примере конструктора графиков
import matplotlib.pyplot as plt

from random import randint

def customize_the_window(title,x,y):
    """
    Кастомизация окна 
    """
    
    plt.suptitle(title)
    plt.xlabel(x)
    plt.ylabel(y)

window = customize_the_window("Производство угля","год","тонн")

class Graphs:
    """
    График
    """

    def __init__(self, name:str,linestyle:str,style:str,color:str,*coord:list):

        for i in coord:
            plt.plot(i,linestyle=linestyle, marker=style, color=color,
         markerfacecolor='black',label=name)
            
        plt.legend()

plt.grid(True)
n = 10
russia = Graphs("Россия","-.","v","r",[randint(500,100000) for i in range(n)])
ukraine = Graphs("Украина","--","o","y",[randint(500,100000) for i in range(n)])
usa = Graphs("США",":","s","g",[randint(500,100000) for i in range(n)])
italy = Graphs("Италия","-","s","b",[randint(500,100000) for i in range(n)])
plt.show()