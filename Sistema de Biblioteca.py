# Lista que armazenará os livros cadastrados
livros = []

# Função responsável por cadastrar um novo livro
def cadastrar_livro(nome):
    livros.append(nome)
    print(f"Livro '{nome}' cadastrado com sucesso!")

# Função responsável por listar todos os livros cadastrados
def listar_livros():

    # Verifica se a lista está vazia
    if not livros:
        print("\nNão há livros cadastrados.")
        return

    print("\n--- LIVROS DISPONÍVEIS ---")

    # Percorre a lista exibindo os livros numerados
    for i, nome in enumerate(livros, start=1):
        print(f"{i}. {nome}")

    print("--------------------------")


# Função responsável por atualizar o nome de um livro
def atualizar_livro(nome_antigo, nome_novo):

    # Verifica se o livro existe na lista
    if nome_antigo in livros:
        indice = livros.index(nome_antigo)
        livros[indice] = nome_novo
        print(f"Livro '{nome_antigo}' atualizado para '{nome_novo}'!")

    else:
        print(f"Erro: Livro '{nome_antigo}' não encontrado.")


# Função responsável por remover um livro da lista
def apagar_livro(nome):

    # Verifica se o livro existe antes de removê-lo
    if nome in livros:
        livros.remove(nome)
        print(f"Livro '{nome}' removido com sucesso!")

    else:
        print(f"Erro: Livro '{nome}' não encontrado.")


# Laço principal do sistema
# Mantém o menu em execução até o usuário escolher sair
while True:

    # Exibição do menu principal
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1. Cadastrar Livro")
    print("2. Visualizar Livros")
    print("3. Atualizar Livro")
    print("4. Apagar Livro")
    print("5. Sair")
    print("=============================")

    # Recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção (1-5): ")

    # Estrutura de decisão para executar a funcionalidade escolhida
    match opcao:

        # Cadastro de livro
        case "1":
            nome = input("Digite o nome do livro: ")
            cadastrar_livro(nome)

        # Listagem dos livros cadastrados
        case "2":
            listar_livros()

        # Atualização de um livro existente
        case "3":
            antigo = input("Digite o nome do livro que deseja atualizar: ")
            novo = input("Digite o novo nome do livro: ")
            atualizar_livro(antigo, novo)

        # Exclusão de um livro
        case "4":
            nome = input("Digite o nome do livro que deseja apagar: ")
            apagar_livro(nome)

        # Encerramento do programa
        case "5":
            print("Saindo do sistema...")
            break

        # Tratamento para opções inválidas
        case _:
            print("Opção inválida. Tente novamente.")
