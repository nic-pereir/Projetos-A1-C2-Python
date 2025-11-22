#Cirar um calculadora no terminal que permite recomeçar sem fechar o programa

print("----- OPERACOES -----")
print("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Recomeçar")

final = 0
again = "S"

while again.upper() == "S":

    operator = int(input("\nDigite o operador: "))

    if operator == 5:
        print("\nRecomeçando a calculadora...\n")
        final = 0
        continue  

    num = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    if operator not in [1,2,3,4,5]:
        print("Opção inválida. Tente novamente.")
        continue
    elif operator == 1:
        total = num + num2
    elif operator == 2:
        total = num - num2
    elif operator == 3:
        total = num * num2
    elif operator == 4:
        total = num / num2

    final += total

    print(f"Resultado desta operação: {total}")
    print(f"Total acumulado: {final}")

    again = input("\nDeseja continuar (S/N)? ").upper()

print("\nO total final foi:", final)
