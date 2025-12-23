"""
Arquivo de testes - Produto e ProdutoService
Rodei esses testes pra garantir se esta funcionando certinho os códigos tanto de produto quanto de produtoservice
"""

from provider.produto import Produto
from provider.produto_service import ProdutoService

def print_separador(msg):
    print("\n" + "="*60)
    print(f" {msg}")
    print("="*60)

def testar_produto():
    print_separador("Testando classe Produto")
    
    try:
        # criando produto normal
        print("\n[Teste 1] Criando produto completo...")
        p1 = Produto("PROD001", "Notebook Dell", 3500.00, 10)
        print(f"OK - {p1}")
        print(f"Codigo: {p1.codigo}, Nome: {p1.nome}, Preco: {p1.preco}, Qtd: {p1.quantidade}")
        
        # produto só com código
        print("\n[Teste 2] Produto so com codigo...")
        p2 = Produto("PROD002")
        print(f"OK - {p2}")
        
        # mudando valores depois
        print("\n[Teste 3] Alterando valores...")
        p2.nome = "Mouse Logitech"
        p2.preco = 150.00
        p2.quantidade = 50
        print(f"OK - {p2}")
        
        # tentando criar sem código (tem que dar erro)
        print("\n[Teste 4] Tentando criar sem codigo...")
        try:
            p3 = Produto("")
            print("ERRO - deveria ter dado excecao!")
        except ValueError as e:
            print(f"OK - erro esperado: {e}")
        
        # testando o to_dict
        print("\n[Teste 5] Convertendo pra dict...")
        print(f"OK - {p1.to_dict()}")
        
        print("\n[OK] Testes do Produto OK!")
        return True
        
    except Exception as e:
        print(f"\nERRO: {e}")
        return False

def testar_service():
    print_separador("Testando ProdutoService")
    
    try:
        service = ProdutoService()
        
        # criando alguns produtos
        print("\n[Teste 1] Criando produtos...")
        p1 = Produto("PROD001", "Notebook", 3500.00, 10)
        p2 = Produto("PROD002", "Mouse", 150.00, 50)
        p3 = Produto("PROD003", "Teclado", 450.00, 30)
        
        service.criar(p1)
        service.criar(p2)
        service.criar(p3)
        print(f"OK - {service.total_produtos()} produtos criados")
        
        # listando tudo
        print("\n[Teste 2] Listando todos...")
        todos = service.listarTodos()
        for p in todos:
            print(f"  {p}")
        print(f"OK - {len(todos)} produtos na lista")
        
        # buscando (case insensitive)
        print("\n[Teste 3] Buscando PROD001 (minusculo)...")
        busca = Produto("prod001")
        encontrado = service.buscarPorCodigo(busca)
        if encontrado:
            print(f"OK - achei: {encontrado}")
        else:
            print("ERRO - nao achou")
        
        # buscando código que não existe
        print("\n[Teste 4] Buscando codigo inexistente...")
        busca2 = Produto("PROD999")
        nao_existe = service.buscarPorCodigo(busca2)
        if nao_existe is None:
            print("OK - retornou None")
        else:
            print("ERRO - deveria ser None")
        
        # atualizando
        print("\n[Teste 5] Atualizando PROD002...")
        atualizar = Produto("PROD002")
        atualizar.nome = "Mouse Gamer"
        atualizar.preco = 250.00
        atualizado = service.atualizar(atualizar)
        if atualizado:
            print(f"OK - atualizado: {atualizado}")
        
        # tentando atualizar um que não existe
        print("\n[Teste 6] Atualizando produto inexistente...")
        fake = Produto("PROD999", "Teste", 100.00, 5)
        resultado = service.atualizar(fake)
        if resultado is None:
            print("OK - retornou None")
        
        # apagando
        print("\n[Teste 7] Apagando PROD003...")
        apagar = Produto("PROD003")
        ok = service.apagar(apagar)
        if ok:
            print(f"OK - apagado! Restam {service.total_produtos()} produtos")
        
        # tentando apagar um que não existe
        print("\n[Teste 8] Apagando produto inexistente...")
        resultado = service.apagar(Produto("PROD999"))
        if resultado is False:
            print("OK - retornou False")
        
        # código duplicado (tem que dar erro)
        print("\n[Teste 9] Tentando criar duplicado...")
        try:
            dup = Produto("PROD001", "Duplicado", 100.00, 5)
            service.criar(dup)
            print("ERRO - deveria ter dado excecao")
        except ValueError as e:
            print(f"OK - erro esperado: {e}")
        
        # estado final
        print("\n[Teste 10] Estado final...")
        finais = service.listarTodos()
        print(f"OK - {len(finais)} produtos no total:")
        for p in finais:
            print(f"  {p}")
        
        print("\n[OK] Testes do Service OK!")
        return True
        
    except Exception as e:
        print(f"\nERRO: {e}")
        import traceback
        traceback.print_exc()
        return False

def testar_casos_especiais():
    print_separador("Testando casos especiais")
    
    try:
        service = ProdutoService()
        
        # código com espaços
        print("\n[Teste 1] Codigo com espacos...")
        p1 = Produto("  PROD001  ", "Teste", 100.00, 5)
        print(f"OK - codigo limpo: '{p1.codigo}'")
        
        # valores None
        print("\n[Teste 2] Valores opcionais None...")
        p2 = Produto("PROD002", "So Nome")
        print(f"OK - nome='{p2.nome}', preco={p2.preco}, qtd={p2.quantidade}")
        
        # atualização parcial (só muda preço)
        print("\n[Teste 3] Atualizacao parcial...")
        service.criar(Produto("PROD003", "Original", 100.00, 10))
        parcial = Produto("PROD003")
        parcial.preco = 200.00
        atualizado = service.atualizar(parcial)
        print(f"OK - resultado: {atualizado}")
        print(f"  Nome mantido: '{atualizado.nome}'")
        print(f"  Preco mudou: {atualizado.preco}")
        print(f"  Qtd mantida: {atualizado.quantidade}")
        
        print("\n[OK] Casos especiais OK!")
        return True
        
    except Exception as e:
        print(f"\nERRO: {e}")
        return False

# roda todos os testes
def rodar_tudo():
    print("\n" + "="*60)
    print("  TESTES - Backend Core (Produto)")
    print("="*60)
    
    resultados = []
    
    resultados.append(("Classe Produto", testar_produto()))
    resultados.append(("ProdutoService", testar_service()))
    resultados.append(("Casos Especiais", testar_casos_especiais()))
    
    # resumo
    print_separador("RESUMO")
    total = len(resultados)
    passou = sum(1 for _, r in resultados if r)
    
    for nome, ok in resultados:
        status = "[OK]" if ok else "[ERRO]"
        print(f"  {status} {nome}")
    
    print(f"\nTotal: {passou}/{total} passaram")
    
    if passou == total:
        print("\nDeu green! ta funfando tudo.")
    else:
        print("\nTem algo completamente errado aq")
    
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    rodar_tudo()