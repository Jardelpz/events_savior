# Events Savior

Este projeto consiste em uma demonstração do armazenamento de eventos em uma aplicação.


## Tecnologias

* RabbitMQ
* Redis
* ElasticSearch
* APM
* Kibana
* Flask


## How it works

O producer recebe uma tarefa de buscar todas cidades de um estado, além de salvar isso em cache,
envia para uma fila RabbitMQ, chamada *city*. 


De outro lado, temos um simples consumidor dessa fila, trabalhando apenas com um worker, consumindo a mensagem e salvando as informação no Elastic.


## Environment

Este projeto consiste em dois microserviços atuando dentro de uma mesma network

Para Rodar o projeto, neste sentido, é preciso criar um network localmente: 


    docker network create elastic_t

Entrar nos dois diretórios (producer e consumer) e iniciar os seus respectivos docker-compose: 
    
    make docker_run


