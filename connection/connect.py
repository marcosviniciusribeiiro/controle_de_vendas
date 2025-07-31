import sqlite3
import os

db_path = 'dados.db'
conn = None  

def get_connection():
    global conn
    if conn is None:
        conn = sqlite3.connect(db_path)
    return conn

def create_database() -> None:
    global conn
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_venda TEXT NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            total_venda REAL NOT NULL,
            FOREIGN KEY(produto_id) REFERENCES produtos(id)
        );
    """)

    cursor.close()
    conn.commit()
    print("Banco de dados criado com sucesso.")

def drop_database() -> None:
    global conn
    try:
        if conn:
            conn.close()
            conn = None
        if os.path.exists(db_path):
            os.remove(db_path)
            print("Banco de dados apagado com sucesso.")
        else:
            print("Arquivo do banco não existe.")
    except Exception as e:
        print("Erro ao apagar o banco:", e)
