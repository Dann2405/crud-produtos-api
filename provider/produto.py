"""
Classe Produto - representa um produto no sistema como se fosse um inventario
"""

class Produto:
    
    def __init__(self, codigo, nome=None, preco=None, quantidade=None):
        # Valida se tem código
        if not codigo or str(codigo).strip() == "":
            raise ValueError("Código é obrigatório")
        
        self.__codigo = str(codigo).strip()
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("Código é obrigatório")
        self.__codigo = str(valor).strip()
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor is not None:
            try:
                self.__preco = float(valor)
            except (ValueError, TypeError):
                raise ValueError("Preço inválido")
        else:
            self.__preco = None
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        if valor is not None:
            try:
                self.__quantidade = int(valor)
            except (ValueError, TypeError):
                raise ValueError("Quantidade inválida")
        else:
            self.__quantidade = None
    
    def to_dict(self):
        return {
            "codigo": self.__codigo,
            "nome": self.__nome,
            "preco": self.__preco,
            "quantidade": self.__quantidade
        }
    
    def __str__(self):
        return f"Produto(codigo='{self.codigo}', nome='{self.nome}', preco={self.preco}, quantidade={self.quantidade})"