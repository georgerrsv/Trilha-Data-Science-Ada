#Gráficos utilizados na aula 4

import numpy as np
import matplotlib.pyplot as plt


#Função constante
fig = plt.figure(figsize=(8, 5))
plt.title('Função constante')

x = np.linspace(-10, 10, 1000)
y = 20*np.ones(x.shape)

plt.plot(x, y)
plt.show()


#Função linear
fig = plt.figure(figsize=(8, 5))
plt.title('Função linear')

x = np.linspace(-10, 10, 1000)
y = 5 + 2*x

plt.plot(x, y)
plt.show()


#Função quadrática
fig = plt.figure(figsize=(8, 5))
plt.title('Função quadrática')

x = np.linspace(-10, 10, 1000)
y = 5 + 5*x**2

plt.plot(x, y)
plt.show()

#Função polinomial
fig = plt.figure(figsize=(8, 5))
plt.title('Função polinomial')

x = np.linspace(-10, 10, 1000)
y = x**3 - 2*x**2 + 5*x - 10

plt.plot(x, y)
plt.show()

#Função racional
fig = plt.figure(figsize=(8, 5))
plt.title('Função racional')

x = np.linspace(-10, 10, 1000)
y = 1/(x**2 + 1)

plt.plot(x, y)
plt.show()

#Função trigonométrica
fig = plt.figure(figsize=(8, 5))
plt.title('Função trigonométrica, cosseno')

x = np.linspace(-10, 10, 1000)
y = np.cos(x)

plt.plot(x, y)
plt.show()

#Função exponencial
fig = plt.figure(figsize=(8, 5))
plt.title('Função exponencial')

x = np.linspace(-10, 10, 1000)
y = np.exp(x)

plt.plot(x, y)
plt.show()

#Função sigmoide
fig = plt.figure(figsize=(8, 5))
plt.title('Função sigmoide')

x = np.linspace(-10, 10, 1000)
y = 1/(1 + np.exp(-x))

plt.plot(x, y)
plt.show()