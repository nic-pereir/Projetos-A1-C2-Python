#Receber 5 números em uma lista e exibir o maior

num = []

for _ in range(5): # Aqui, usei o _ (underline) pra não precisar declarar uma variável, já que não vou usá-la
    num.append(int(input("Digite um número: ")))

print("O maior número entre eles é o ", max(num))


# Outra alternativa

numeros = [int(input("Digite um número: ")) for _ in range(5)]
print("O maior número é:", max(numeros))