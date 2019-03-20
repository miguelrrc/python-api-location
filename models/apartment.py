"""
Define the Apartment model
"""
from sqlalchemy.ext.declarative import declarative_base
from . import db
from sqlalchemy import inspect
Base = declarative_base()


class Apartment(Base):

    to_json_filter = ()

    """Model for the Apartment table"""
    __tablename__ = 'apartment'

    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    price_sqm = db.Column(db.Numeric(7, 2))
    living_area_sqm = db.Column(db.Numeric(10, 1))

    def __init__(self, longitude, latitude, price_sqm, living_area_sqm):
        """ Create a new Apartment """
        self.longitude = longitude
        self.latitude = latitude
        self.price_sqm = price_sqm
        self.living_area_sqm = living_area_sqm

    @property
    def json(self):
        """ Define a base way to jsonify models
            Columns inside `to_json_filter` are excluded """
        return {
            column: value
            for column, value in self._to_dict().items()
            if column not in self.to_json_filter
        }

    def _to_dict(self):
        """ This would more or less be the same as a `to_json`
            But putting it in a "private" function
            Allows to_json to be overriden without impacting __repr__
            Or the other way around
            And to add filter lists """
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self.__class__).attrs
        }
