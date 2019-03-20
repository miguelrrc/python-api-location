""" Defines the Apartment repository """

from models import Apartment
from lib.geolocation import bounding_box
from sqlalchemy import and_
import pandas as pd
from models import db


class ApartmentRepository:
    """ The repository for the apartment model """

    @staticmethod
    def get():
        """ Return all """
        return db.session.query(Apartment).all()


class ApartmentItemRepository:
    """ The repository for the ApartmentItem model """

    @staticmethod
    def get(id):
        """ Query by id """
        apartment = db.session.query(Apartment).filter(Apartment.id == id).first()
        return apartment


class ApartmentLocationRepository:
    """ The repository for the ApartmentLocation model """

    @staticmethod
    def get(longitude, latitude, km):
        """ Query by location and radius """
        lon_max, lon_min, lat_max, lat_min = bounding_box(float(longitude), float(latitude), km)
        df = pd.read_sql(sql=db.session.query(Apartment).filter(and_(Apartment.longitude >= lon_min, Apartment.longitude <= lon_max, Apartment.latitude >= lat_min, Apartment.latitude <= lat_max)).statement,
                 con=db.session.bind)
        apartments = df.to_dict(orient="records")
        price_sqm_mean = df["price_sqm"].mean()
        living_area_sqm_mean = df["living_area_sqm"].mean()
        return (apartments, price_sqm_mean, living_area_sqm_mean)
