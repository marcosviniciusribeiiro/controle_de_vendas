from models.vendas_dao import Vendas

def menu():
    print("\n----- MENU DE VENDAS -----")
    print("1 - Inserir nova venda")
    print("2 - Listar todas as vendas")
    print("3 - Buscar venda por ID")
    print("4 - Atualizar venda")
    print("5 - Deletar venda")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def main():
    dao = Vendas()

    while True:
        opcao = menu()

        if opcao == "1":
            data = input("Data da venda (AAAA-MM-DD): ")
            data = data.replace('/', '-')
            
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade vendida: "))
            total = float(input("Total da venda: "))

            if dao.insert(data, produto_id, quantidade, total):
                print("Venda inserida com sucesso!")
            else:
                print("Erro ao inserir venda.")

        elif opcao == "2":
            vendas = dao.select_all()
            if vendas:
                print("\n--- Vendas Cadastradas ---")
                for v in vendas:
                    print(f"ID: {v[0]}, DATA_VENDA: {v[1]}, PRODUTO_ID: {v[2]}, QUANTIDADE: {v[3]}, TOTAL_VENDA: {v[4]} R$")
            else:
                print("Nenhuma venda cadastrada.")

        elif opcao == "3":
            id_busca = int(input("ID da venda que deseja buscar: "))

            venda = dao.select_by_id(id_busca)

            if venda:
                print(f"Venda encontrada: ID: {venda[0]}, DATA_VENDA: {venda[1]}, PRODUTO_ID: {venda[2]}, QUANTIDADE: {venda[3]}, TOTAL_VENDA: {venda[4]} R$")
            else:
                print("Venda não encontrada.")

        elif opcao == "4":
            id_atualizar = int(input("ID da venda que deseja atualizar: "))
            data = input("Nova data (AAAA-MM-DD): ")
            produto_id = int(input("Novo ID do produto: "))
            quantidade = int(input("Nova quantidade: "))
            total = float(input("Novo total da venda: "))

            if dao.update(id_atualizar, data, produto_id, quantidade, total):
                print("Venda atualizada com sucesso!")
            else:
                print("Erro ao atualizar venda.")

        elif opcao == "5":
            id_deletar = int(input("ID da venda que deseja deletar: "))
            if dao.delete(id_deletar):
                print("Venda deletada com sucesso!")
            else:
                print("Erro ao deletar venda.")

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
