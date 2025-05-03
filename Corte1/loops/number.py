import random
import matplotlib.pyplot as plt

numeros_x = range(1, 13)

numeros_y = [random.randint(1, 1000) for _ in range(12)]

plt.plot(numeros_x, numeros_y)
plt.show()
