# ITFlex
---------------

## Back-end
### Executando Aplicação

1. Criaçao do Venv
~~~
python -m venv venv
~~~
2. Acessando o ambiente do venv
~~~
source venv/bin/activate
~~~
3. Executando a aplicação
~~~
flask run
~~~
4. Port
~~~
http://localhost:5000/
~~~


### End Points
* ## Cadastro Certificados
~~~
http://localhost:5000/api/create
~~~
### Enviado
~~~
{
    "username":"Joazinho12",
    "name":"Joao Antonio",
    "description":"",
    "expiration":10,
    "expirated_at":"25/08/2021",
    "created_at":"25/08/2021",
    "updated_at":"25/08/2021",
	"groups":1
}
~~~
### Recebido
~~~
{
    "created_at": "Wed, 25 Aug 2021 00:00:00 GMT",
    "description": "",
    "expirated_at": "Wed, 25 Aug 2021 00:00:00 GMT",
    "expiration": 10,
    "groups": 1,
    "id": 10,
    "name": "Joao Antonio",
    "updated_at": "Wed, 25 Aug 2021 00:00:00 GMT",
    "username": "Joazinho12"
}
~~~

* ## Cadastro Grupos
~~~
http://localhost:5000/api/groups
~~~

### Enviado
~~~
{
    "cod":1,
    "name":"ADM"
}
~~~
### Recebido
~~~
{
    "cod":1,
    "name":"ADM"
}
~~~


* ## Listagem
~~~
http://localhost:5000/api/list
~~~

### Recebido
~~~
{
    [
        {
            "created_at": "Wed, 25 Aug 2021 00:00:00 GMT",
            "description": "",
            "expirated_at": "Wed, 25 Aug 2021 00:00:00 GMT",
            "expiration": 10,
            "groups": 1,
            "id": 10,
            "name": "Joao Antonio",
            "updated_at": "Wed, 25 Aug 2021 00:00:00 GMT",
            "username": "Joazinho12"
        },
        {
            "created_at": "Wed, 25 Aug 2021 00:00:00 GMT",
            "description": "bruninho",
            "expirated_at": "Wed, 25 Aug 2021 00:00:00 GMT",
            "expiration": 10,
            "groups": 1,
            "id": 8,
            "name": "bruninho",
            "updated_at": "Wed, 25 Aug 2021 00:00:00 GMT",
            "username": "bruninho"
        }
    ]
    
}
~~~


* ## Deletar
~~~
http://localhost:5000/api/delete/7
~~~


* ## Atualizar
~~~
http://localhost:5000/api/update/8
~~~
### Enviado
~~~
{
	"username":"bruninho",
    "name":"bruninho",
    "description":"bruninho"
}
~~~
### Recebido
~~~
{
    "created_at": "Wed, 25 Aug 2021 00:00:00 GMT",
    "description": "bruninho",
    "expirated_at": "Wed, 25 Aug 2021 00:00:00 GMT",
    "expiration": 10,
    "groups": 1,
    "id": 8,
    "name": "bruninho",
    "updated_at": "Wed, 25 Aug 2021 00:00:00 GMT",
    "username": "bruninho"
}
~~~

### Variavies de Ambiente
* SQLALCHEMY_DATABASE_URI='bancoDeDados://username:senha@localhost:portaDoBancod/nomeDoBanco'

## Front-end
### Executando Aplicação

1. Rodando aplicação
~~~
npm run serve
~~~
2. Acessar/Port
~~~
http://localhost:8080/
~~~