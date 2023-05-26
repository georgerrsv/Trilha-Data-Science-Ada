import numpy as np
import matplotlib.pyplot as plt

# Aplicações de limites, Aula 7

# Exemplo

def f(x):

    return (x**2 - 1)/(2*x**2 - x - 1)

print(f(1)) #Impossível de calcular, pois o denominador é zero
print(f(-1/2)) #Impossível de calcular, pois o denominador é zero
# Para qualquer valor diferente de 1 e -1/2 
# é possível calcular os valores da função
print(f(1.0003)) #Possível de calcular, pois o denominador é diferente de zero
print(f(0.883)) #Possível de calcular, pois o denominador é diferente de zero
print(f(-0.999)) #Possível de calcular, pois o denominador é diferente de zero