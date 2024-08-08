# Catálogo de Produtos - Microserviço

Este repositório contém a implementação de um microserviço de Catálogo de Produtos, utilizando Python com Flask e Docker, seguindo os princípios da arquitetura hexagonal.

## Funcionalidades

- Listar produtos
- Adicionar novos produtos
- Atualizar produtos existentes
- Remover produtos

## Tecnologias Utilizadas

- Python
- Flask
- Docker
- PostgreSQL

## Instalação e Configuração

### Pré-requisitos

- Python 3.12+
- Docker e Docker Compose
- Git (para clonagem do repositório)

### Clonagem do Repositório

```bash
git clone https://github.com/itallonet/dm-test-ecommerce-product-catalog.git
cd dm-test-ecommerce-product-catalog
```

### Configuração do Ambiente

```bash
python -m venv venv
source venv/bin/activate  # Para Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Uso do Docker Compose
Para iniciar o serviço juntamente com o PostgreSQL:

```bash
docker-compose up --build
```

O serviço estará disponível em http://localhost:5000.

## Testes

```bash
py -m pytest
```

## Teste HTTP

```bash
curl --request GET \
  --url http://localhost:5000/products/1 \
  --header 'User-Agent: insomnia/9.3.2'
```