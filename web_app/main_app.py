""" create the authentication blueprint """
from flask import Flask
from flask_login import LoginManager

from web_app.auth import app_auth
from web_app.views import app_views

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = 'yni_secret_key'

# blueprints
app.register_blueprint(app_auth)
app.register_blueprint(app_views)

login_manager = LoginManager()
login_manager.login_view = "app_auth.login"
login_manager.session_protection = 'strong'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """ Load information about a user that is authenticated """
    from models import storage
    return storage.get_user_by_id(user_id)


def close_db(error):
    """Remove the current SQLAlchemy Session"""
    from models import storage
    storage.close()


if __name__ == "__main__":
    """Main"""
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
