![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?logo=flask)
![REST API](https://img.shields.io/badge/API-REST-blue)
![CRUD](https://img.shields.io/badge/CRUD-MongoDB-success)
![MongoDB Atlas](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb)
![Postman](https://img.shields.io/badge/Postman-API%20Client-orange?logo=postman)



# Documentação Técnica - API CRUD com Flask + MongoDB Atlas

## Visão Geral

Este projeto consiste no desenvolvimento de uma API REST utilizando **Python**, **Flask** e **MongoDB Atlas**, com o objetivo de realizar operações de **CRUD** sobre coleções de dados, permitindo criar, consultar, atualizar e remover registros de forma estruturada.

A aplicação foi construída com foco em aprendizado prático de conceitos fundamentais de backend, integração com banco NoSQL, organização modular com rotas separadas e testes de endpoints via Postman.

Atualmente, o projeto contempla operações sobre coleções como:

* `carros`
* `posts`

Além da implementação funcional das rotas, o projeto também inclui uma coleção do Postman para testes e validações manuais da API.

---

## Objetivo do Projeto

O principal objetivo deste projeto é demonstrar, na prática, a construção de uma API backend conectada a um banco de dados em nuvem, permitindo:

* conexão com o MongoDB Atlas;
* estruturação de uma API REST com Flask;
* manipulação de documentos em coleções MongoDB;
* aplicação das operações básicas de CRUD;
* testes de endpoints com Postman;
* organização do projeto de forma modular e próxima de um ambiente profissional.

---

## Tecnologias Utilizadas

* **Python** — linguagem principal do projeto;
* **Flask** — microframework utilizado para construção da API;
* **MongoDB Atlas** — banco de dados NoSQL em nuvem;
* **PyMongo** — driver Python para comunicação com o MongoDB;
* **Postman** — ferramenta utilizada para testes das requisições HTTP;
* **VS Code** — ambiente de desenvolvimento.

---

## Arquitetura do Projeto

A aplicação foi organizada em uma estrutura modular, separando responsabilidades entre inicialização da aplicação, conexão com banco de dados, rotas e testes.

```text
project_api/
│
├── docs/
├── src/
│    ├── database/
│    │      └── connection.py
│    │
│    ├── routes/
│    │      ├── carros.py
│    │      └── posts.py
|    |── postman/
│           └── carros.postman_collection.json
│
├── tests/
│
├── app.py
└── README.md
└── requirements.txt
```

### Descrição dos diretórios

* **`app.py`**: ponto de entrada da aplicação Flask e registro dos blueprints.
* **`src/database/connection.py`**: responsável por estabelecer conexão com o MongoDB Atlas.
* **`src/routes/`**: contém as rotas da API separadas por entidade.
* **`tests/`**: scripts auxiliares para testes de conexão, leitura e validação.
* **`postman/`**: coleção exportada do Postman com os endpoints da API.

---

## Funcionamento da API

A API segue o padrão REST, utilizando os métodos HTTP principais:

* **GET** → consultar dados;
* **POST** → criar novos registros;
* **PUT** → atualizar registros existentes;
* **DELETE** → remover registros.

> Cada coleção possui endpoints específicos para manipulação de seus documentos.

---

## Banco de Dados

O banco utilizado é o **MongoDB Atlas**, acessado remotamente por meio de uma string de conexão configurada no projeto.

O MongoDB foi escolhido por sua flexibilidade na manipulação de documentos JSON-like, o que facilita a modelagem inicial e o aprendizado de operações CRUD em aplicações backend.

### Coleções utilizadas:
#### Carros

Exemplo lógico de documento:

```json
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2024
}
```

#### Posts:

Exemplo lógico de documento:

```json
{
  "author": "Daniel",
  "text": "My first mongodb application based on Python",
  "tags": ["mongodb", "python3", "pymongo"],
  "date": "2026-03-07T20:04:23.173000"
}
```

### Observação sobre o `_id`

No MongoDB, cada documento recebe automaticamente um campo `_id`, do tipo `ObjectId`. Na API, esse valor é convertido para string e retornado como `id` nas respostas JSON.

---

## Endpoints Disponíveis

### Carros

| Método | Endpoint       | Descrição                   |
| ------ | -------------- | --------------------------- |
| GET    | `/carros`      | Lista todos os carros       |
| GET    | `/carros/<id>` | Busca um carro por ID       |
| POST   | `/carros`      | Cria um novo carro          |
| PUT    | `/carros/<id>` | Atualiza um carro existente |
| DELETE | `/carros/<id>` | Remove um carro             |

### Posts

| Método | Endpoint      | Descrição                  |
| ------ | ------------- | -------------------------- |
| GET    | `/posts`      | Lista todos os posts       |
| GET    | `/posts/<id>` | Busca um post por ID       |
| POST   | `/posts`      | Cria um novo post          |
| PUT    | `/posts/<id>` | Atualiza um post existente |
| DELETE | `/posts/<id>` | Remove um post             |

---

## Exemplo de Uso dos Endpoints

### Exemplo — Criar post

**Requisição**

```http
POST /posts
Content-Type: application/json
```

```json
{
  "author": "Daniel",
  "text": "API Flask com MongoDB",
  "tags": ["flask", "mongodb", "api"]
}
```

**Resposta esperada**

```json
{
  "msg": "Post criado com sucesso"
}
```

### Exemplo — Atualizar post

**Requisição**

```http
PUT /posts/<id>
Content-Type: application/json
```

```json
{
  "author": "Daniel",
  "text": "Post atualizado com sucesso",
  "tags": ["mongodb", "flask", "api"]
}
```

### Exemplo — Deletar post

**Requisição**

```http
DELETE /posts/<id>
```

**Resposta esperada**

```json
{
  "msg": "Post deletado com sucesso"
}
```

---

## Testes com Postman

Os testes dos endpoints foram realizados com o **Postman**, permitindo validar:

* criação de documentos;
* consulta de listas e itens por ID;
* atualização de documentos existentes;
* exclusão de registros;
* tratamento de erros para IDs inválidos ou inexistentes.

A coleção exportada foi salva dentro do projeto no diretório:

```text
/postman/api_collection.json
```

Isso permite compartilhar os testes junto com o código-fonte e reutilizar as requisições em outros ambientes.

---

## Tratamento de Erros

A API contempla validações importantes para melhorar a confiabilidade das rotas, como:

* validação de `ObjectId`;
* retorno `400 Bad Request` para IDs inválidos;
* retorno `404 Not Found` quando o documento não existe;
* retorno de mensagens JSON descritivas para facilitar testes e depuração.

Exemplo:

```json
{
  "erro": "ID inválido"
}
```

---

## Aprendizados Desenvolvidos

Durante a construção do projeto, foram consolidados conhecimentos em:

* criação de APIs REST com Flask;
* organização modular com Blueprints;
* conexão e manipulação de dados em MongoDB Atlas;
* uso do PyMongo para operações CRUD;
* utilização de `ObjectId` em rotas dinâmicas;
* testes práticos de API com Postman;
* estruturação inicial de documentação técnica para portfólio.

---

## Melhorias Futuras

Como evolução natural do projeto, podem ser implementadas as seguintes melhorias:

* documentação interativa com Swagger/OpenAPI;
* separação em camadas `routes`, `services` e `models`;
* criação de testes automatizados;
* deploy da API em ambiente cloud;
* autenticação e autorização de usuários.

---

## Conclusão

Este projeto representa a implementação de uma API CRUD funcional com Flask e MongoDB Atlas, cobrindo desde a conexão com o banco de dados até a exposição de endpoints REST testáveis via Postman.

Além de cumprir o objetivo técnico de manipulação de coleções NoSQL, o projeto também estabelece uma base sólida para evolução futura, aproximando sua estrutura de padrões mais profissionais de desenvolvimento backend.

---

## Arquitetura Visual

O projeto foi desenvolvido para atender a uma necessidade de modernização no fluxo de gerenciamento de dados de uma aplicação.
Antes, o processo não possuía uma interface centralizada para operações de cadastro, consulta, atualização e remoção, o que dificultava a manutenção e a escalabilidade da solução.

Como resposta a esse problema, foi construída uma API REST em Flask, organizada de forma modular com Blueprints, utilizando PyMongo para integração com o MongoDB Atlas, responsável pelo armazenamento em nuvem dos dados.
O desenvolvimento foi realizado em VS Code, enquanto os testes das rotas foram conduzidos com Postman.

Fluxo da solução: 

```
  Sistema Consumidor
           │
           ▼
        API REST
        (Flask)
           │
           ▼
    Camada de Rotas
   (Blueprints Flask)
           │
           ▼
  MongoDB Atlas Cloud
```

![Diagrama do projeto:](docs\arquitetura_project_mongo_2.png)


## 👤 Autor

**Daniel Martins França**  

---

## 📬 Contato:

- 📧 Email: [f.daniel.m@gmail.com](mailto:f.daniel.m@gmail.com)  
- 💼 LinkedIn: [www.linkedin.com/in/danixdev](https://www.linkedin.com/in/danixdev)  


