from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS, cross_origin
from models import db
from config import Config
import routes

server = Flask(__name__)
CORS(server, resources={r"/*": {"origins": "*"}})

server.config.from_object(Config)
db.init_app(server)
db.app = server
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint,
            url_prefix='/api'
        )

if __name__ == '__main__':
    server.run()
