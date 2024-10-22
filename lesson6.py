

#TODO Рисуем гистограммы, столбчатые и круговые диаграммы

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0,2,500)

#plt.hist(x,50)

x = [f"H{i + 1}" for i in range(10)]
y = np.random.randint(1,5,len(x))
#plt.bar(x,y)

#plt.barh(x,y)

country = ["Украина","Россия","США","Китай","Япония","Грузия"]
mark = [10,100,98,90,87,12]
plt.pie(mark,labels=country,autopct="%.2f",shadow=True)

plt.show()