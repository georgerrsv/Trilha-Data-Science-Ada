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