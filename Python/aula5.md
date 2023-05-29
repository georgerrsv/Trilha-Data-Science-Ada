## Disciplina de Python

### Aula 5 - Métodos e funções de listas

#### Introdução

- Métodos e funções de listas são usados para manipular listas.

- Em Python, métodos e funções de listas são representados por `lista.metodo()` e `funcao(lista)`.

#### Exemplos

##### 1. Append:

```python
lista = [1, 2, 3, 4, 5]
lista.append(6) # [1, 2, 3, 4, 5, 6]
```
Neste exemplo, a função `append()` adiciona um elemento ao final da lista.

##### 2. Insert:

```python
lista = [1, 2, 3, 4, 5]
lista.insert(0, 0) # [0, 1, 2, 3, 4, 5]
```
Neste exemplo, a função `insert()` adiciona um elemento em uma posição específica da lista.

##### 3. Remove:

```python
lista = [1, 2, 3, 4, 5]
lista.remove(5) # [1, 2, 3, 4]
```
Neste exemplo, a função `remove()` remove um elemento da lista.

##### 4. Pop:

```python
lista = [1, 2, 3, 4, 5]
lista.pop() # [1, 2, 3, 4]
```
Neste exemplo, a função `pop()` remove o último elemento da lista.

##### 5. Pop, passando um índice como parâmetro:

```python
lista = [1, 2, 3, 4, 5]
lista.pop(0) # [2, 3, 4, 5]
```
Neste exemplo, a função `pop()` remove um elemento específico da lista.

- A função `pop()` retorna o elemento removido. Então, podemos armazenar o elemento removido em uma variável. Enquanto a função `remove()` não retorna nada.

##### 6. Clear:

```python
lista = [1, 2, 3, 4, 5]
lista.clear() # []
```
Neste exemplo, a função `clear()` remove todos os elementos da lista.

##### 7. Reverse:

```python
lista = [1, 2, 3, 4, 5]
lista.reverse() # [5, 4, 3, 2, 1]
```
Neste exemplo, a função `reverse()` inverte a ordem dos elementos da lista.

##### 8. Sort:

```python
lista = [5, 4, 3, 2, 1]
lista.sort() # [1, 2, 3, 4, 5]
```
Neste exemplo, a função `sort()` ordena os elementos da lista. Por padrão, a função `sort()` ordena os elementos em ordem crescente. Para ordenar os elementos em ordem decrescente, podemos passar o parâmetro `reverse=True` para a função `sort()`.

##### 9. Count:

```python
lista = [1, 2, 3, 4, 5]
lista.count(1) # 1
```
Neste exemplo, a função `count()` conta quantas vezes um elemento passado por parâmetro aparece na lista.

##### 10. Index:

```python
lista = [1, 2, 3, 4, 5]
lista.index(1) # 0
```
Neste exemplo, a função `index()` retorna o índice de um elemento passado por parâmetro.

##### 11. Extend:

```python
lista = [1, 2, 3, 4, 5]
lista.extend([6, 7, 8, 9, 10]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
Neste exemplo, a função `extend()` adiciona uma lista ao final de outra lista.

##### 12. Copy:

```python
lista = [1, 2, 3, 4, 5]
lista2 = lista.copy() # [1, 2, 3, 4, 5]
```
Neste exemplo, a função `copy()` copia uma lista para outra lista.

##### 13. Copy com referência:

```python
lista = [1, 2, 3, 4, 5]
lista2 = lista # [1, 2, 3, 4, 5]
```
Neste exemplo, a lista `lista2` é uma referência para a lista `lista`. Então, se alterarmos a lista `lista2`, a lista `lista` também será alterada.

##### 14. Copy sem referência:

```python
lista = [1, 2, 3, 4, 5]
lista2 = lista[:] # [1, 2, 3, 4, 5]
```
Neste exemplo, a lista `lista2` é uma cópia da lista `lista`. Então, se alterarmos a lista `lista2`, a lista `lista` não será alterada.

##### 15. Lista fatiada:

```python
lista = [1, 2, 3, 4, 5]
lista2 = lista[1:3] # [2, 3]
```
Neste exemplo, a lista `lista2` é uma fatia da lista `lista`. Então, se alterarmos a lista `lista2`, a lista `lista` não será alterada.


#### Funções de lista

##### 1. Len:

```python
lista = [1, 2, 3, 4, 5]
len(lista) # 5
```

Neste exemplo, a função `len()` retorna o tamanho da lista.

##### 2. Max:

```python
lista = [1, 2, 3, 4, 5]
max(lista) # 5
```

Neste exemplo, a função `max()` retorna o maior elemento da lista.

##### 3. Min:

```python
lista = [1, 2, 3, 4, 5]
min(lista) # 1
```

Neste exemplo, a função `min()` retorna o menor elemento da lista.

##### 4. Sum:

```python
lista = [1, 2, 3, 4, 5]
sum(lista) # 15
```

Neste exemplo, a função `sum()` retorna a soma dos elementos da lista.

##### 5. Enumerate:

```python
lista = [1, 2, 3, 4, 5]
for indice, valor in enumerate(lista):
    print(indice, valor)
```

Neste exemplo, a função `enumerate()` retorna uma tupla com o índice e o valor de cada elemento da lista.