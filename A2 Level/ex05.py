#Somar todos os números de 1 a 100 com um loop

c = 0
total = 0

for c in range(0, 100):
    print(c+1)
    c += 1
    total += c

print("A soma de todos os números anteriores é de ", total)

#Outra forma de fazer o exercício

total = sum(range(1, 101))
print("\n", total)
