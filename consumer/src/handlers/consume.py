from src.utils.elasticsearch import ESManager


def process_message(message):
    ESManager().es_client.index(index='cities', doc_type='city_type', body=message, id=message['city'])
