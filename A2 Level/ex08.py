#Contar quantas vogais existem em uma string

text = input("Digite uma frase: ").lower()
vogais = "aeiou"
cont = 0

for letter in text:
    if letter in vogais:
        cont += 1

print("Quantidade de vogais: ", cont)

#Outra alternativa

texto = input("Digite uma frase: ")
contador = sum(1 for letra in texto.lower() if letra in "aeiou")

print("Quantidade de vogais: ", contador)
