# Criar um To-do List que contenha funções de: adicionar, remover e mudar status de cada tarefa.

task = list()
checklist = dict(status = "P" or "C", description = str)

def show_menu():
    print("=" * 30)
    print("      TO DO LIST SIMPLES      ")
    print("=" * 30)
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Modificar status")
    print("4 - Remover tarefa")
    print("5 - Sair")
    print()

def enter():
    print()
    input("Pressione ENTER para voltar ao menu...")
    print()
    show_menu()

show_menu()

while True:
    print()
    awnser = int(input("Escolha uma opção: "))
    if awnser == 1:
        print("Digite a descrição da tarefa: ")
        checklist["status"] = "[ ]"
        checklist["description"] = str(input("> "))
        task.append(checklist)
        print()
        print("Tarefa adicionada com sucesso!")
        enter()
        
    elif awnser == 2:
        print()
        print("=" *30)
        print("     TAREFAS CADASTRADAS:     ")
        print()
        for i, v in enumerate(task):
            i +=1
            print(f"{i} - {v}")   
        enter()
    elif awnser == 3:
        print()
        print("Digite o número da tarefa concluída: ")
        status = int(input("> "))
        if status not in task:
            print("Tente novamente.")
            show_menu()
        else:

            print("Tarefa marcada como concluída!")
        enter()