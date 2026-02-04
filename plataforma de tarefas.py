tarefas = []


def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")

    tarefa = {
        "título": titulo,
        "descrição": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['título']} - {tarefa['descrição']} [{status}]")


def marcar_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")


def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida com sucesso!")
    else:
        print("Índice inválido.")


def mostrar_menu():
    print("\nMenu de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("0. Sair")


def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()

        elif escolha == "2":
            listar_tarefas()

        elif escolha == "3":
            try:
                indice = int(input("Digite o índice da tarefa: ")) - 1
                marcar_concluida(indice)
            except ValueError:
                print("Digite um número válido.")

        elif escolha == "4":
            try:
                indice = int(input("Digite o índice da tarefa: ")) - 1
                remover_tarefa(indice)
            except ValueError:
                print("Digite um número válido.")

        elif escolha == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
# Programa de Gerenciamento de Tarefas

