
#TODO Рисуем ступенчатые, стековые, stem и точечные графики

import matplotlib.pyplot as plt
import numpy as np



a = np.arange(0,10)
b = a
#plt.step(a,b)



#plt.stem(a,b)


x = np.arange(-2,2,0.1)
y1 = np.array([-y**2 for y in x]) +8
y2 =  np.array([-y**2 for y in x])+8
y3 =  np.array([-y**2 for y in x])+8
#plt.stackplot(x,y1,y2,y3)



x = np.random.normal(0,2,500)
y = np.random.normal(0,2,500)

plt.scatter(x,y)
plt.show()

