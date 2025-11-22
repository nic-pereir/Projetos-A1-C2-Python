#Verificar se um nome está em uma lista de convidados

list_names = ["Ana", "Carlos", "Lucas", "Maria", "Greice", "Pedro", "Antonio", "Bruna"]

print(list_names)

name = input("Digite um nome para verificar se ele está na lista: ")
name = name.strip().lower() # Padroniza o nome em minúsculo e sem espaços

# Cria uma lista padronizada em minúsculo
list_names_lower = [n.lower() for n in list_names]

if name in list_names_lower:
    print("Está na lista!")
else:
    print("Não está na lista!")
