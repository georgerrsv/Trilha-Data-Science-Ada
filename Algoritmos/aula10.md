## Disciplina de Algoritmos

### Aula 10 - Lista de Exercícios II

#### Questão 1.

- Uma equipe de desenvolvedores está testando um algoritmo que realiza cálculos. O fluxograma a seguir mostra como é seu funcionamento:

        INICIO main
            VAR t -> 1
            VAR m -> 5
            VAR c -> 10
            FAÇA c -> c * (t + 1)
            ENQUANTO t < m
                FAÇA t -> t + 1
            FIM ENQUANTO
            MOSTRAR c
        FIM

- Qual será o valor mostrado na tela ao final da execução do algoritmo?

#### Questão 2.

- O Código de um programa para cadastro de alunos realiza a seguinte validação das variáveis Nome e CPF:

        - SE(Nome não é vazio E CPF não é vazio) CONTINUE

- Essa validação avalia um dos percursos possíveis, no qual os dados foram preenchidos corretamente e com isso faz com que o sistema continue. Se a validação fosse programada para avaliar o preenchimento incorreto dos dados, qual das seguintes expressões seria utilizada?

a) SE(Nome não é vazio OU CPF é vazio) PARE

b) SE(Nome não é vazio OU CPF não é vazio) PARE

c) SE(Nome é vazio OU CPF não é vazio) PARE

d) SE(Nome é vazio OU CPF é vazio) PARE

e) SE(Nome é vazio E CPF é vazio) PARE

#### Questão 3.

- Sabe-se que:
    - ESCREVA é o comando que escreve uma informação na tela;
    - <- atribui um valor a uma variável;
    - Variável é um espaço na memória capaz de reter e apresentar um valor;

- Observe o código a seguir:

    INICIO
        A <- 30
        B <- 20
        C <- A + B
        ESCREVA C
        B <- 10
        ESCREVA B, C
        C <- A + B
        ESCREVA A, B, C
    FIM

- Qual será o resultado apresentado na tela?

#### Questão 4.

- Sabe-se que: 
    - REAL x cria a variável x que armazena dados do tipo número real;
    - SE divide o fluxo do programa em dois, um representado por ENTAO, que roda se a condição for satisfeita, e outro representado por SENAO, que roda se a condição não for satisfeita;
    - - é o operador de subtração;
    - == e > são operadores relacionais igual a e maior que, respectivamente;

- Observe o código a seguir:

        INICIO
            ESCREVA "--- Moisés, bem-vindo ao App da poupança ---"

            INTEIRO i
            REAL valor, saldo, poupanca

            saldo <- 1000.00
            poupanca <- 500.00
            i <- 0

            ENQUANTO i != 3 FAÇA
                ESCREVA "Digite 1 para APLICAR, 2 para RESGATAR ou 3 para SAIR: "
                LEIA i
                SE i == 1 ENTAO
                    ESCREVA "Digite o valor a ser aplicado: "
                    LEIA valor
                    SE valor > saldo ENTAO FAÇA
                        ESCREVA "Saldo insuficiente"
                    SENAO FAÇA
                        saldo <- saldo - valor
                        poupanca <- poupanca + valor
                        ESCREVA "Aplicação realizada com sucesso"
                    FIM SE
                    SENAO FAÇA
                        SE i == 2 ENTAO
                            ESCREVA "Digite o valor a ser resgatado: "
                            LEIA valor
                            SE valor > poupanca ENTAO FAÇA
                                ESCREVA "Saldo insuficiente"
                    SENAO FAÇA
                        saldo <- saldo + valor
                        poupanca <- poupanca - valor
                        ESCREVA "Resgate realizado com sucesso"
                    FIM SE
                    SENAO FAÇA
                        ESCREVA "Até logo!"
                    FIM SE
                FIM SE
            FIM ENQUANTO
        FIM

- Utilizando o programa acima, Moisés realizou um resgate seguido de uma aplicação. Seguem Mensagens mostradas na tela ao final da execução do programa, inclusive dos valores informados por Moisés.

    Digite 1 para APLICAR, 2 para RESGATAR ou 3 para SAIR: 2
    Digite o valor a ser resgatado: x
    Resgate realizado com sucesso
    Digite 1 para APLICAR, 2 para RESGATAR ou 3 para SAIR: 1
    Digite o valor a ser aplicado: y
    Saldo insuficiente
    Digite 1 para APLICAR, 2 para RESGATAR ou 3 para SAIR: 3
    Até logo!

- Considerando que Moisés informou valores válidos para x e y, quais são os valores de x e y?

#### Questão 5.

- Sabe-se que:
    - ESCREVA "a", "b" escreve na tela as letras a e b;
    - Variável é um espaço na memória capaz de reter e apresentar um valor;
    - CARACTER x cria a variável x que armazena dados do tipo caractere;
    - LEIA z é o comando que solicita uma informação ao usuário e armazena na variável z;
    - + é o operador de adição que concatena duas variáveis do tipo caractere;

- Observe o código a seguir:

    INICIO
        CARACTER nome, dia, mes
        ESCREVA "Bem-vindo(a) ao App do sistema"

        ESCREVA "Digite seu nome: "
        LEIA nome

        ESCREVA "Digite o dia do seu aniversário: "
        LEIA dia

        ESCREVA "Digite o mês do seu aniversário: "
        LEIA mes

        ESCREVA "Login:", dia + nome + mes
    FIM

- Qual será a última linha impressa pelo programa se o usuário digitar, nessa ordem, Luiza, 9 e 10?