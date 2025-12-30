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
├── client.py              # Cliente HTTP para consumir a API
├── cli.py                 # Interface de linha de comando
├── ws_provider.py         # Servidor HTTP (API REST)
└── provider/
    ├── produto.py         # Classe Produto (modelo)
    └── produto_service.py # Serviço de regras de negócio
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

## Como Executar

### 1️ Executar o servidor web

```bash
python ws_provider.py
```

---

### 2️ Usar o cliente HTTP

```bash
python client.py
```

---

### 3️ Usar a interface CLI

```bash
python cli.py
```

---

## Requisitos

* Python 3.8+
* Biblioteca `requests`

Instalação:

```bash
pip install requests
```

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

Maycon Victor

Samuel Fogaça

---
Desenvolvido para fins acadêmicos e didáticos

