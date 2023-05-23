#!/usr/bin/python3
"""This module delivers authentication for a user"""
from datetime import date
from flask import render_template, url_for, render_template, redirect, flash, jsonify
from flask_login import login_required, current_user
from models.company import Company
from models.intern import Intern
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
    The template rendered depends on whether the user is
    authenticated and the class, if authenticated.

    The template rendering is checked for the `Company` class
    to allow only users with `Intern` class apply to companies.

    `Company` class clients and users that are not authenticated can
    also view companies but cannot apply.
    """
    from models import storage
    
    all_companies = storage.all(Company).values()
    companies = sorted(all_companies, key=lambda k: k.name)

    # Get the user's class if authenticated
    if current_user.is_authenticated:
        user = storage.get_user_by_id(current_user.id)
        user_class = user.to_dict()['__class__']

        if user_class == 'Intern':
            return render_template("auth_all_companies.html",
                                   companies=companies)
    return render_template("all_companies.html", companies=companies)

@app_views.route("/org_profile/<company_id>", methods=['GET', 'POST'])
@login_required
def company_profile(company_id):
    """ Retrieve data for a company's profile """
    from models import storage
    if current_user.is_authenticated:
        storage.get_user_id(Company, company_id)
        return render_template("org_profile.html", user=current_user)

@app_views.route("/all_interns", methods=['GET'])
def all_interns():
    """ Get all the companies on the platform """
    from models import storage
    all_interns = storage.all(Intern).values()
    interns = sorted(all_interns, key=lambda k: k.first_name)
    return render_template("all_interns.html", interns=interns)
