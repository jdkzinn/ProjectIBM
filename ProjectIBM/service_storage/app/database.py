import sqlite3

conn = sqlite3.connect("projectibm.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

sql_clientes = """
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL,
        telefone VARCHAR(15) NOT NULL UNIQUE,
        correntista BOOLEAN NOT NULL,
        score_credito FLOAT NOT NULL,
        saldo_cc FLOAT NOT NULL CHECK (saldo_cc >= 0)
    );
"""
cursor.execute(sql_clientes) 

print("Banco ''projectibm.db'' e tabela ''clientes'' criados com sucesso")

conn.commit()

conn.close()
