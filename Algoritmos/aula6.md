## Disciplina de Algoritmos

### Aula 6 - Lista de exercícios I

#### Questão 1.

- Sabe-se que:

    - ESCREVA "a", "b" é o comando que imprime a mensagem a b na tela;
    - Uma cadeia de caracteres é delimitada por aspas duplas;
    - Variável é um espaço na memória do computador capaz de reter e apresentar um valor;
    - REAL x cria a variável x que armazena dados do tipo número real;
    - LEIA z é o comando que solicita uma informação ao usuário e a armazena na variável z;
    - * é o operador aritmético de multiplicação;

- Observe o programa abaixo e responda: o que o código mostra na tela ao ser executado (inclusive, o que foi digitado pelo usuário)?
    
        
        REAL a, b
        ESCREVA "Digite um número: "
        LEIA a
        ESCREVA "Digite outro número: "
        LEIA b
        ESCREVA "a * b = ", a * b
        
#### Questão 2.

- São dados os seguintes comandos:

    - INTEIRO x cria uma variável x que armazena dados do tipo número inteiro;
    - ENQUANTO repete um trecho de código até que sua condição torne-se falsa;
    - <- atribui um valor a uma variável;
    - + é o operador matemático de adição;
    - != é o operador lógico de diferente;

- Observe o código:

        
        CARACTER senha
        INTEIRO i

        ESCREVA "Para continuar, digite sua senha: "
        LEIA senha

        i <- 0

        ENQUANTO senha != "a6b5c4" FAÇA
            ESCREVA "Senha inválida"
            i <- i + 1
            ESCREVA "Para continuar, digite sua senha: "
            LEIA senha
        FIM_ENQUANTO

        ESCREVA "Seja bem-vindo(a) à área do cliente"
        
- Márcia, uma cliente, utiliza o programa acima para acessar a área do cliente e, após 7 tentativas de digitar a senha, visualiza a mensagem de boas vindas. Sabendo disso, qual é o valor armazenado em i ao final da execução do programa?

#### Questão 3.

- Sabendo que:

    - SE divide o fluxo do programa em dois, um representado por ENTAO, que roda se a condição for verdadeira, e outro representado por SENAO, que roda se a condição for falsa;
    - / é o operador aritmético de divisão;
    - ->  é o operador lógico de maior que;

- Observe o código:

        
        INTEIRO x1, x2
        REAL res
        ESCREVA "digite um número positivo"
        LEIA x1
        ESCREVA "digite outro número positivo"
        LEIA x2

        SE (x1 > x2) ENTAO
            res <- (x1 - x2) / x1
        SENAO FAÇA
            res <- (x2 - x1) / x2
        FIM_SE

        ESCREVA res
        
- Qual alternativa representa corretamente a última linha impressa pelo programa para os seguintes pares de valores [n1, n2], respectivamente: [3, 12], [5, 5], [10, 8]?

#### Questão 4.

- Sabendo que < é o operador relacional menor que, analise o código abaixo:
    
        
        INTEIRO x, i, t, e
        REAL a

        ESCREVA "Digite um número: "
        LEIA x
    
        i <- 0
        t <- 0

        ENQUANTO i < x FAÇA
            ESCREVA "Digite um número: "
            LEIA e
            t <- t + e
            i <- i + 1
        FIM_ENQUANTO
        a <- t / x
        ESCREVA i, a
        
- Ao executar o programa acima, qual será a última linha impressa na tela se os valores digitados pelo usuário forem, nessa ordem: 5, 3, 4, 5, 4, 5?

#### Questão 5.

- PARA é um comando que repete um bloco de código um determinado número de vezes e que possui uma variávei(i) que conta o número de iterações realizadas. Sabendo que v(n) e u(n) são vetores de tamanho n, que armazenam números reais, escolha a alternativa que contém a saída do programa abaixo.

        
        INTEIRO i, n
        REAL v(5), u(5)

        v(1) <- 2.0
        v(2) <- 3.0
        v(3) <- 4.0
        v(4) <- 5.0
        v(5) <- 6.0

        n <- 5

        PARA i DE 1 ATÉ n FAÇA
            u(i) <- v(i) * i
        FIM_PARA
        ESCREVA u(2), u(4)
        