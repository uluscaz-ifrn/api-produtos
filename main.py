from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from models import Produto, produtos  # Importando do models.py

app = FastAPI() # Instância do FastAPI

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
def create_produto(produto: Produto):
    for p in produtos:
        if p.id == produto.id:
            return {"message": "ID já existe. Escolha outro ID."}
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
def delete_produto(produto_id: int):
    global produtos
    produtos_filtrados = [p for p in produtos if p.id != produto_id]
    if len(produtos_filtrados) == len(produtos):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    
    produtos = produtos_filtrados
    return {"message": "Produto deletado com sucesso"}

