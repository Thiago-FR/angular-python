
---

# BRAVi - Angular - Python <a name="boas-vindas-ao-repositório"></a>

---

# Sumário

- [Angular - Python](#boas-vindas-ao-repositório)
- [O que foi desenvolvido](#o-que-foi-desenvolvido)
- [Conexão com o Banco](#conexao-db)
  - [Conexão local](#conexao-local)
- [Para testar o projeto](#testar-o-projeto)
  - [Rodar API FULLSTACK por docker](#via-docker-fullstack)
  - [Rodar API Local](#via-local)
- [Testes desenvolvidos](#tdd)
  - [Testes](#tdd-1)
- [Endpoint's](#endpoint)
  - [Para criar Tarefa POST](#user-post)
  - [Para buscar Tarefas GET](#user-get)
  - [Para atualizar Tarefa por ID PUT](#user-put)
  - [Para deletar Tarefa por ID DELETE](#user-delete)

---

## O que foi desenvolvido: <a name="o-que-foi-desenvolvido"></a>

  Foi desenvolvido aplicação fullstack com angular e python.

  Os usuários são inseridos em um banco de dados **MongoDB** sendo possível modelar os dados através do **pymongo**

  É possível:
   - Adicionar usuário
   - Remover usuário
   - Atualizar usuário

---

### Conexão com o Banco: <a name="conexao-db"></a>

#### Conexão local <a name="conexao-local"></a>

**⚠️ IMPORTANTE! ⚠️**

Para conexão local é necessário ter instalado localmente o **MongoDB**

Essa API utiliza as seguintes variáveis de ambiente:

```sh
FLASK_APP=app/app.py
FLASK_DEBUG=1
MONGO_URI="mongodb://localhost:27017/db"
```

---

## Para testar o projeto: <a name="testar-o-projeto"></a>

1. Clone o repositório:
  * `git@github.com:Thiago-FR/angular-python.git`.
  * Entre na pasta do repositório que você acabou de clonar


### Rodar APP FULLSTACK por docker <a name="via-docker-fullstack"></a>

1. API via Docker [**É Necessário ter o docker-compose v1.29 instalado!**]
  * Na raiz do projeto rode o comando:
  * `docker-compose up -d --build`

2. Ao final da containerização você pode checar o container **app_backend** :
  * `docker ps`

3. Para descer os container basta rodar:
  * `docker-compose down --remove-orphans`


### Rodar API Local <a name="via-local"></a>
1. Acessar a pasta backend

2. Instalar as dependências:
  * `python3 -m pip install --upgrade pip`
  * `python3 -m venv .venv && source .venv/bin/activate`
  * `python3 -m pip install -r requirements.txt`

3. Iniciar o Banco de dados
  * `docker-compose up -d --build`

4. Iniciar servidor:
  * `flask run`

Obs: Este projeto utiliza variáveis de ambiente veja - [Conexão com o Banco](#conexao-db)

---

## Testes desenvolvidos: <a name="tdd"></a>

Foi realizado alguns teste unitários na camada Model e Service.

### Testes <a name="tdd-1"></a>

1. Após instalar as dependências rode o comando:
  * `pytest tests/ -v`

---

## Endpoint's <a name="endpoint"></a>

### Para criar Tarefa POST <a name="user-post"></a>

* Endpoint: `/api/v1/user`

Body
```json
  { 

  }
 ```

Reponse
```json
  {
    "message": {

    }
  }
```
---

### Para buscar Usuários GET <a name="user-get"></a>

* Endpoint: `/api/user`

```json
  [
    {

    },
    ...
  ]
```
---

### Para atualizar Usuário por ID PUT <a name="user-put"></a>

* Endpoint: `/api/user/<id>`

Body
```json
  {

  }
```
---

### Para deletar Usuário por ID DELETE <a name="user-delete"></a>

* Endpoint: `/api/user/<id>`

---
