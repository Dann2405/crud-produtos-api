import requests
import json

class ClienteProduto:
    def __init__(self):
        self.base_url = "http://localhost:8080"
        self.endpoint = f"{self.base_url}/produto"


    def criar_produto(self, codigo, nome, preco, quantidade):
        payload = {
            "codigo": codigo,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        response = requests.post(self.endpoint, json=payload)
        print("CRIAR PRODUTO:")
        print(response.json())
        print("=" * 30)

    
    def buscar_produto(self, codigo):
        response = requests.get(f"{self.endpoint}/{codigo}")
        print("BUSCAR PRODUTO:")
        print(response.json())
        print("=" * 30)      
        
    def atualizar_produto(self, codigo, nome=None, preco=None, quantidade=None):
        payload = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        response = requests.put(f"{self.endpoint}/{codigo}", json=payload)
        print("ATUALIZAR PRODUTO:")
        print(response.json())
        print("=" * 30)

    def apagar_produto(self, codigo):
        response = requests.delete(f"{self.endpoint}/{codigo}")
        print("APAGAR PRODUTO:")
        print(response.json())
        print("=" * 30)

    def listar_produtos(self):
        response = requests.get(self.endpoint)
        dados_json = response.json()

        print("=" * 30)
        print("RESULTADO LISTA DE PRODUTOS:")
        for produto in dados_json:
            print(
                f"Código: {produto['codigo']}, "
                f"Nome: {produto['nome']}, "
                f"Preço: {produto['preco']}, "
                f"Quantidade: {produto['quantidade']}"
            )
        print("=" * 30)
      

if __name__ == "__main__":
    produto = ClienteProduto()
    

