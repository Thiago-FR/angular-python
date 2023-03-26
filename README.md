
---

# BRAVi - Angular - Python <a name="boas-vindas-ao-repositório"></a>

---

# Sumário

- [Angular - Python](#boas-vindas-ao-repositório)
- [O que foi desenvolvido](#o-que-foi-desenvolvido)
- [Para testar o projeto](#testar-o-projeto)
  - [Rodar API FULLSTACK por docker](#via-docker-fullstack)
  - [Deploy](#deploy)

---

## O que foi desenvolvido: <a name="o-que-foi-desenvolvido"></a>

  Foi desenvolvido aplicação fullstack com angular e python.

  Os usuários são inseridos em um banco de dados **MongoDB** sendo possível modelar os dados através do **pymongo**

  É possível:
   - Adicionar usuário
   - Remover usuário
   - Atualizar usuário

---

## Para testar o projeto: <a name="testar-o-projeto"></a>

1. Clone o repositório:
  * `git@github.com:Thiago-FR/angular-python.git`.
  * Entre na pasta do repositório que você acabou de clonar


### Rodar APP FULLSTACK com docker <a name="via-docker-fullstack"></a>

1. API via Docker [**É Necessário ter o docker-compose v1.29 instalado!**]
  * Na raiz do projeto rode o comando:
  * `docker-compose up -d --build`

2. Ao final da containerização você pode checar o container **app_backend** :
  * `docker ps`

3. Para descer os container basta rodar:
  * `docker-compose down --remove-orphans`

### Deploy <a name="via-local"></a>
Acessar: [LINK](https://angular-python.vercel.app/)