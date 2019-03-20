from flask_restful import Resource
from flask.json import jsonify
from repositories import ApartmentRepository, ApartmentItemRepository, ApartmentLocationRepository


class ApartmentResource(Resource):
    """ Verbs relative to the ApartmentResource """

    @staticmethod
    def get():
        """ Return a list of apartments"""
        apartments = ApartmentRepository.get()
        apartment_json = [ob.json for ob in apartments]
        return jsonify({'apartments': apartment_json})


class ApartmentItemResource(Resource):
    """ Verbs relative to the ApartmentItemResource """

    @staticmethod
    def get(id):
        """ Return an apartment key information based on the id """
        apartment = ApartmentItemRepository.get(id)
        return jsonify({'apartment': apartment.json})


class ApartmentLocationResource(Resource):
    """ Verbs relative to the ApartmentLocation """

    @staticmethod
    def get(longitude, latitude, km):
        """ Return list of apartments based on longitude, latitude and and radius """
        apartments, price_sqm, living_area_sqm = ApartmentLocationRepository.get(longitude, latitude, km)
        return ({'livingAreaSqmMean': round(living_area_sqm, 2),
                'priceSqmMean': round(price_sqm, 2), 'apartments': apartments})
