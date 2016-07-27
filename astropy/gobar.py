# http://stackoverflow.com/questions/37927270/python3-using-matplotlib-to-create-figure-using-a-dictionary

import matplotlib.pyplot as plt
import operator

fig, ax = plt.subplots()

d = {0.1: (0.94736842105263153, 0.90294117647058825), 0.2: (0.92105263157894735, 0.90397350993377479), 0.3: (0.82456140350877194, 0.9242424242424242), 0.6: (0.8722466960352423, 0.91390728476821192), 0.8: (0.76897689768976896, 0.98666666666666669), 0.5: (0.79894179894179895, 0.95767195767195767), 0.7: (0.8226415094339623, 0.99115044247787609), 0.9: (0.62463343108504399, 1.0), 0.4: (0.79605263157894735, 0.92920353982300885)}

lists = sorted(d.items())

x = list(map(operator.itemgetter(0), lists))
y = list(map(operator.itemgetter(1), lists))

y1 = list(map(operator.itemgetter(0), y))
ax.plot(x, y1, label='Test error', color='b', linewidth=2)

y2 = list(map(operator.itemgetter(1), y))
ax.plot(x, y2, label='Training error', color='r', linewidth=2)

plt.legend(loc='best')
plt.grid()
plt.show()
