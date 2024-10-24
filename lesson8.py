
#TODO Как строить трехмерные графики

import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure(figsize=(7,4))
ax3d = fig.add_subplot(projection="3d") #! Задать трехмерную ось


x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.arange(-2*np.pi, 2*np.pi, 0.2)

xgrid, ygrid = np.meshgrid(x, y)

zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)
#ax3d.plot_wireframe(xgrid,ygrid,zgrid)
ax3d.plot_surface(xgrid,ygrid,zgrid)
plt.show()