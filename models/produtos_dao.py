from connection.connect import get_connection

class Produtos:

    def __init__(self) -> None:
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def insert(self, nome: str, preco: float, estoque: int) -> bool:
        try:
            self.cursor.execute("""
                                    INSERT INTO produtos (nome, preco, estoque)
                                    VALUES (?, ?, ?)
                                """, (nome, preco, estoque))
            self.conn.commit()

        except Exception as e:
            print("Erro ao inserir o produto: ", e)
            return False
        
        else:
            return True

    def select_all(self) -> list:
        try:
            produtos = self.cursor.execute("SELECT * FROM produtos ORDER BY id")
            return produtos.fetchall()
        
        except Exception as e:
            print("Erro ao listar os produtos: ", e)

    def select_by_id(self, id: int) -> tuple:
        try:
            produto = self.cursor.execute("SELECT * FROM produtos WHERE id = ?", (id, ))
            return produto.fetchone()

        except Exception as e:
            print("Erro ao buscar o produto: ", e)
        
    def update(self, id: int, nome: str, preco: float, estoque: int) -> bool:
        try:
            self.cursor.execute("""UPDATE produtos 
                                   SET nome = ?, preco = ?, estoque = ? 
                                   WHERE id = ?""", (nome, preco, estoque, id))
            self.conn.commit()

        except Exception as e:
            print("Erro ao tentar atualizar o produto: ", e)
            return False
        
        else:
            return True

    def delete(self, id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM produtos WHERE id = ?", (id, ))
            self.conn.commit()
        
        except Exception as e:
            print("Erro ao tentar deletar o produto: ", e)
            return False
        
        else:
            return True

    def atualizar_estoque(self, produto_id: int, nova_quantidade: int) -> bool:
        try:
            self.cursor.execute("""
                                    UPDATE produtos
                                    SET estoque = ?
                                    WHERE id = ?
                                """, (nova_quantidade, produto_id))
            self.conn.commit()
            
            if self.cursor.rowcount == 0:
                print(f"Nenhum produto com ID {produto_id} foi encontrado para atualizar.")
                return False
            
            return True        
        
        except Exception as e:
            print('Erro ao Atualizar o Estoque: ', e)
            return False