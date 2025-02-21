#!/usr/bin/python3
"""
    The entry point of our application'0'.
"""

from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    """
    a method that closes the storage
    """
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """
    handles the error
    """
    return jsonify({
        'error': 'Not found'
    }), 404


if __name__ == '__main__':
    if getenv('HBNB_API_HOST'):
        host = getenv('HBNB_API_HOST')
    else:
        host = "0.0.0.0"

    if getenv('HBNB_API_PORT'):
        port = getenv('HBNB_API_PORT')
    else:
        port = 5000

    app.run(host=host, port=port, threaded=True)
