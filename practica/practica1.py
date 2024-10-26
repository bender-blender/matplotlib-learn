

"""
#TODO 1. Графики функций

    *Постройте графики различных математических функций, например, синуса, косинуса, экспоненты и параболы.
    *Настройте график: добавьте заголовок, подпишите оси, добавьте сетку и легенду.
    *Измените цвет линий, тип линии (сплошная, пунктирная), добавьте маркеры.
"""


import matplotlib.pyplot as plt
import numpy as np

# Синус
x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(x)

plt.plot(x,y,"--r",label="Синус")


# Косинус
x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.cos(x)
plt.plot(x,y,">",label="Косинус")

# Экспонент
x1 = np.arange(-1,1,0.1)
y1 = np.e ** x1
plt.plot(x1,y1,".",label="Экспонент")



x2 = np.arange(-np.pi,np.pi,0.01)
y2 = np.square(x2)
plt.plot(x2,y2,label="Парабола")

plt.legend()
plt.grid()

plt.show()