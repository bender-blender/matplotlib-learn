

#TODO Добавляем легенду и рисуем геометрические фигуры на графиках


import matplotlib.pyplot as plt



plt.plot([1,2,3,4],":s",label="line 1")
plt.plot([1,5,1,3,2,6],"--r",label="line 2")
plt.grid(which="major",color="#444",linewidth=2)
plt.grid(which="minor",color="#aaa", linewidth=2)
plt.legend()
plt.show()



#TODO Узнаете как рисовать геометрические фигуры непосредственно на графике. Классы: Line2D, Rectangle, Arc, Arrow, Circle, CirclePolygon, Ellipse, FancyBboxPatch, PathPatch, Polygon, Wedge. 