#Dado um número, verificar se é par ou ímpar

num = int(input("Digite um número inteiro: "))

if (num % 2) == 0:
    print("O número ", num, " é um número par.")
else:
    print("O número ", num, " é um número ímpar.")