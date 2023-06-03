#!/usr/bin/python3
"""This module creates the Flask app factory
and registers blueprints for diffrent API routes
"""
from api.v1.views import app_views
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
import os


def create_app():
    """ API app factory """
    app = Flask(__name__)


    # disable strict slashes in routes
    app.url_map.strict_slashes = False

    # register blueprints
    app.register_blueprint(app_views)

    # Enable cross-origin-resource sharing
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


    def close_db_connection(error):
        """Closes the database connection"""
        storage.close()

    @app.errorhandler(404)
    def not_found(error):
        """ 
        404 error

        Return: 404 - resource not found 
        """
        return make_response(jsonify({"error": "Not found"}), 404)
    
    return app

if __name__ == "__main__":
    load_dotenv()

    HOST = os.getenv("API_HOST")
    PORT = os.getenv("API_PORT")

    host = HOST if HOST else "0.0.0.0"
    port = PORT if PORT else "5000"

    app = create_app()

    app.run(host=host, port=port, threaded=True, debug=True)
