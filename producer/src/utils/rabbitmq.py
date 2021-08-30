import pika
import json


def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq_p'))
    channel = connection.channel()
    channel.queue_declare(queue='city')
    channel.basic_publish(exchange='', routing_key='city', body=json.dumps(message))
    connection.close()

