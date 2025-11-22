#Pedir números ao usuário e somá-los até ele digitar 0

total = 0 

while True:
    num = int(input("Digite um número inteiro: "))
    total += num
    if num == 0:
        break

print("A soma dos números foi de ", total)
