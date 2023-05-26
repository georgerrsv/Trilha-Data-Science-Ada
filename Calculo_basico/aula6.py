import numpy as np
import matplotlib.pyplot as plt

# Gráficos das questões da Lista I

# Questão 3

fig = plt.figure(figsize=(8, 5))
plt.title('Questão 3')

x = np.linspace(-10, 10, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.show()