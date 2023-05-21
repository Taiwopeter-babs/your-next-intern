#!/usr/bin/python3
""" Create the blueprint for the API routes"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/")
from web_app.views.views import *