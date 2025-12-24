import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from provider.produto_service import ProdutoService
from provider.produto import Produto
from urllib.parse import urlparse, parse_qs

class WSProvider(BaseHTTPRequestHandler):
    
    service = ProdutoService()
    
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    def do_GET(self):

        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/produtos":
            print("Requisição GET recebida - LISTAR PRODUTOS")
            produtos = self.service.listarTodos()
            produtos_list = [
                {
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "preco": p.preco,
                    "quantidade": p.quantidade
                } for p in produtos
            ]
            self._set_headers()
            self.wfile.write(json.dumps(produtos_list).encode())

        elif 'codigo' in query :
            codigo = query.get("codigo", [None])[0]
            print(f"Requisição GET recebida - BUSCAR PRODUTO {codigo}")
            if not codigo:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Código é obrigatório"}).encode())
                return
            
            produto = self.service.buscarPorCodigo(Produto(codigo=codigo))
            if produto:
                self._set_headers()
                response = {
                    "codigo": produto.codigo,
                    "nome": produto.nome,
                    "preco": produto.preco,
                    "quantidade": produto.quantidade
                }
                self.wfile.write(json.dumps(response).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Produto não encontrado"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())
    
    def do_POST(self):
        parsed = urlparse(self.path)

        if parsed.path == "/produtos":
            print("Requisição POST recebida - ADICIONAR PRODUTO")
            
            try: 
                content_length = int(self.headers.get('Content-Length', 0)) 
                if content_length == 0:
                    raise ValueError("Corpo da requisição vazio") 
                raw_data = self.rfile.read(content_length)
                data = json.loads(raw_data.decode('utf-8'))  
                
                if not data.get("codigo"):
                    raise ValueError("Campo 'codigo' é obrigatório")

                produto = Produto(
                    codigo=data["codigo"],
                    nome=data.get("nome"),
                    preco=data.get("preco"),
                    quantidade=data.get("quantidade")
                )
                criado = self.service.criar(produto)

                self._set_headers(201)
                response = {
                    "codigo": criado.codigo,
                    "nome": criado.nome,
                    "preco": criado.preco,
                    "quantidade": criado.quantidade
                }
                self.wfile.write(json.dumps(response).encode())
            except ValueError as e:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    def do_PUT(self):

        parsed = urlparse(self.path)
        if parsed.path == "/produtos":
            print("Requisição PUT recebida - ATUALIZAR PRODUTO")
            
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                if content_length == 0:
                     raise ValueError("Corpo da requisição vazio")
            
                raw_data = self.rfile.read(content_length)
                data = json.loads(raw_data.decode('utf-8'))

                produto = Produto(
                    codigo=data["codigo"],
                    nome=data.get("nome"),
                    preco=data.get("preco"),
                    quantidade=data.get("quantidade")
                )
                atualizado = self.service.atualizar(produto)

                if atualizado:
                    self._set_headers()
                    response = {
                        "codigo": atualizado.codigo,
                        "nome": atualizado.nome,
                        "preco": atualizado.preco,
                        "quantidade": atualizado.quantidade
                    }
                    self.wfile.write(json.dumps(response).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Produto não encontrado"}).encode())
            except ValueError as e:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())


    def do_DELETE(self):
        parsed = urlparse(self.path)

        if  parsed.path == "/produtos":
            query_params = parse_qs(parsed.query)
            
            print("Requisição DELETE recebida - APAGAR PRODUTO")
            codigo = query_params.get("codigo", [None])[0]
            if not codigo:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Código é obrigatório"}).encode())
                return
            
            try:
                produto = Produto(codigo=codigo)
                apagado = self.service.apagar(produto)

                if apagado:
                    self._set_headers(204)
                    self.wfile.write(b'')
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Produto não encontrado"}).encode())
            except ValueError as e:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())                   

def main():
    # Inicia o servidor HTTP na porta 8081
    servidor = HTTPServer(('127.0.0.1', 8081), WSProvider)
    print("Servidor iniciado em http://127.0.0.1:8081")
    servidor.serve_forever()

if __name__ == "__main__":
    main()