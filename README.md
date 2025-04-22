
# 🏛️ Olimpíada de Programação Nova Roma

Bem-vindo à **Olimpíada de Programação Nova Roma** — um desafio criado para testar suas habilidades de desenvolvimento, depuração e pensamento crítico!

## 📜 Contexto

Você acaba de ser contratado como desenvolvedor júnior na empresa fictícia **Nova Roma Systems**. Seu primeiro trabalho não é criar um sistema do zero, mas sim **corrigir e aprimorar o sistema que estava sendo desenvolvido pelo antigo estagiário**, que deixou o código incompleto, com várias falhas de lógica, estrutura e segurança.

Seu desafio é identificar os erros, propor soluções e deixar o sistema pronto para produção. Boa sorte!

## ⚙️ Sobre o projeto

Este projeto é uma API REST desenvolvida com **FastAPI** e persistência em **SQLite**, contendo funcionalidades relacionadas a:

- Cadastro e listagem de **clientes**.
- Consulta de **pagamentos**.
- Simulação de lucro com criptomoedas (utiliza dados da API do Mercado Bitcoin).

## Requisitos

- Docker (recomendado)
- Python 3.10+ (alternativa sem Docker)

## Como rodar com Docker

```bash
docker build -t desafio-api .
docker run -d -p 8000:8000 desafio-api
```

A API estará disponível em `http://localhost:8000`

A arquitetura segue o padrão de separação por domínio, com os seguintes diretórios:

  

```

app/

├── controllers/ # Rotas e endpoints

├── models.py # ORM com SQLAlchemy

├── database.py # Conexão com banco SQLite

└── main.py # Ponto de entrada da aplicação

tests/

└── test_main.py # Casos de teste (pytest)

```

  

---

## 🧪 Rodar testes

```bash
docker run --rm desafio-api pytest
```

## 🎯 Critérios de Avaliação
  

| Critério | Peso |
|------------------------------------|------|
| Correção dos erros principais | 🟩🟩🟩🟩 |
| Qualidade dos testes | 🟩🟩🟩 |
| Clareza e organização do código | 🟩🟩🟩 |
| Uso correto do Git | 🟩🟩 |
| Criatividade (melhorias extras) | 🟩 |
