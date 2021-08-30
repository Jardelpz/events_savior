from flask_restful import Api

from src.handlers.city_of_country import RegisterCities, Cities


def make_resources(app):
    api = Api()
    api.add_resource(RegisterCities, "/register/<state>")
    api.add_resource(Cities, "/city/<city>")
    api.init_app(app)
