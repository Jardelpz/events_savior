import logging
import requests

from flask_restful import Resource
from datetime import datetime

from src.utils.redis import save_cache, get_from_cache
from src.utils.elasticsearch import ESManager
from src.utils.apm import apm
from src.utils.rabbitmq import send_message


class RegisterCities(Resource):

    @staticmethod
    def get(state):
        return {'status': 'OK'}

    @staticmethod
    def post(state):
        if cities := get_from_cache(state):
            logging.info('cities founded was cached!')
            return cities

        response = requests.get(f'http://educacao.dadosabertosbr.com/api/cidades/{state}')
        if not response.status_code == 200:
            apm.capture_message(f"{state} not found")
            return

        payload = []
        for city in response.json():
            message = {
                "city": city.split(':')[-1].title(),
                "population": int(city.split(':')[0]),
                "state": state,
                "event_date": datetime.now().isoformat()
            }

            payload.append(message)
            send_message(message)

        save_cache(state, payload)
        return payload


class Cities(Resource):

    @staticmethod
    def delete(city):
        info = ESManager().es_client.delete(index='cities', doc_type='city_doc', id=city)
        return f"{city} deleted: {info}"

    @staticmethod
    def get(city):
        elastic = ESManager()
        resp = elastic.es_client.search(body={"from": 0, "size": 10000, "query": {"match": {"city": f"{city}"}}},
                                         index='cities', doc_type='city_doc')

        payload = []
        for hit in resp.get('hits').get('hits'):
            payload.append(hit)

        return payload
