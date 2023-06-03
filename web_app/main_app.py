""" create the authentication blueprint """
from web_app.config import Config
from flask import Flask, render_template
from flask_login import LoginManager
from web_app.auth import app_auth
from web_app.views import app_views

# Configuration for the upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.url_map.strict_slashes = False

# load the application configuration from Config class
app.config.from_object(Config)

def create_app():
    """ App Factory """

    # Register blueprints
    app.register_blueprint(app_auth)
    app.register_blueprint(app_views)

    """ Protection for the routes/endpoints which are only
    accessed by authenticated users
    """
    login_manager = LoginManager()
    login_manager.login_view = "app_auth.login"
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        """ Load information about a user that is authenticated """
        from models import storage
        return storage.get_user_by_id(user_id)


    @app.errorhandler(408)
    def request_timeout_error(error):
        """ 408 error handler """
        return render_template('408.html')

    @app.errorhandler(500)
    def internal_server_error(error):
        """ 500 error handler """
        return render_template('500.html')

    @app.errorhandler(404)
    def not_found_error(error):
        """ Handler for 404 error """
        return render_template("404.html")


    # close session on exit of application or error 
    def close_db(error):
        """Remove the current SQLAlchemy Session"""
        from models import storage
        storage.close()
    
    return app


if __name__ == "__main__":
    """Main"""
    app = create_app()
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
