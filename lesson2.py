

#TODO Отображение нескольких координатных осей в одном окне

import matplotlib.pyplot as plt


#TODO subplot - создает новую ось

plt.subplot(1,2,1)
plt.plot([1,2,3,4,5])
plt.subplot(1,2,2)
plt.plot([1,2,3,4,5])

plt.subplot(2,3,1)
plt.plot([1,2,3,4,5])

#TODO sublots - создает несколько осей

f, p = plt.subplots(2,2)
p[0,0].plot([1,2,3,4])
p[0,1].plot([-1,-2,0,3]) #TODO заполнить определенную ось


#TODO  Способ создания дополнительного окна с помощью функции figure()

a = plt.figure(figsize=(4,7)) #TODO указать размер в дюймах

plt.show()



