from connection.connect import get_connection

class Vendas:

    def __init__(self) -> None:
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def insert(self, data_venda: str, produto_id: int, quantidade: int, total_venda: float) -> bool:
        try:
            self.cursor.execute("""
                                INSERT INTO vendas(data_venda, produto_id, quantidade, total_venda)
                                VALUES (?, ?, ?, ?)
                                """, (data_venda, produto_id, quantidade, total_venda))
            self.conn.commit()
            print("Commit executado com sucesso.")

        except Exception as e:
            print("Erro ao inserir venda: ", e)
            return False
        
        else:
            return True
        
    def select_all(self) -> list:
        try:
            vendas = self.cursor.execute("SELECT * FROM vendas ORDER BY id, data_venda")
            return vendas.fetchall()
        
        except Exception as e:
            print("Erro ao listar as vendas: ", e)

    def select_by_id(self, id: int) -> tuple:
        try:
            venda = self.cursor.execute("SELECT * FROM vendas WHERE id = ?", (id, ))
            return venda.fetchone()

        except Exception as e:
            print("Erro ao buscar a venda: ", e)

    def buscar_quantidade_por_id(self, id: int) -> int:
        self.cursor.execute("SELECT quantidade FROM vendas WHERE id = ?", (id,))
        resultado = self.cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            raise ValueError(f'Nenhuma venda encontrada com ID {id}')

    def update(self, id: int, data_venda: str, produto_id: int, quantidade: int, total_venda: float) -> bool:
        try:
            self.cursor.execute("""UPDATE vendas
                                   SET data_venda = ?, produto_id = ?, quantidade = ?, total_venda = ?
                                   WHERE id = ?""", (data_venda, produto_id, quantidade, total_venda, id))
            self.conn.commit()

        except Exception as e:
            print("Erro ao tentar atualizar a venda: ", e)
            return False
        
        else:
            return True
        
    def delete(self, id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM vendas WHERE id = ?", (id, ))
            self.conn.commit()
        
        except Exception as e:
            print("Erro ao tentar deletar a venda: ", e)
            return False
        
        else:
            return True