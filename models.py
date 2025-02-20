from pydantic import BaseModel

# Modelo de dados para um produto
class Produto(BaseModel):
    id: int
    nome: str
    preco: float

# Lista de produtos (simulação de um banco de dados)
produtos = [
    Produto(id=1, nome="Produto 1", preco=100.0),
    Produto(id=2, nome="Produto 2", preco=200.0),
    Produto(id=3, nome="Produto 3", preco=300.0)
]
