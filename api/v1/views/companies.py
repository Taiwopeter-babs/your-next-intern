#!/usr/bin/python3
"""This module delivers the API routes for companies"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage



@app_views.route('/companies/<company_id>', methods=['GET'])
def get_company(company_id):
    """Retrieves a Company object
    """
    company_obj = storage.get("Company", company_id)

    if company_obj:
        com_dict = company_obj.to_dict()
        int_list = [obj.to_dict() for obj in company_obj.interns]
        com_dict["interns"] = int_list
        return make_response(jsonify(com_dict), 200)
    abort(404)

@app_views.route('/companies/<company_id>/interns/<intern_id>', methods=['POST'])
def link_intern_with_company(company_id, intern_id):
    """This endpoint allows an intern to be linked to a company

    if status code == 200, intern already applid to the company,
    otherwise status code == 201 and intern is just added.
    """
    intern_obj = storage.get("Intern", intern_id)
    
    if not intern_obj:
        abort(404)
    com_obj = storage.get("Company", company_id)
    if not com_obj:
        abort(404)

    
    if intern_obj in com_obj.interns:
        return make_response(jsonify(intern_obj.to_dict()), 200)
    
    com_obj.interns.append(intern_obj)
    storage.save()
    return make_response(jsonify(intern_obj.to_dict()), 201)
