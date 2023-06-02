#!/usr/bin/python3
"""This module delivers authentication for a user"""
from datetime import date, datetime
from flask import render_template, url_for, render_template, request, redirect, flash, jsonify, abort, send_from_directory
from flask_login import login_required, current_user
from models.company import Company
from models.intern import Intern
import os
import random
from sqlalchemy import exc
import string
from web_app.views import app_views
from web_app.main_app import app, ALLOWED_EXTENSIONS
from werkzeug.utils import secure_filename



@app_views.route("/intern_profile/<intern_id>", methods=['GET'])
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

    except exc.SQLAlchemyError:
        storage.rollback_session()
        abort(400)


@app_views.route("/all_companies/open", methods=['GET'])
@login_required
def open_companies():
    """ 
    route for all the companies whose application windows are open
    """
    return render_template("open_org.html")


@app_views.route("/org_profile/<org_id>", methods=['GET', 'POST'])
@login_required
def company_profile(org_id):
    """ Retrieve data for a company's profile """
    from models import storage
    
    try:
        com_obj = storage.get(Company, org_id)
        com_interns = sorted(com_obj.interns, key=lambda k: k.first_name) 
        return render_template("org_profile.html", user=current_user,
                                com_interns=com_interns)
    except exc.SQLAlchemyError:
        storage.rollback_session()
        abort(400)


@app_views.route("/all_interns", methods=['GET'])
def all_interns():
    """ Get all the companies on the platform """
    from models import storage

    try:
        all_interns = storage.all(Intern).values()
        interns = sorted(all_interns, key=lambda k: k.first_name)
        return render_template("all_interns.html", interns=interns)

    except exc.SQLAlchemyError:
        storage.rollback_session()
        abort(400)

@app_views.route("/intern_profile/<intern_id>/", methods=['POST'])
@login_required
def upload_image(intern_id):
    """ Route that handles the intern image upload """
    from models import storage
    
    try:
        int_obj = storage.get(Intern, intern_id)

        if request.method == 'POST':
            # check if the request contains a file
            if 'user_photo' not in request.files:
                flash('No file in request', category='error')
                return redirect(url_for('app_views.intern_profile', intern_id=current_user.id))

            # check if the user selected a file
            up_file = request.files.get('user_photo')
            if up_file.filename == '':
                flash('No file selected')
                return redirect(url_for('app_views.intern_profile', intern_id=current_user.id))
            
            if not allowed_filename(up_file.filename):
                flash('Allowed files are jpg, jpeg, png', category="error")
                return redirect(url_for('app_views.intern_profile', intern_id=current_user.id))
            
            if up_file and allowed_filename(up_file.filename):
                filename = secure_filename(up_file.filename)

                # Generate a random string to preserve user's input

                # get file extension
                file_ext = os.path.splitext(filename)[1]

                # generate random string file name
                datetime_format = "%Y-%m-%dT%H:%M:%S"
                curr_date = datetime.now().strftime(datetime_format)
                
                gen_str = string.ascii_letters + '12345678910'
                rand_str = ''.join([random.choice(gen_str) for n in range(0, 30)])
                new_filename = "{}_{}{}".format(rand_str, curr_date, file_ext)
                
                # save the file with the new filename
                file_path = os.path.join((app.config['UPLOAD_FOLDER']), new_filename)
                up_file.save(file_path)
                int_obj.image_path = new_filename
                int_obj.save()
                flash('Image uploaded successfully', category='success')
                return redirect(url_for('app_views.intern_profile', intern_id=current_user.id))
        
    except (exc.SQLAlchemyError, FileExistsError, FileNotFoundError):
        storage.rollback_session()
        abort(400)


@app_views.route("/upload/<filename>/", methods=['GET'])
@login_required
def display_image(filename):
    """ Display image in user's profile """
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


def allowed_filename(filename: str) -> bool:
    """ Checks if the filename is allowed """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS