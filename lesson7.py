
#TODO Показ изображений и цветовых сеток

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


img = Image.open("tank.png")
#plt.imshow(img)


a = np.random.randint(0,255,(100,100))
#plt.imshow(a)


plt.pcolormesh(a)
plt.show()
# print(a)