from provider.produto import Produto
from provider.produto_service import ProdutoService

service = ProdutoService()

def cmd_listar():
    produtos = service.listarTodos()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(p)

def cmd_criar(codigo, nome, preco, quantidade):
    try:
        produto = Produto(
            codigo=codigo,
            nome=nome,
            preco=preco,
            quantidade=quantidade
        )
        criado = service.criar(produto)
        print(f"Criado: {criado}")
    except Exception as e:
        print(f"Erro ao criar: {e}")


def cmd_buscar(codigo):
    try:
        encontrado = service.buscarPorCodigo(Produto(codigo))
        if encontrado:
            print(encontrado)
        else:
            print("Produto não encontrado")
    except Exception as e:
        print(f"Erro na busca: {e}")


def cmd_atualizar(codigo, nome=None, preco=None, quantidade=None):
    try:
        produto = Produto(codigo=codigo)

        if nome is not None:
            produto.nome = nome
        if preco is not None:
            produto.preco = preco
        if quantidade is not None:
            produto.quantidade = quantidade

        atualizado = service.atualizar(produto)
        if atualizado:
            print(f"Atualizado: {atualizado}")
        else:
            print("Produto não encontrado para atualizar")
    except Exception as e:
        print(f"Erro ao atualizar: {e}")


def cmd_apagar(codigo):
    try:
        apagado = service.apagar(Produto(codigo))
        if apagado:
            print("Produto apagado com sucesso")
        else:
            print("Produto não encontrado para apagar")
    except Exception as e:
        print(f"Erro ao apagar: {e}")

def main():
    while True:
        print("=" * 25)
        print("Gerenciador de Produtos")
        print("=" * 25)
        print("1 - Listar produtos")
        print("2 - Criar produto")
        print("3 - Buscar produto")
        print("4 - Atualizar produto")
        print("5 - Apagar produto")
        print("0 - Sair")

        resp = input("Escolha uma opção: ")

        if resp == '1':
            cmd_listar()

        elif resp == '2':
            codigo = input("Código: ").strip()
            if not codigo:
                print("Código é obrigatório.")
                continue
            nome = input("Nome (opcional): ").strip()
            preco_input = input("Preço (opcional): ").strip()
            quantidade_input = input("Quantidade (opcional): ").strip()

            preco = None
            quantidade = None
            if preco_input:
                try:
                    preco = float(preco_input)
                except ValueError:
                    print("Entrada inválida para preço. Operação cancelada.")
                    continue
            if quantidade_input:
                try:
                    quantidade = int(quantidade_input)
                except ValueError:
                    print("Entrada inválida para quantidade. Operação cancelada.")
                    continue

            cmd_criar(codigo, nome if nome else None, preco, quantidade)

        elif resp == '3':
            codigo = input("Código do produto a buscar: ").strip()
            if not codigo:
                print("Código é obrigatório.")
                continue
            cmd_buscar(codigo)

        elif resp == '4':
            codigo = input("Código do produto a atualizar: ").strip()
            if not codigo:
                print("Código é obrigatório.")
                continue
            nome = input("Novo nome (deixe vazio para não alterar): ").strip()
            preco_input = input("Novo preço (deixe vazio para não alterar): ").strip()
            quantidade_input = input("Nova quantidade (deixe vazio para não alterar): ").strip()

            preco = None
            quantidade = None
            if preco_input:
                try:
                    preco = float(preco_input)
                except ValueError:
                    print("Entrada inválida para preço. Operação cancelada.")
                    continue
            if quantidade_input:
                try:
                    quantidade = int(quantidade_input)
                except ValueError:
                    print("Entrada inválida para quantidade. Operação cancelada.")
                    continue

            cmd_atualizar(codigo, nome if nome else None, preco, quantidade)

        elif resp == '5':
            codigo = input("Código do produto a apagar: ").strip()
            if not codigo:
                print("Código é obrigatório.")
                continue
            confirmar = input(f"Confirma apagar o produto '{codigo}'? (s/N): ").strip().lower()
            if confirmar == 's' or confirmar == 'y':
                cmd_apagar(codigo)
            else:
                print("Operação cancelada.")

        elif resp == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
