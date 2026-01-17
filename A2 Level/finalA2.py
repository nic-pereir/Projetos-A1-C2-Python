# Criar um To-do List que contenha funções de: adicionar, remover e mudar status de cada tarefa.

task = list()
checklist = dict()

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
    awnser = int(input("Escolha uma opção: "))
    if awnser == 1:
        print("Digite a descrição da tarefa: ")
        checklist["status"] = "[ ]"
        checklist["description"] = str(input("> "))
        task.append(checklist.copy())
        checklist.clear()
        print()
        print("Tarefa adicionada com sucesso!")
        enter()
        
    elif awnser == 2:
        print()
        print("=" *30)
        print("     TAREFAS CADASTRADAS:     ")
        print()
        for i, v in enumerate(task):
            i+=1
            print(f"{i} - {v['status']}  {v['description']}")
        enter()

    elif awnser == 3:
        print()
        print("Digite o número da tarefa concluída: ")
        status = int(input("> "))
        indic = status - 1
        if 0 <= indic < len(task):
            task[indic]["status"] = "[x]"
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido. Essa tarefa não existe.")
        enter()

    elif awnser == 4:
        print()
        print("Digite o número da tarefa a ser removida:")
        remove = int(input("> "))
        index = remove - 1
        if 0 <= index < len(task):
            del task[index]
            print("Tarefa removida com sucesso.")
        else:
            print("Número inválido. Essa tarefa não existe.")
        enter()
    
    else:
        print("Saindo...")