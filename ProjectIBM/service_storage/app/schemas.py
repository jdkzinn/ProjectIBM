from pydantic import BaseModel, Field


class CustomerBase(BaseModel):
    nome: str = Field(..., max_length=255, description="Nome do cliente")
    telefone: str = Field(..., max_length=15, description="Telefone do cliente")
    correntista: bool = Field(..., description="Indica se é correntista")
    score_credito: float = Field(..., description="Score de crédito do cliente")
    saldo_cc: float = Field(..., ge=0, description="Saldo da conta corrente (deve ser >= 0)")
 

class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    nome: str | None = Field(None, max_length=255, description="Nome do cliente")
    telefone: str | None = Field(None, max_length=15, description="Telefone do cliente")
    correntista: bool | None = Field(None, description="Indica se é correntista")
    score_credito: float | None = Field(None, description="Score de crédito do cliente")
    saldo_cc: float | None = Field(None, ge=0, description="Saldo da conta corrente (deve ser >= 0)")


class CustomerOut(CustomerBase):
    """Schema para resposta de cliente (inclui o id)."""
    id: int = Field(..., description="ID único do cliente")
    
    class Config:
        from_attributes = True
