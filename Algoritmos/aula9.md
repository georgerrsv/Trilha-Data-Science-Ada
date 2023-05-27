## Disciplina de Algoritmos

### Aula 9 - Pseudocódigo

#### Introdução

- Pseudocódigo é uma forma genérica de escrever um algoritmo, utilizando uma linguagem simples (nativa ou não) para descrever o fluxo de um algoritmo.

- O pseudocódigo é uma forma de representar um algoritmo de forma mais próxima da linguagem humana, facilitando a compreensão do algoritmo.

##### Exemplo de pseudocódigo

    INICIO principal
        VAR opc_escolhida: STRING
        VAR valor: INTEIRO
        VAR saldo: INTEIRO
        VAR encerrar_programa: BOOLEANO

        DEFINIR encerrar_programa IGUAL_A Falso

        ENQUANTO encerrar_programa IGUAL_A Falso
            CHAMAR MOSTRAR_MENU -> opc_escolhida
            SE opc_escolhida IGUAL_A "a"
                MOSTRAR "Seu saldo é: ", saldo
            OU SE opc_escolhida IGUAL_A "b"
                MOSTRAR "Digite o valor a ser depositado: "
                ESPERAR_DIGITACAO -> valor
                SOMAR valor, saldo -> saldo
                MOSTRAR "Depósito realizado com sucesso!"
            OU SE opc_escolhida IGUAL_A "c"
                MOSTRAR "Digite o valor a ser sacado: "
                ESPERAR_DIGITACAO -> valor
                SE valor MAIOR_QUE saldo
                    MOSTRAR "Saque não permitido, saldo insuficiente!"
                SENAO
                    SUBTRAIR valor, saldo -> saldo
                    MOSTRAR "Saque realizado com sucesso!"
            OU SE opc_escolhida IGUAL_A "d"
                DEFINIR encerrar_programa IGUAL_A Verdadeiro
            SENAO
                MOSTRAR "Opção inválida!"
            FIM SE
        FIM ENQUANTO
    FIM

    INICIO mostrar_menu
        VAR opc_escolhida: STRING
        
        MOSTRAR "Menu:"
        MOSTRAR "[a] Consultar saldo"
        MOSTRAR "[b] Depositar"
        MOSTRAR "[c] Sacar"
        MOSTRAR "[d] Encerrar programa"
        MOSTRAR "Digite a opção desejada: "
        ESPERAR_DIGITACAO -> opc_escolhida
        RETORNAR opc_escolhida
    FIM mostrar_menu