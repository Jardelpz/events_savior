import logging
from elasticsearch import Elasticsearch


class ESManager:

    def __init__(self):
        self.es_client = Elasticsearch(["http://elasticsearch_p:9200"])
        logging.warning(f'{self.es_client.info()}')
