from connection.connect import create_database, drop_database

def menu_banco():
    while True:
        print("\n=== MENU DO BANCO ===")
        print("1 - Criar banco")
        print("2 - Apagar banco")
        print("3 - Sair")

        op = input("Escolha: ")

        if op == "1":
            create_database()
        elif op == "2":
            drop_database()
        elif op == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu_banco()
