# Events Savior

This project consists of a demonstration of event storage in an application.


## Technologies

* RabbitMQ
* Redis
* ElasticSearch
* APM
* Kibana
* Flask


## How it works

The producer receives a task to fetch all cities in a state, in addition to saving this in cache, sends it to a RabbitMQ queue, called *city*.

On the other hand, we have a simple consumer of this queue, working only with a worker, consuming the messages and saving the information in Elastic.


## Environment

This project consists of two microservices acting within the same network

In order to Run the project, in this sense, it is necessary to create a network locally:


    docker network create elastic_t

Enter the two directories (producer and consumer) and start their respective docker-compose:
    
    make docker_run


