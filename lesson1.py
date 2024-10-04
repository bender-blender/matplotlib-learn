
#Функция plot для построения и оформления двумерных графиков 
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2,3,4])

plt.plot(a,"--r") #TODO В график можно задавать цвет а также стиль линии 
#plt.show() #TODO функция, который сохраняет окно с графиком


x = np.linspace(0,10,100)
y = np.array(np.sin(x))

plt.plot(x,y,marker="+")
plt.fill_between(x,y) #TODO Заливка области
plt.show()
