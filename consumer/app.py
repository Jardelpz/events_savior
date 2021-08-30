import pika
import sys
import os
import json
import logging

from src.handlers.consume import process_message


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq_p'))
    channel = connection.channel()

    channel.queue_declare(queue='city')

    def callback(ch, method, properties, body):
        logging.info(f'Message received: f{body}')
        message = json.loads(body)
        process_message(message)

    channel.basic_consume(queue='city', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)