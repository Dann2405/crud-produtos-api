"""
ProdutoService - gerencia as operações com produtos na memória de forma simpls
"""

from produto import Produto

class ProdutoService:
    
    def __init__(self):
        self.__produtos = []
    
    def criar(self, produto):
        if not isinstance(produto, Produto):
            raise ValueError("Precisa ser um Produto válido")
        
        # checa se já existe
        if self._buscar_interno(produto.codigo):
            raise ValueError(f"Já tem um produto com código '{produto.codigo}'")
        
        self.__produtos.append(produto)
        return produto
    
    def buscarPorCodigo(self, produto):
        if not isinstance(produto, Produto):
            raise ValueError("Precisa ser um Produto válido")
        
        return self._buscar_interno(produto.codigo)
    
    def atualizar(self, produto):
        if not isinstance(produto, Produto):
            raise ValueError("Precisa ser um Produto válido")
        
        prod_existente = self._buscar_interno(produto.codigo)
        
        if not prod_existente:
            return None
        
        # só atualiza o que não é None
        if produto.nome is not None:
            prod_existente.nome = produto.nome
        
        if produto.preco is not None:
            prod_existente.preco = produto.preco
        
        if produto.quantidade is not None:
            prod_existente.quantidade = produto.quantidade
        
        return prod_existente
    
    def apagar(self, produto):
        if not isinstance(produto, Produto):
            raise ValueError("Precisa ser um Produto válido")
        
        prod_existente = self._buscar_interno(produto.codigo)
        
        if not prod_existente:
            return False
        
        self.__produtos.remove(prod_existente)
        return True
    
    def listarTodos(self):
        return self.__produtos.copy()
    
    def _buscar_interno(self, codigo):
        # busca ignorando maiúsculas/minúsculas
        cod_busca = codigo.lower().strip()
        
        for p in self.__produtos:
            if p.codigo.lower() == cod_busca:
                return p
        
        return None
    
    def total_produtos(self):
        return len(self.__produtos)