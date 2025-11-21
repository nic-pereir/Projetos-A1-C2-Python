#Receber um número inteiro e exibir se ele é positivo, negativo ou zero

num = int(input("Digite um número inteiro: "))

if num > 0:
    print("O número ", num, " é positivo.")
elif num < 0:
    print("O número ", num, " é negativo.")
else:
    print("O número ", num, " é igual a zero.")