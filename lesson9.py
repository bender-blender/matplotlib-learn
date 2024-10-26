

#TODO Создаем анимацию графиков

from matplotlib.animation import FuncAnimation, ArtistAnimation
import matplotlib.pyplot as plt
import numpy as np

def update_cos(frame,line,x):
    """
    frame - параметр , который меняется от кадра к кадру
    В данном случае - это начальная фаза(угол)
    line - ссылка на объект Line2D
    """
    line.set_ydata(np.cos(x + frame))
    return [line]



fig,ax = plt.subplots()
x = np.arange(-2*np.pi, 2*np.pi,0.1)
y = np.cos(x)

line, = plt.plot(x,y)

phasa = np.arange(0, 4*np.pi, 0.1)
animation = FuncAnimation(
    fig, # Фигура, где отображается анимация
    func=update_cos, # Функция обновления текущего кадра
    frames=phasa, # Параметр, меняющейся от кадра к кадру
    fargs=(line,x), # дополнительные параметры для func
    interval=30, # задержка между кадрами 
    blit=True, # использовать ли двойную буферизацию
    repeat=False # зацикливать ли анимацию 
)

plt.show()