#!/usr/bin/python3
"""This module delivers the API routes for interns"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage



@app_views.route("/interns", methods=['GET', 'POST'])
def get_all_interns():
    """ Retrives all Intern objects from storage """
    
    if request.method == "GET":
        all_interns = storage.all("Intern").values()

        interns = [obj.to_dict() for obj in all_interns]
        return make_response(jsonify(interns), 200)


@app_views.route('/interns/<intern_id>', methods=['GET', 'PUT'])
def get_intern(intern_id):
    """Retrieves a single Intern object or Updates it
    based on the HTTP method used to access the resource

    For now, first_name, last_name, and address can only be
    updated
    """
    intern_obj = storage.get("Intern", intern_id)

    if intern_obj:
        if request.method == 'GET':
            return make_response(jsonify(intern_obj.to_dict()), 200)
        
        # if request.method == 'PUT':
        #     if not request.json:
        #         return make_response(jsonify("Not a JSON"), 400)

        #     req_dict = request.get_json()

        #     if "first_name" in req_dict:
        #         intern_obj.first_name = req_dict.get("first_name")
        #     if "last_name" in req_dict:
        #         intern_obj.last_name = req_dict.get("last_name")
        #     if "address" in req_dict:
        #         intern_obj.address = req_dict.get("address")
            
        #     intern_obj.save()
        #     return make_response(jsonify(intern_obj.to_dict()), 200)

    abort(404)