# Crud pro FASTAPI (roteamento e etc) para operações na tabela clientes

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
import sqlite3
from typing import List

from app.schemas import CustomerCreate, CustomerOut, CustomerUpdate
from app import crud
from app.database import conn

app = FastAPI(
    title="Service Storage",
    description="Serviço de armazenamento de clientes",
    version="1.0.0"
)


@app.get("/customers", response_model=List[CustomerOut])
def list_customers():
    """Lista todos os clientes."""
    try:
        customers = crud.list_customers(conn)
        return customers
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao listar clientes: {str(e)}"
        )


@app.get("/customers/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int):
    """Obtém um cliente específico por ID."""
    try:
        customer = crud.get_customer(conn, customer_id)
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente não encontrado"
            )
        return customer
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao buscar cliente: {str(e)}"
        )


@app.post("/customers", response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate):
    """Cria um novo cliente."""
    try:
        new_customer = crud.create_customer(conn, customer.model_dump())
        return new_customer
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except sqlite3.IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cliente com este telefone já existe"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar cliente: {str(e)}"
        )


@app.put("/customers/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, customer: CustomerUpdate):
    """Atualiza um cliente existente."""
    try:
        updated_customer = crud.update_customer(
            conn, customer_id, customer.model_dump(exclude_unset=True)
        )
        if not updated_customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente não encontrado"
            )
        return updated_customer
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar cliente: {str(e)}"
        )


@app.delete("/customers/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int):
    """Deleta um cliente."""
    try:
        result = crud.delete_customer(conn, customer_id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente não encontrado"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao deletar cliente: {str(e)}"
        )


@app.get("/health")
def health_check():
    """Verificação de saúde da API."""
    return {"status": "ok", "service": "storage"}