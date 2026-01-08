import sqlite3
from typing import Optional, List, Dict, Any


def _row_to_dict(row: sqlite3.Row) -> Dict[str, Any]:
    """Converte uma linha SQLite Row para dicionário."""
    return dict(row)


def create_customer(conn: sqlite3.Connection, data: Dict[str, Any]) -> Dict[str, Any]:
    if data["saldo_cc"] < 0:
        raise ValueError("O saldo_cc não pode ser negativo")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO clientes (nome, telefone, correntista, score_credito, saldo_cc)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            data["nome"],
            data["telefone"],
            data["correntista"],
            data["score_credito"],
            data["saldo_cc"]
        )
    )
    conn.commit()
    
    # Busca o cliente recém-criado para retornar com o id
    customer_id = cursor.lastrowid
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (customer_id,))
    row = cursor.fetchone()
    cursor.close()
    
    return _row_to_dict(row)


def list_customers(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY id")
    rows = cursor.fetchall()
    cursor.close()
    
    return [_row_to_dict(row) for row in rows]


def get_customer(conn: sqlite3.Connection, customer_id: int) -> Optional[Dict[str, Any]]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (customer_id,))
    row = cursor.fetchone()
    cursor.close()
    
    if row is None:
        return None
    
    return _row_to_dict(row)


def update_customer(conn: sqlite3.Connection, customer_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if "saldo_cc" in data and data["saldo_cc"] < 0:
        raise ValueError("O saldo_cc não pode ser negativo")
    
    existing = get_customer(conn, customer_id)
    if existing is None:
        return None
    
    fields = []
    values = []
    
    for key, value in data.items():
        if key != "id":  # Não permite atualizar o ID
            fields.append(f"{key} = ?")
            values.append(value)
    
    if not fields:
        # Nenhum campo para atualizar, retorna o cliente existente
        return existing
    
    values.append(customer_id)  # Para a cláusula WHERE
    
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE clientes SET {', '.join(fields)} WHERE id = ?",
        values
    )
    conn.commit()
    cursor.close()
    
    return get_customer(conn, customer_id)


def delete_customer(conn: sqlite3.Connection, customer_id: int) -> bool:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (customer_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    cursor.close()
    
    return deleted

