#!/usr/bin/python3
""" Create the blueprint for the API routes"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
from api.v1.views.interns import *
from api.v1.views.companies import *
from api.v1.views.companies_interns import *
