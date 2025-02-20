from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # Instância do FastAPI

# Modelo de dados para um produto
class Produto(BaseModel):
    id: int
    nome: str
    preco: float

# Lista de produtos
produtos = [
    Produto(id=1, nome="Produto 1", preco=100.0),
    Produto(id=2, nome="Produto 2", preco=200.0),
    Produto(id=3, nome="Produto 3", preco=300.0)
]

@app.get("/produtos/")
def get_produtos(): # Função que retorna a lista de produtos
    return produtos

@app.get("/produtos/{produto_id}")
def get_produto(produto_id: int): # Função que retorna um produto específico
    for produto in produtos:
        if produto.id == produto_id:
            return produto
    return {"message": "Produto não encontrado"}

@app.post("/produtos/")
def create_produto(produto: Produto): # Função que cria um novo produto
    produtos.append(produto)
    return produto

@app.put("/produtos/{produto_id}")
def update_produto(produto_id: int, produto: Produto): # Função que atualiza um produto
    for i in range(len(produtos)):
        if produtos[i].id == produto_id:
            produtos[i] = produto
            return produto
    return {"message": "Produto não encontrado"}

@app.delete("/produtos/{produto_id}")
def delete_produto(produto_id: int): # Função que deleta um produto
    for i in range(len(produtos)):
        if produtos[i].id == produto_id:
            produto = produtos[i]
            del produtos[i]
            return produto
    return {"message": "Produto não encontrado"}
