#Inverter uma string sem usar funções prontas

phrase = input("Escreva uma frase: ")
chars = []                              # lista vazia para acumular caracteres

for i in range(len(phrase) -1, -1, -1):    # -1: conta quantos caracteres tem a string -- -1: até onde a contagem vai -- -1: "contagem" regressiva
    chars.append(phrase[i])             # adiciona cada caractere à lista

invert = "".join(chars)                 # junta a lista numa string só
print(invert)



