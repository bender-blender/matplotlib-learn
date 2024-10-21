
#TODO Размещаем стандартные текстовые элементы на графике
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(7,4))
fig.set(facecolor="#eee")
ax = fig.add_subplot()
ax.set(facecolor="#AAFFAA")

plt.figtext(0.05,0.6,"Текст в области окна")
fig.suptitle("Заголовок окна")

plt.xlabel("Ox")
plt.ylabel("Oy")

ax.text(0.05,0.1,"Произвольный текст в координатных осях")

plt.plot([1,2,3,4,5])
plt.show()
