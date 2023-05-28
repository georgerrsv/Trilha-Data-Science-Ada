## Disciplina de Python

### Aula 6 - Dicionários

#### Introdução

- Dicionários são estruturas de dados que armazenam pares de chave-valor. A chave é um identificador único e o valor é o dado associado a essa chave. Dicionários são mutáveis, ou seja, podem ser alterados após sua criação.

- Dicionários são representados por chaves {} e os pares de chave-valor são separados por vírgula. A chave e o valor são separados por dois pontos.

- Dicionários são estruturas de dados não ordenadas, ou seja, não é possível acessar seus elementos através de índices.

- Dicionários podem ser criados de duas formas:

    - Através de chaves e valores separados por dois pontos:

        ```python
        dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
        ```

    - Através da função dict():

        ```python
        dicionario = dict(chave1='valor1', chave2='valor2')
        ```

- Para acessar um valor de um dicionário, basta informar a chave entre colchetes:

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    print(dicionario['chave1'])
    ```

- Para alterar o valor de uma chave, basta informar a chave entre colchetes e atribuir um novo valor:

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    dicionario['chave1'] = 'novo valor'
    print(dicionario['chave1'])
    ```

- Para adicionar um novo par chave-valor, basta informar a chave entre colchetes e atribuir um valor:

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    dicionario['chave3'] = 'valor3'
    print(dicionario['chave3'])
    ```

- Para remover um par chave-valor, basta utilizar a função del() e informar a chave:

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    del(dicionario['chave1'])
    print(dicionario)
    ```

- Para verificar se uma chave existe em um dicionário, basta utilizar o operador in:

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    if 'chave1' in dicionario:
        print('A chave existe')
    else:
        print('A chave não existe')
    ```

- Para verificar se um valor existe em um dicionário, basta utilizar o operador in e a função values():

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    if 'valor1' in dicionario.values():
        print('O valor existe')
    else:
        print('O valor não existe')
    ```

- Para verificar se um par chave-valor existe em um dicionário, basta utilizar o operador in e a função items():

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    if ('chave1', 'valor1') in dicionario.items():
        print('O par chave-valor existe')
    else:
        print('O par chave-valor não existe')
    ```

- Para percorrer um dicionário, podemos utilizar o laço for:

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    for chave in dicionario:
        print(chave)
    ```
    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    for chave, valor in dicionario.items():
        print(chave, valor)
    ```
    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    for valor in dicionario.values():
        print(valor)
    ```

- Para remover todos os pares chave-valor de um dicionário, basta utilizar a função clear():

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    dicionario.clear()
    print(dicionario)
    ```

- Para remover um par chave-valor de um dicionário e retornar o valor, basta utilizar a função pop() e informar a chave:

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    valor = dicionario.pop('chave1')
    print(valor)
    ```

- Para remover um par chave-valor de um dicionário e retornar o par chave-valor, basta utilizar a função popitem():

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    chave, valor = dicionario.popitem()
    print(chave, valor)
    ```

- Para obter o tamanho de um dicionário, basta utilizar a função len():

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    print(len(dicionario))
    ```

- Para obter uma lista com as chaves de um dicionário, basta utilizar a função keys():

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    print(dicionario.keys())
    ```

- Para copiar um dicionário, basta utilizar a função copy():

    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    dicionario2 = dicionario.copy()
    print(dicionario2)
    ```
    ```python
    dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
    dicionario2 = dict(dicionario)
    print(dicionario2)
    ```