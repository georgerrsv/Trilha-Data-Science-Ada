def verifica_par():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

    if ((x + y)% 2) == 0:
        print("O resultado é =", x+y)
        print("A soma dos números é par.")
    else:
        print("O resultado é =", x+y) 
        print("A soma dos números é ímpar.")

verifica_par()

def check_negativo():
    x = int(input("Digite um número: "))
    if (x < 0):
        print("O número é negativo.")
    else:
        print("O número é positivo.")

check_negativo()

def aprovado():
    nota = int(input("Digite a nota do aluno: "))
    
    if(nota >= 6):
        print("Aluno aprovado")
    else :
        print("Aluno reprovado")