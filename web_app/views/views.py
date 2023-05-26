#!/usr/bin/python3
"""This module delivers authentication for a user"""
from datetime import date
from flask import render_template, url_for, render_template, redirect, flash, jsonify, abort
from flask_login import login_required, current_user
from models.company import Company
from models.intern import Intern
from sqlalchemy import exc
from web_app.views import app_views



@app_views.route("/intern_profile/<intern_id>", methods=['GET', 'POST'])
@login_required
def intern_profile(intern_id):
    """ retrieve data for an intern profile """
    from models import storage
    if current_user.is_authenticated:
        storage.get_user_id(Intern, intern_id)
        return render_template("intern_profile.html", user=current_user)

@app_views.route("/all_companies", methods=['GET'])
def all_companies():
    """ Get all the companies on the platform. 
    The template rendered depends on the class and if the user is
    authenticated or not.

    The template is rendered to allow only users with `Intern` 
    class to apply to companies.
    `Company` class clients and users that are not authenticated can
    also view companies but cannot apply.

    The Company objects rendered for authenticated `interns` have their
    `application_open` set to True
    """
    from models import storage
    
    try:
        all_companies = storage.all(Company).values()
    except exc.SQLAlchemyError:
        storage.rollback_session()
        abort(404)

    companies = sorted(all_companies, key=lambda k: k.name)

    """
    Get the user's class if authenticated. This will be used
    to redirect the user to the appropriate page
    """
    if current_user.is_authenticated:
        user = storage.get_user_by_id(current_user.id)
        user_class = user.to_dict()['__class__']

        if user_class == 'Intern':
            return render_template("auth_all_companies.html",
                                   companies=companies)
    return render_template("all_companies.html", companies=companies)


@app_views.route("/all_companies/open", methods=['GET'])
def open_companies():
    """ 
    route for all the companies whose application windows are open
    """
    return render_template("open_org.html")


@app_views.route("/org_profile/<company_id>", methods=['GET', 'POST'])
@login_required
def company_profile(company_id):
    """ Retrieve data for a company's profile """
    from models import storage
    
    com_obj = storage.get(Company, company_id)
    com_interns = sorted(com_obj.interns, key=lambda k: k.first_name) 
    return render_template("org_profile.html", user=current_user,
                            com_interns=com_interns)


@app_views.route("/all_interns", methods=['GET'])
def all_interns():
    """ Get all the companies on the platform """
    from models import storage
    all_interns = storage.all(Intern).values()
    interns = sorted(all_interns, key=lambda k: k.first_name)
    return render_template("all_interns.html", interns=interns)
