#!/usr/bin/python3
""" Create the blueprint for the API routes"""
from flask import Blueprint

app_auth = Blueprint("app_auth", __name__, url_prefix="/")
from web_app.auth.auth_user import *