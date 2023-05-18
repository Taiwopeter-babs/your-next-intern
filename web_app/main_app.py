""" create the authentication blueprint """
from flask import Flask
from models import storage
from web_app.auth import app_auth

app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(app_auth)

def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    """ Main """
    app.run(host="0.0.0.0", port=5000, threaded=True)