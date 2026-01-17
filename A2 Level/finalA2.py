tasks = []


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


def pause():
    input("\nPressione ENTER para voltar ao menu...\n")


def add_task(tasks):
    description = input("Digite a descrição da tarefa: ")
    task = {
        "status": "[ ]",
        "description": description
    }
    tasks.append(task)
    print("Tarefa adicionada com sucesso!")


def list_tasks(tasks):
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nTAREFAS CADASTRADAS:\n")
    for i, task in enumerate(tasks, start=1):
        print(f"{i} - {task['status']} {task['description']}")


def get_valid_index(tasks, message):
    try:
        number = int(input(message))
        index = number - 1
        if 0 <= index < len(tasks):
            return index
        else:
            print("Número inválido.")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return None


def update_status(tasks):
    index = get_valid_index(tasks, "Digite o número da tarefa concluída: ")
    if index is not None:
        tasks[index]["status"] = "[x]"
        print("Tarefa marcada como concluída!")


def remove_task(tasks):
    index = get_valid_index(tasks, "Digite o número da tarefa a ser removida: ")
    if index is not None:
        del tasks[index]
        print("Tarefa removida com sucesso!")

while True:
    show_menu()
    option = input("Escolha uma opção: ")

    if option == "1":
        add_task(tasks)
        pause()

    elif option == "2":
        list_tasks(tasks)
        pause()

    elif option == "3":
        update_status(tasks)
        pause()

    elif option == "4":
        remove_task(tasks)
        pause()

    elif option == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
        pause()
