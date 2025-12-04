#Verificar se uma senha tem pelo menos 8 caracteres.

password = str(input("Digite uma senha com, pelo menos, 8 caracteres: "))
if len(password) >= 8:
    print("Parabéns! A sua senha possui pelo menos de 8 caracteres.")
else:
    print("Infelizmente a sua senha não possui pelo menos 8 caracteres.")