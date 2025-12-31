# Gerenciador de Produtos em Python

Este projeto implementa um sistema de gerenciamento de produtos, utilizando Python com três formas de interação:

* **CLI (linha de comando interativa)**
* **Web Service HTTP (API REST simples)**
* **Cliente HTTP usando `requests`**

Os dados são mantidos **em memória**, sendo ideais para fins **didáticos**, estudos de **POO** e **comunicação cliente-servidor**.

---

## Estrutura do Projeto

```
.
├── provider/
│   ├── __init__.py
│   ├── produto.py         # Entidade/Modelo (Product entity)
│   └── produto_service.py # Camada de negócio (Business logic layer)
├── client.py              # Cliente HTTP (HTTP client)
├── cli.py                 # Interface CLI (Command-line interface)
├── ws_provider.py         # Servidor API REST (REST API server)
├── test_produto.py        # Testes unitários (Unit tests)
├── popular_produtos.py    # Script de população (Data seeding script)
├── .gitignore
└── README.md
```

---

## Descrição dos Arquivos

### `produto.py`

Define a classe **Produto**, que representa um item do inventário.

**Atributos:**

* `codigo` (obrigatório)
* `nome`
* `preco`
* `quantidade`

Inclui validações, getters/setters e conversão para dicionário.

---

### 📄 `produto_service.py`

Responsável pela **regra de negócio** e gerenciamento dos produtos em memória.

Funcionalidades:

* Criar produto
* Buscar por código
* Atualizar dados
* Apagar produto
* Listar todos

Aplica validações e evita duplicação de códigos.

---

### 📄 `cli.py`

Interface **interativa em terminal**, permitindo que o usuário gerencie produtos via menu.

Funcionalidades disponíveis:

1. Listar produtos
2. Criar produto
3. Buscar produto
4. Atualizar produto
5. Apagar produto

---

### `ws_provider.py`

Implementa um **servidor HTTP** usando `http.server`.

Endpoints disponíveis:

| Método | Endpoint               | Descrição                |
| ------ | ---------------------- | ------------------------ |
| GET    | `/produtos`            | Lista todos os produtos  |
| GET    | `/produtos?codigo=XXX` | Busca produto por código |
| POST   | `/produtos`            | Cria um novo produto     |
| PUT    | `/produtos`            | Atualiza um produto      |
| DELETE | `/produtos?codigo=XXX` | Remove um produto        |

Servidor roda em:

```
http://127.0.0.1:8081
```

---

### `client.py`

Cliente HTTP que consome a API usando a biblioteca `requests`.

Permite:

* Criar produto
* Buscar produto
* Atualizar produto
* Apagar produto
* Listar produtos

---

### Pré-requisitos

```bash
# Python 3.8 ou superior
python --version

# Instalar biblioteca requests
pip install requests
```

---

### Fluxo de execução recomendado

#### **Passo 1: Executar testes**

Validar implementação antes de usar:

```bash
python test_produto.py
```

Aguarde confirmação: `Total: 3/3 passaram`

---

#### **Passo 2: Iniciar servidor API**

**Terminal 1:**
```bash
python ws_provider.py
```

**Saída esperada:**
```
Servidor iniciado em http://127.0.0.1:8081
```

⚠️ **Mantenha este terminal aberto!**

---

#### **Passo 3: Testar no navegador**

Acesse: `http://127.0.0.1:8081/produtos`

Você verá a lista de produtos em JSON.

---

#### **Passo 4: Usar cliente HTTP (opcional)**

**Terminal 2:**
```bash
python client.py
```

Edite o arquivo para testar operações específicas. Por padrão ele vai criar uma lista de produtos que será exibido em: `http://127.0.0.1:8081/produtos` 
(OBS: recomenda-se dar F5 para atualizar a pagina apos rodar client.py) 

---

#### **Passo 5: Usar CLI (alternativa)**

**Terminal 2:**
```bash
python cli.py
```

⚠️ **Atenção:** CLI usa instância separada do service (dados não compartilhados com API).

---

## Objetivo Educacional

Este projeto é indicado para:

* Estudo de **Programação Orientada a Objetos**
* Separação de responsabilidades (Model / Service / Interface)
* Noções de **API REST**
* Comunicação cliente-servidor
* Validação de dados e tratamento de erros

---

## Observações

* Os dados perdem-se ao encerrar o programa.
* Projeto voltado para aprendizado.

---

## Autores
Daniel Soares

Lana Ramos

Maycon Vyctor

Samuel Fogaça

---
Desenvolvido para fins acadêmicos e didáticos

