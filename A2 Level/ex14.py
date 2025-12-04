#Calcular a média de notas armazenadas em uma lista.

lista = list()
sum = 0

while True:
    nota = float(input("Digite uma nota: "))
    lista.append(nota)
    sum += nota
    
    opc = str(input("Deseja continuar [S/N]? ").upper().strip())
    if opc != "S":
        break

media = sum / len(lista)
lista.sort()
print(f"A média da lista de notas {lista} é de {media:.2f}.")