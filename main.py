from connection.connect import create_database
from windows.cadastrar_produtos import P_Window
from windows.registrar_vendas import V_Window

if __name__ == '__main__':
    create_database()  

    # Cadastro de Produtos - Interface Gráfica
    tela1 = P_Window()

    # Registro de Vendas - Interface Gráfica
    # tela2 = V_Window() 

    tela1.run()
    # tela2.run() 