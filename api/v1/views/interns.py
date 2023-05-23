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


@app_views.route('/interns/<intern_id>/', methods=['GET'])
def get_intern(intern_id):
    """Retrieves a single Intern object
    """
    intern_obj = storage.get("Intern", intern_id)

    if intern_obj:
        if request.method == 'GET':
            ret_dict = {}
            int_dict = intern_obj.to_dict()
            com_list = [obj.to_dict() for obj in intern_obj.companies]
            int_dict["companies"] = com_list
            return make_response(jsonify(int_dict), 200)
    abort(404)

