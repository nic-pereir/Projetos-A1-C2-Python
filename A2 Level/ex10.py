#Imprimir a tabuada de um número escolhido pelo usuário

num = int(input("Digite um número: "))
c, total = 0, 0

for c in range(0, 10):
    c += 1
    total = num * c
    print(num, " * ", c, " = ", total)