## Exemplo de código para aula 9, caixa eletrônico

class caixa_eletronico():

    def __init__(self, nome, acc_numero, saldo = 0):
        self.nome = nome
        self.acc_numero = acc_numero
        self.saldo = saldo
    
    def deposito(self, deposito):
        self.deposito = deposito
        self.saldo += deposito
        print(f"Deposito de R${self.deposito} realizado com sucesso!")
        print(f"Seu saldo atual é de R${self.saldo}")
    
    def saque(self, saque):
        self.saque = saque
        if self.saque > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= self.saque
            print(f"Saque de R${self.saque} realizado com sucesso!")
            print(f"Seu saldo atual é de R${self.saldo}")

    def extrato(self):
        print(f"Nome do cliente: {self.nome}")
        print(f"Numero da conta: {self.acc_numero}")
        print(f"Saldo: R${self.saldo}")
    
    def transacao(self):
        print("Bem vindo(a) ao caixa eletronico!")
        print("Menu: ")
        print("1 - Saldo")
        print("2 - Saque")
        print("3 - Deposito")
        print("4 - Extrato")
        print("5 - Sair")

        while True:
            try:
                opc = int(input("Digite a opção desejada: "))
            except:
                print("Opção invalida!")
                continue
            else:
                if opc == 1:
                    caixa_eletronico.extrato(self)
                elif opc == 2:
                    while True:
                        try:
                            saque = float(input("Digite o valor do saque: "))
                        except:
                            print("Valor invalido!")
                            continue
                        else:
                            caixa_eletronico.saque(self, saque)
                            break
                elif opc == 3:
                    while True:
                        try:
                            deposito = float(input("Digite o valor do deposito: "))
                        except:
                            print("Valor invalido!")
                            continue
                        else:
                            caixa_eletronico.deposito(self, deposito)
                            break
                elif opc == 4:
                    print("Extrato: ")
                    caixa_eletronico.extrato(self)
                elif opc == 5:
                    print("Obrigado por utilizar nosso caixa eletronico!")
                    break
                else:
                    print("Opção invalida!")
                    continue

nome = input("Digite seu nome: ")
acc_numero = input("Digite o numero da conta: ")
saldo = float(input("Digite o saldo inicial: "))
cliente = caixa_eletronico(nome, acc_numero, saldo)

cliente.transacao()