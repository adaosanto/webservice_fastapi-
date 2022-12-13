
# Webservice FastAPI

Webservice construido com FastAPI e SQLAlchemy, com autenticação pronto para deploy.


## Configurando

- Banco de Daaods
```
  Altere a variável DB_URL no arquivo /core/config.py.
```

- Gerando o JWT Secrets

```python
import secrets
token: str = secrets.token_urlsafe(32)
```
- JWT Secrets
```
  Altere a variável JWT_SECRET no arquivo /core/config.py.
```
## Documentação da API

#### Retorna todos os artigos cadastrados

```http
  GET /api/v1/artigos
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |

#### Retorna um artigo

```http
  GET /api/v1/artigos/${artigo_id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |


## Documentação completa

[Documentação](https://fastapi.mapstecnologia.com/docs)


## Autores

- [@adaosantos](https://github.com/adaosanto)


## Screenshots

![Projeto Deploy](https://i.ibb.co/njxWS6s/download-3.png)
![GET Artigos](https://i.ibb.co/1GMb1CN/download.png)
## Deploy

Para fazer o deploy desse projeto rode

```bash
  gunicorn main:app -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker -w 4 --graceful-timeout 0 --access-logfile app_log
```

