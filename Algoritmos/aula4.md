## Disciplina de Algoritmos

### Aula 4 - Decisão

#### Introdução

- A decisão é utilizada para definir qual ação será executada de acordo com uma condição, ou seja, se uma condição for verdadeira, uma ação será executada, caso contrário, outra ação será executada.

- A seguir será apresentado um exemplo de decisão:

    - Se o aluno for aprovado, o aluno será aprovado, caso contrário, o aluno será reprovado.

- A seguir será apresentado um exemplo de decisão em um algoritmo:

    - Se o aluno obtiver nota >= 6, o aluno será aprovado, caso contrário, o aluno será reprovado.

    - Exemplo de algoritmo:

        ```python
        def aprovado():
            nota = int(input("Digite a nota do aluno: "))

            if(nota >= 6):
                print("Aluno aprovado")
             else 
                printf("Aluno reprovado")
        ```
#### Operadores lógicos

- Os operadores lógicos são utilizados para definir condições, ou seja, são utilizados para definir se uma condição é verdadeira ou falsa.

- Exemplos de operadores lógicos:

    - `==` - Igual
    - `!=` - Diferente
    - `>` - Maior
    - `<` - Menor
    - `>=` - Maior ou igual
    - `<=` - Menor ou igual

- Exemplos de operadores lógicos em um algoritmo:

- Exemplo 1:

    ```python
    def compara():
        x = int(input())
        y = int(input())

        if(x >= y):
            print("x é maior ou igual a y")
        elif(x <= y):
            printf("x é menor ou igual a y")
        elif(x == y):
            printf("x é igual a y")
        elif(x != y):
            printf("x é diferente de y")
        elif(x > y):
            printf("x é maior que y")
        elif(x < y):
            printf("x é menor que y")
    ```
- Exemplo 2:

    ```python
    def compare_nomes():
        nome1 = (input())
        nome2 = input()

        if(nome1 == nome2):
            print("Os nomes são iguais")
        else:
            print("Os nomes são diferentes")
    ```
- Exemplo 3:

    ```python
    def horas():
        hora = int(input())

        if(hora >= 0 and hora <= 12):
            print("Bom dia")
        elif(hora > 12 and hora <= 18):
            print("Boa tarde")
        else:
            print("Boa noite")
    ```