#Receber uma palavra e dizer se é palíndromo

word = str(input("Digite uma palavra para verificar se é um palíndromo: "))
chars = []

for i in range(len(word) - 1, -1, -1):
    chars.append(word[i])

invert = "".join(chars)
print (invert)

if invert == word:
    print(f"A palavra {word} é um palíndromo.")
else:
    print(f"A palavra {word} não é um palíndromo.")