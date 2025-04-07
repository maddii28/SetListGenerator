from flask import Flask
from flask_cors import CORS
from .db import init_db

def create_app():
    app = Flask(__name__) # initialize Flask app
    CORS(app) # allow frontend and backend to communicate
    init_db(app) # connect to database

    from .routes import main # import the blueprint that contains the endpoints
    app.register_blueprint(main) # tell Flask to use those endpoints

    return app