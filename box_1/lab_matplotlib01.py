# python_live_plot.py

import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dataset = []
i = 1
while i <= 100:
    dataset.append(i)
    i = i+1



plt.style.use('fivethirtyeight')

x_values = []
y_values = []
c_values = []


index = count()





def animate(i):



    x_values.append(next(index))
    y_values.append(random.choice(dataset))
    c_values.append(random.choice(dataset))

    if len(c_values) == 20:
        c = 1
        while c <= 70:
            dataset.remove(c)
            c = c + 1



        ii = 100
        while ii <= 300:
            dataset.append(ii)
            ii = ii + 12



    plt.cla()
    plt.plot(x_values, y_values,c_values)






ani = FuncAnimation(plt.gcf(), animate, 1000)


plt.tight_layout()
plt.show()

print(c_values)