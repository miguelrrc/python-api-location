from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_sqlalchemy import SQLAlchemy
from numpy import genfromtxt
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('postgresql://@localhost:5432/location_db')
if not database_exists(engine.url):
    create_database(engine.url)

# Base = declarative_base()
db = SQLAlchemy()


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()


# create tables
Base.metadata.create_all(engine)

# Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

# Import csv
with open('dataset.csv', 'r') as f:
    conn = engine.raw_connection()
    try:
        cursor = conn.cursor()
        # cmd = "copy apartment FROM '/dataset.csv' delimiter ',' csv"
        cmd = 'COPY apartment(longitude, latitude, price_sqm, living_area_sqm) FROM STDIN WITH (FORMAT CSV)'
        cursor.copy_expert(cmd, f)
        conn.commit()
    except Exception as e:
        print('Error: ', e)
