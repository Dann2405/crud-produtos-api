"""
Script pra adicionar uns produtos de teste na API
Bom pra testar rapido sem ficar criando manual
"""

import requests
import json

BASE_URL = "http://localhost:8081/produtos"

# alguns produtos pra testar
produtos = [
    {
        "codigo": "PROD001",
        "nome": "Notebook Dell Inspiron",
        "preco": 3500.00,
        "quantidade": 10
    },
    {
        "codigo": "PROD002",
        "nome": "Mouse Logitech MX Master",
        "preco": 250.00,
        "quantidade": 50
    },
    {
        "codigo": "PROD003",
        "nome": "Teclado Mecanico Keychron",
        "preco": 450.00,
        "quantidade": 30
    },
    {
        "codigo": "PROD004",
        "nome": "Monitor LG 27 polegadas",
        "preco": 1200.00,
        "quantidade": 15
    },
    {
        "codigo": "PROD005",
        "nome": "Webcam Logitech C920",
        "preco": 450.00,
        "quantidade": 25
    },
    {
        "codigo": "PROD006",
        "nome": "Headset HyperX Cloud",
        "preco": 350.00,
        "quantidade": 40
    },
    {
        "codigo": "PROD007",
        "nome": "SSD Samsung 1TB",
        "preco": 600.00,
        "quantidade": 20
    },
    {
        "codigo": "PROD008",
        "nome": "Memoria RAM 16GB DDR4",
        "preco": 300.00,
        "quantidade": 35
    }
]

def popular_produtos():
    print("\n" + "="*50)
    print("Adicionando produtos na API")
    print("="*50 + "\n")
    
    deu_certo = 0
    deu_ruim = 0
    
    for produto in produtos:
        try:
            resp = requests.post(BASE_URL, json=produto)
            
            if resp.status_code == 201:
                print(f"[OK] {produto['codigo']} - {produto['nome']}")
                deu_certo += 1
            else:
                erro = resp.json()
                print(f"[ERRO] {produto['codigo']}: {erro}")
                deu_ruim += 1
                
        except Exception as e:
            print(f"[ERRO] Nao deu pra criar {produto['codigo']}: {e}")
            deu_ruim += 1
    
    print("\n" + "="*50)
    print(f"Resumo: {deu_certo} criados, {deu_ruim} com problema")
    print("="*50 + "\n")
    
    # mostra o que foi criado
    if deu_certo > 0:
        print("Lista dos produtos:")
        print()
        try:
            resp = requests.get(BASE_URL)
            lista = resp.json()
            
            for p in lista:
                print(f"  {p['codigo']}: {p['nome']}")
                print(f"    Preco: R$ {p['preco']:.2f} | Estoque: {p['quantidade']} un")
                print()
        except Exception as e:
            print(f"Deu problema ao listar: {e}")

if __name__ == "__main__":
    print()
    print("Opa! Antes de continuar...")
    print("Certifica que o servidor ta rodando: python ws_provider.py")
    print()
    
    continuar = input("Bora popular? (s/n): ").lower().strip()
    
    if continuar == 's' or continuar == 'sim' or continuar == 'y':
        print()
        popular_produtos()
        
        print("Pronto! Agora abre no navegador:")
        print("http://127.0.0.1:8081/produtos")
        print()
    else:
        print("\nBlz, quando quiser e so rodar de novo!")