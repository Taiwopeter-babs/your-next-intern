#!/usr/bin/python3
"""This module delivers authentication for a user"""
from web_app.main_app import app
from flask import render_template
from web_app.views import app_views


@app.errorhandler(408)
# @app_views.route("/408", methods=['GET'])
def request_timeout_error(error):
    """ 408 error handler """
    return render_template('408.html')

@app.errorhandler(500)
# @app_views.route("/500", methods=['GET'])
def internal_server_error(error):
    """ 500 error handler """
    return render_template('500.html')

@app.errorhandler(404)
# @app_views.route("/404", methods=['GET'])
def not_found_error(error):
    """ Handler for 404 error """
    return render_template("404.html")