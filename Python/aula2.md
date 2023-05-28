## Disciplina de Python

### Aula 2 - Estruturas condicionais

#### Introdução

- Estruturas condicionais são usadas para controlar o fluxo de execução de um programa.

- Em Python, existem dois tipos de estruturas condicionais: `if` e `switch`.

#### Estrutura condicional `if`

- A estrutura condicional `if` é usada para executar um bloco de código caso uma condição seja verdadeira.

- A sintaxe da estrutura condicional `if` é a seguinte:

```python
if condicao:
    # bloco de codigo
```

- O bloco de código é executado caso a condição seja verdadeira.

- Exemplo:

```python
if 1 == 1:
    print('1 é igual a 1')
```

- O bloco de código não é executado caso a condição seja falsa.

- Exemplo:

```python
if 1 == 2:
    print('1 é igual a 2')
```

- O bloco de código pode ser executado caso a condição seja falsa usando a palavra-chave `else`.

- Exemplo:

```python
if 1 == 2:
    print('1 é igual a 2')
else:
    print('1 é diferente de 2')
```

- O bloco de código pode ser executado caso a condição seja falsa usando a palavra-chave `elif`.

- Exemplo:

```python
if 1 == 2:
    print('1 é igual a 2')
elif 1 == 3:
    print('1 é igual a 3')
else:
    print('1 é diferente de 2 e 3')
```

#### Estrutura condicional `switch`

- A estrutura condicional `switch` é usada para executar um bloco de código caso uma condição seja verdadeira.

- A sintaxe da estrutura condicional `switch` é a seguinte:

```python
switch condicao:
    case valor1:
        # bloco de codigo
    case valor2:
        # bloco de codigo
    default:
        # bloco de codigo
```

- O bloco de código é executado caso a condição seja verdadeira.

- Exemplo:

```python
switch 1:
    case 1:
        print('1 é igual a 1')
    case 2:
        print('1 é igual a 2')
    default:
        print('1 é diferente de 1 e 2')
```

- O bloco de código não é executado caso a condição seja falsa.

- Exemplo:

```python
switch 1:
    case 2:
        print('1 é igual a 2')
    default:
        print('1 é diferente de 2')
```