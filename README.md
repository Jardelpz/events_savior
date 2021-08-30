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


Send a post request to *http://localhost:5001/register/{state}* and you should see the result like on next step below:


## Expected Result

Request:
![Request](https://user-images.githubusercontent.com/32064166/131373278-95d8c7da-24eb-47ee-8c9c-db90015c6f14.png)

APM
![APM](https://user-images.githubusercontent.com/32064166/131372368-2b1ceeee-272f-4e02-b5ee-df6a4bad2a8c.png)

![APM](https://user-images.githubusercontent.com/32064166/131372383-1aee2841-d957-4349-8cc6-a1bddc3b3ec2.png)

Kibana
![Kibana](https://user-images.githubusercontent.com/32064166/131372389-d25a3c64-2308-42a1-94f2-546eb1011045.png)

RabbitMQ
![RabbitMQ](https://user-images.githubusercontent.com/32064166/131372409-6a8d40d4-8e08-4eb3-872d-ad3b3ed039de.png)
