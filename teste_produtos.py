from models.produtos_dao import Produtos

dao = Produtos()

def exibir_produtos():
    print("\n Lista de Produtos:")
    produtos = dao.select_all()
    for p in produtos:
        print(f"ID: {p[0]}, Nome: {p[1]}, Preço: {p[2]}, Estoque: {p[3]}")

while True:
    print("\n--- MENU TESTE PRODUTOS ---")
    print("1 - Inserir Produto")
    print("2 - Listar Produtos")
    print("3 - Atualizar Produto")
    print("4 - Excluir Produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        if dao.insert(nome, preco, estoque):
            print(" Produto inserido com sucesso.")
        else:
            print(" Falha ao inserir produto.")

    elif opcao == '2':
        exibir_produtos()

    elif opcao == '3':
        id_prod = int(input("ID do produto a ser atualizado: "))
        nome = input("Novo nome: ")
        preco = float(input("Novo preço: "))
        estoque = int(input("Novo estoque: "))
        if dao.update(id_prod, nome, preco, estoque):
            print(" Produto atualizado com sucesso.")
        else:
            print(" Falha ao atualizar produto.")

    elif opcao == '4':
        id_prod = int(input("ID do produto a ser deletado: "))
        if dao.delete(id_prod):
            print(" Produto excluído com sucesso.")
        else:
            print(" Falha ao excluir produto.")

    elif opcao == '0':
        print("Saindo...")
        break

    else:
        print("⚠️ Opção inválida!")
