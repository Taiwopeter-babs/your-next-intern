#!/usr/bin/python3
"""This module delivers the API routes for companies"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage



@app_views.route('/interns/<intern_id>/companies', methods=['GET'])
def get_companies_of_intern(intern_id):
    """Retrieves companies linked to an Intern object
    """
    com_list = storage.get_company_by_date(intern_id)

    if com_list:
        return make_response(jsonify(com_list), 200)

    return make_response(jsonify([]), 200)