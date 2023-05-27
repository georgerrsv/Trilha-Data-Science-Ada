## Disciplina de Algoritmos

### Aula 8 - Funções

#### Introdução

- A função é utilizada para agrupar um conjunto de instruções que serão executadas quando a função for chamada.

- São criadas de forma isolada do resto do código, e podem ser chamadas várias vezes.

- A seguir será apresentado um exemplo de função:

    ```python
      def soma():
          x = int(input("Digite o primeiro número: "))
          y = int(input("Digite o segundo número: "))
          print(x + y)
        
        soma()
    ```

#### Parâmetros

- Os parâmetros são utilizados para passar valores para uma função.

- A seguir será apresentado um exemplo de função com parâmetros:

    ```python
      def soma(x, y):
          print(x + y)
        
        soma(1, 2)
    ```

#### Retorno

- O retorno é utilizado para retornar um valor para quem chamou a função.

- A seguir será apresentado um exemplo de função com retorno:

    ```python
      def soma(x, y):
          return x + y
        
        print(soma(1, 2))
    ```

- Uma das vantagens da função é que elas podem estar isoladas do fluxo principal do programa, ou seja, podem ser criadas em um arquivo separado e serem importadas para o arquivo principal.