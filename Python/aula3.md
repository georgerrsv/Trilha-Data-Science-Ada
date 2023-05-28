## Disciplina de Python

### Aula 3 - Estruturas de repetição

#### Introdução

- Estruturas de repetição são usadas para repetir um bloco de código várias vezes.

- Em Python, existem dois tipos de estruturas de repetição: `for` e `while`.

#### Estrutura de repetição `for`

- A estrutura de repetição `for` é usada para executar um bloco de código várias vezes.

- A sintaxe da estrutura de repetição `for` é a seguinte:

```python
for variavel in iteravel:
    # bloco de codigo
```

- O bloco de código é executado para cada elemento do iterável.

- Exemplo:

```python
for i in range(10):
    print(i)
```

- No exemplo, a variável `i` recebe cada elemento do iterável `range(10)`.

- O bloco de código pode ser executado para cada elemento do iterável usando a palavra-chave `else`.

- Exemplo:

```python
for i in range(10):
    print(i)
else:
    print('Fim do loop')
```

- No exemplo, o bloco de código é executado para cada elemento do iterável `range(10)` e, após o término do loop, o bloco de código dentro do `else` é executado encerrando o loop.

- O bloco de código pode ser interrompido usando a palavra-chave `break`.

- Exemplo:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

- No exemplo, o bloco de código é executado para cada elemento do iterável `range(10)` e, quando a variável `i` recebe o valor `5`, o loop é interrompido.

- O bloco de código pode ser interrompido usando a palavra-chave `continue`.

- Exemplo:

```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```

- No exemplo, o bloco de código é executado para cada elemento do iterável `range(10)` e, quando a variável `i` recebe o valor `5`, o loop é interrompido e o próximo elemento do iterável é processado.

#### Estrutura de repetição `while`

- A estrutura de repetição `while` é usada para executar um bloco de código várias vezes.

- A sintaxe da estrutura de repetição `while` é a seguinte:

```python
while condicao:
    # bloco de codigo
```

- O bloco de código é executado enquanto a condição for verdadeira.

- Exemplo:

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

- No exemplo, o bloco de código é executado enquanto a variável `i` for menor que `10`.

- O bloco de código pode ser executado enquanto a condição for verdadeira usando a palavra-chave `else`.

- Exemplo:

```python
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('Fim do loop')
```

- No exemplo, o bloco de código é executado enquanto a variável `i` for menor que `10` e, após o término do loop, o bloco de código dentro do `else` é executado encerrando o loop.

- O bloco de código pode ser interrompido usando a palavra-chave `break`.

- Exemplo:

```python
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
```

- No exemplo, o bloco de código é executado enquanto a variável `i` for menor que `10` e, quando a variável `i` recebe o valor `5`, o loop é interrompido.