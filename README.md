# API_assincrona - Como utilizar

### Virtual Environment
Primeiramente, é necessario criar um ambiente virtual, para tal, utilize o comando:

```sh
$ python3 -m venv <myenvname>
```
A versão utilizada foi o python 3.9, logo, para evitar possiveis erros de compatibilidade, sugiro a utlização da mesma versão.
Em Seguida, ative seu ambiente virtual com o comando:

```sh
$ source <myenvname>/bin/activate
```
### Requirements
Para instalar os requirements do projeto, vá até a pasta raiz e digite:

```sh
$ pip install -r requirements.txt
```

### Database
O banco de dados utilizado foi o Postgres, com user e senha padrãoo(postgres).
Basta criar um banco de dados com o nome api_DB e utilizar a porta padrão da aplicação(5432).
Para criar as tabelas no banco, utilize a sequencia:

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
### REDIS
Utilizamos o REDIS pra fazer o gerenciamento das filas de tarefas.
Primeiramente instale a aplicação, em seguida roda o comando:

```sh
$ redis-server
```
Para verificar se o REDIS está pronto para uso, digite num novo terminal:
```sh
$ redis-cli ping
```
Se a resposta for PONG, o servidor do REDIS está ponto para gerenciar filas.

### Celery
Utilizamos o Celery para realizar tarefas assincronas.
Após a instalação do celery, na pasta raiz do projeto, abra um novo terminal e digite o comando:

```sh
$ celery -A setup worker --loglevel=info
```
Onde setup é o nome do projeto. Esse comando inicializará um worker, que utilizará o numero de threads disponiveis no pc utilizado.

Finalmente, para rodar o servidor do projeto, basta digitar:
```sh
$ python manage.py runserver
```


### API
Para navegar pela API, acesse o endpoint:
```sh
http://localhost:8000
```

Antes de utilizar as features do sistema, é necessário cadastrar-se. Para tal, acesse o endpoint:
```sh
http://localhost:8000/clientes
```
Esse mesmo endpoint permite visualizar todos os clientes cadastrados no sistema.

Para visualizar as informações de um cliente especifico acesse:
```sh
http://localhost:8000/clientes/<cliente_id>
```

Para pedir um emprestimo, acesse:
```sh
http://localhost:8000/clientes/<cliente_id>/emprestar
```
Após informado o valor do emprestimo, um ticket será gerado, informando se o emprestimo poderá ou não ser realizado.

Para consultar seu ticket:
```sh
http://localhost:8000/clientes/<cliente_id>/consultar/<numero_do_ticket>
```

Para consultar todos os tickets gerados por um cliente:
```sh
http://localhost:8000/clientes/<cliente_id>/consultar/
```
### Documentação da API:
Utilizamos o Swagger para realizar a documentação da API.
Para acessá-la, digite no navegador:

```sh
http://localhost:8000/swagger
```

### Docker:
Para rodar o projeto diretamente de um container, com o docker e docker-compose instalados
, acesse a pasta raiz do projeto e digite:

```sh
$ docker-compose up --force-recreate
```
E acesse seu navegador no endereço:

```sh
http://localhost:8000/
```

Obrigado!