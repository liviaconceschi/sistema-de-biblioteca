livros = []

def cadastrar_livro(nome):
    livros.append(nome)
    print(f"Livro '{nome}' cadastrado com sucesso!")

def listar_livros():
    if not livros:
        print("\nNão há livros cadastrados.")
        return

    print("\n--- LIVROS DISPONÍVEIS ---")
    for i, nome in enumerate(livros, start=1):
        print(f"{i}. {nome}")
    print("--------------------------")

def atualizar_livro(nome_antigo, nome_novo):
    if nome_antigo in livros:
        indice = livros.index(nome_antigo)
        livros[indice] = nome_novo
        print(f"Livro '{nome_antigo}' atualizado para '{nome_novo}'!")
    else:
        print(f"Erro: Livro '{nome_antigo}' não encontrado.")

def apagar_livro(nome):
    if nome in livros:
        livros.remove(nome)
        print(f"Livro '{nome}' removido com sucesso!")
    else:
        print(f"Erro: Livro '{nome}' não encontrado.")



while True:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1. Cadastrar Livro")
    print("2. Visualizar Livros")
    print("3. Atualizar Livro")
    print("4. Apagar Livro")
    print("5. Sair")
    print("=============================")

    opcao = input("Escolha uma opção (1-5): ")

    match opcao:

        case "1":
            nome = input("Digite o nome do livro: ")
            cadastrar_livro(nome)

        case "2":
            listar_livros()

        case "3":
            antigo = input("Digite o nome do livro que deseja atualizar: ")
            novo = input("Digite o novo nome do livro: ")
            atualizar_livro(antigo, novo)

        case "4":
            nome = input("Digite o nome do livro que deseja apagar: ")
            apagar_livro(nome)

        case "5":
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida. Tente novamente.")