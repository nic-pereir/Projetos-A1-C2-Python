#Receber horas trabalhadas e valor por hora, e calcular o salário do mês.

value = float(input("Digite o valor de cada hora de trabalho: R$"))
time = int(input("Digite o valor da quantidade de horas trabalhadas por semana: "))
week = time * 4
salary = week * value

print("O seu salário, ao final do mês, será de R$", salary, ".")