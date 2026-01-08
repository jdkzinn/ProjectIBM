import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "projectibm.db"

# Conexão global (para apresentação / exemplo)
conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
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

print("Banco 'projectibm.db' e tabela 'clientes' verificados/criados com sucesso")

conn.commit()
cursor.close()
