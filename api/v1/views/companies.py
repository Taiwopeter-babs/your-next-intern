#!/usr/bin/python3
"""This module delivers the API routes for companies"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from werkzeug.exceptions import HTTPException
from sqlalchemy import exc
from models import storage


@app_views.route('/companies/<company_id>', methods=['GET', 'PUT'])
def get_company(company_id):
    """Retrieves a Company object
    """
    com_obj = storage.get("Company", company_id)

    if com_obj:

        try:

            com_dict = com_obj.to_dict()
            int_list = [obj.to_dict() for obj in com_obj.interns]
            com_dict["interns"] = int_list
                    
            if request.method == 'GET':  
                return make_response(jsonify(com_dict), 200)
            
            if request.method == 'PUT':
                if not request.json:
                    return make_response(jsonify('Not a JSON'), 400)
                
                req_dict = request.get_json()
                if 'application_open' not in req_dict:
                    return make_response(jsonify('Empty request'), 400)


                com_obj.application_open = req_dict.get('application_open')
                com_obj.save()
                com_dict = com_obj.to_dict()
                int_list = [obj.to_dict() for obj in com_obj.interns]
                com_dict["interns"] = int_list
                      
                return make_response(jsonify(com_obj.to_dict()), 200)
                    
        except exc.SQLAlchemyError:
            storage.rollback_session()
            return make_response(jsonify('Request timeout or overload'), 408)

    abort(404)
        
    

@app_views.route('/companies/<company_id>/interns/<intern_id>', methods=['POST', 'DELETE'])
def link_intern_with_company(company_id, intern_id):
    """This endpoint allows an intern to be linked to a company

    if status code == 200, intern already applid to the company,
    otherwise status code == 201 and intern is just added.

    For `DELETE` requests, returns status code 200 if the action has been
    enacted, otherwise, a 204 status code is returned
    """
    try:
        intern_obj = storage.get("Intern", intern_id)
        com_obj = storage.get("Company", company_id)

        if not intern_obj:
            abort(404)
    
        if not com_obj:
            abort(404)

        # convert the companies linked to an intern to JSON serializable format
        if request.method == 'POST':
            companies = [obj.to_dict() for obj in intern_obj.companies]
            int_dict = intern_obj.to_dict()
            int_dict['companies'] = companies

            if intern_obj in com_obj.interns:
                return make_response(jsonify(True), 200)
        
            com_obj.interns.append(intern_obj)
            storage.save()
            return make_response(jsonify(True), 201)

        if request.method == 'DELETE':
            if intern_obj in com_obj.interns:
                com_obj.interns.remove(intern_obj)
                storage.save()
                return make_response(jsonify({"status": "success"}), 200)
    
            return make_response(jsonify({"status": "not found"}), 204)

        
    except exc.SQLAlchemyError:
        storage.rollback_session()
        return make_response(jsonify('Request timeout'), 408)

    
@app_views.route("/all_companies", methods=['GET'])
def open_companies():
    """ An endpoint that returns a `JSON` list of companies
    """
    try:
        all_coms = storage.all("Company").values()
        sorted_coms = sorted(all_coms, key=lambda k: k.name)
        
        return_list = []
        for com in sorted_coms:
            com_dict = com.to_dict()
            interns = [obj.to_dict() for obj in com.interns]
            com_dict['interns'] = interns
            return_list.append(com_dict)

        response = jsonify(return_list)
        return make_response(response, 200)

    except exc.SQLAlchemyError:
        storage.rollback_session()
        return make_response(jsonify({"status": "Request timeout"}), 408)
