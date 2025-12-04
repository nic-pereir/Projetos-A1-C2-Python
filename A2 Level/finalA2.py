#Sistema de Gerenciamento de Lista de Tarefas (To-Do List)

ficha = list()

while True:
    add = str(input("Adicionar tarefa: "))
    print("[P] PENDENTE --- [E] EM PROCESSO --- [C] CONCLUIDO")
    status = str(input("Qual o status da tarefa? ").upper().strip())
    ficha.append([add, status])
    question = str(input("Deseja ver a lista de tarefas [S/N]? ").upper().strip())
    if question != "S":
        break
    else:
        print("A sua lista atual está com os seguintes itens e status: ")
        print("-" * 40)
        print(f"{"ITEM":15}" {"STATUS":15})
        for i, j in enumerate(ficha):
            print(f"{j[0]}", {j[1]})
 