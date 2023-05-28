## Disciplina de Python

### Aula 4 - Estruturas de listas

#### Introdução

- Listas são usadas para armazenar vários valores em uma única variável.

- Em Python, listas são representadas por colchetes `[]`.

- Exemplo:

```python
lista = [1, 2, 3, 4, 5]
```

- Listas podem armazenar valores de tipos diferentes.

- Exemplo:

```python
lista = [1, 'dois', 3.0, True]
```

- Listas podem ser acessadas por índices.

- Exemplo:

```python
lista = [1, 2, 3, 4, 5]
print(lista[0]) # 1
print(lista[1]) # 2
print(lista[2]) # 3
print(lista[3]) # 4
print(lista[4]) # 5
```

- Listas podem ser acessadas por índices negativos.

- Exemplo:

```python
lista = [1, 2, 3, 4, 5]
print(lista[-1]) # 5
print(lista[-2]) # 4
print(lista[-3]) # 3
print(lista[-4]) # 2
print(lista[-5]) # 1
```

- Listas podem ser acessadas por intervalos.

- Exemplo:

```python
lista = [1, 2, 3, 4, 5]
print(lista[0:2]) # [1, 2]
print(lista[1:3]) # [2, 3]
print(lista[2:4]) # [3, 4]
print(lista[3:5]) # [4, 5]
```

- Listas podem ser acessadas por intervalos negativos.

- Exemplo:

```python
lista = [1, 2, 3, 4, 5]
print(lista[-2:-1]) # [4]
print(lista[-3:-1]) # [3, 4]
print(lista[-4:-1]) # [2, 3, 4]
print(lista[-5:-1]) # [1, 2, 3, 4]
```

- Listas podem ser acessadas por intervalos com passo.

- Exemplo:

```python
lista = [1, 2, 3, 4, 5]
print(lista[0:5:2]) # [1, 3, 5]
print(lista[1:5:2]) # [2, 4]
print(lista[0:5:3]) # [1, 4]
print(lista[1:5:3]) # [2, 5]
```

#### Operações com listas

- Listas podem ser concatenadas com o operador `+`.

- Exemplo:

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3) # [1, 2, 3, 4, 5, 6]
```

- Listas podem ser repetidas com o operador `*`.

- Exemplo:

```python
lista = [1, 2, 3]
lista = lista * 3
print(lista) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

- Listas podem ser percorridas com o comando `for`.

- Exemplo:

```python
lista = [1, 2, 3]
for item in lista:
    print(item)
```

- Listas podem ser percorridas com o comando `for` e índices.

- Exemplo:

```python
lista = [1, 2, 3]
for indice in range(len(lista)):
    print(lista[indice])
```