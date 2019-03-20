"""
Defines the blueprint for the apartments
"""
from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS
from resources import ApartmentResource, ApartmentItemResource, ApartmentLocationResource


APARTMENT_BLUEPRINT = Blueprint('apartment', __name__)

Api(APARTMENT_BLUEPRINT).add_resource(
    ApartmentResource,
    '/apartment/'
)

Api(APARTMENT_BLUEPRINT).add_resource(
    ApartmentItemResource,
    '/apartment/<int:id>'
)

# http://127.0.0.1:5000/api/location/25.135215846202197/60.586950699999996/5.1
Api(APARTMENT_BLUEPRINT).add_resource(
    ApartmentLocationResource,
    '/location/<float:latitude>/<float:longitude>/<float:km>'
)
