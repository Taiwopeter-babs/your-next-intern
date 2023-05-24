#!/usr/bin/python3
"""This module delivers authentication for a user"""
from datetime import date
from flask import render_template, url_for, render_template, redirect, request, make_response, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from models.intern import Intern
from models.company import Company
import re
from web_app.auth import app_auth
from werkzeug.exceptions import HTTPException


# email regex pattern
pattern = '[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'

@app_auth.route("/")
def go_home():
    # choose which route to direct the intern to depending
    # on the class name - see index.html
    if current_user.is_authenticated:
        from models import storage
        user = storage.get_user_by_id(current_user.id)
        user_class = user.to_dict()['__class__']
        return render_template("index.html", user_class=user_class)

    return render_template("index.html")


@app_auth.route("/login", methods=['GET', 'POST'])
def login():
    """ Login route """
    from models import storage

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        intern = storage.get_user_by_email("Intern", email)
        company = storage.get_user_by_email("Company", email)
        if intern:
            if intern.validate_password(password):
                login_user(intern, remember=True)

                # return client to requested page
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('app_auth.go_home')
                flash('Login successful', category='success')
                return redirect(next)
                
            else:
                flash('Incorrect email or password', category='error')
                return redirect(url_for('app_auth.login'))

        if company:
            if company.validate_password(password):
                # flash("Login successful", category='success')
                login_user(company, remember=True)

                # return client to requested page
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('app_auth.go_home')
                flash('Login successful', category='success')
                return redirect(next)
                
            else:
                flash('Incorrect email or password', category='error')
                return redirect(url_for('app_auth.login'))

        else:
            flash("Email does not exist", category='error')

    return render_template('login.html', user=current_user)


@app_auth.route("/logout")
@login_required
def logout():
    """ Logout route """
    logout_user()
    flash('Logout successful')
    return redirect(url_for('app_auth.go_home'))


@app_auth.route("/intern_signup", methods=['GET', 'POST'])
def intern_signup():
    """ Intern registration endpoint """
    from models import storage

    sch_objs = storage.all("School").values()
    schools = sorted(sch_objs, key=lambda k: k.name)

    if request.method == 'POST':
        first_name = request.form.get('first_name')
        specialization = request.form.get('specialization')
        gender = request.form.get('gender')
        available_slots = request.form.get('available_slots')
        school = request.form.get('school')
        course = request.form.get('course')
        address = request.form.get('address')
        phone = request.form.get('phone')
        preferred_organization = request.form.get('preferred_organzation')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        school_id = storage.get_school_id(school)
        if school_id:
            sch_id = school_id
        else:
            storage.rollback_session()
            flash('Please choose a school', category='error')
            return render_template('intern_signup.html', schools=schools)

        # check if the email is already in use     
        check_exists_email = storage.get_user_by_email(Intern, email)
        if check_exists_email:
            flash('Email already in use', category='error')
            return render_template('intern_signup.html', schools=schools)

        email_match = re.search(pattern, email)
        if not email_match:
            storage.rollback_session()
            flash('Email must follow this pattern \'example@something.com\'',
                  category='error')
            return render_template('intern_signup.html', schools=schools)
        
        # check phone pattern
        phone_pattern = re.compile(r'(\d{3,5})\D*(\d{2})\D*(\d{3})\D*(\d{3})$')
        phone_match = phone_pattern.search(phone).groups()
        if not phone_match:
            storage.rollback_session()
            flash('Phone must follow the pattern in the input form')
            return render_template('intern_signup.html', schools=schools)
        
        
        if len(password1) < 8:
            flash('Password too short', category='error')
            return render_template('intern_signup.html', schools=schools)
        if password1 != password2:
            storage.rollback_session()
            flash('passwords do not match', category='error')
            return render_template('intern_signup.html', schools=schools)
        
        data = {'first_name': first_name, 'specialization': specialization, 'gender': gender,
                'available_slots': date.fromisoformat(available_slots), 'school': school,
                'course': course, 'address': address, 'phone': phone,
                ' preferred_organization': preferred_organization,
                'email': email, 'password': password1, 'school_id': sch_id}
        
        intern = Intern(**data)
        try:
            intern.save()     
        except HTTPException:
            storage.rollback_session()
            flash('Please fill all required fields', category='error')
            return render_template('intern_signup.html', schools=schools)

        flash('Registration successful! Please login.', category='success')
        return redirect(url_for('app_auth.login'))
        
    return render_template('intern_signup.html', schools=schools)


@app_auth.route("/org_signup", methods=['GET', 'POST'])
def org_signup():
    """ Company registration endpoint """
    from models import storage

    if request.method == 'POST':
        name = request.form.get('name')
        specialization = request.form.get('specialization')
        email = request.form.get('email')
        available_slots = request.form.get('available_slots')
        address = request.form.get('address')
        website = request.form.get('website')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        check_exists_email = storage.get_user_by_email(Company, email)
        if check_exists_email:
            flash('Email already in use', category='error')
            return render_template('org_signup.html')
        email_match = re.search(pattern, email)
        if not email_match:
            storage.rollback_session()
            flash('Email must follow this pattern \'example@something.com\'',
                  category='error')
            return render_template('org_signup.html')
        
        
        if len(password1) < 8:
            flash('Password too short', category='error')
            return render_template('org_signup.html')
        if password1 != password2:
            storage.rollback_session()
            flash('passwords do not match', category='error')
            return render_template('org_signup.html')
        
        data = {'name': name, 'specialization': specialization,
                'available_slots': available_slots, 'address': address,
                'email': email, 'password': password1, 'website': website}
        
        company = Company(**data)
        try:
            company.save()
        except HTTPException:
            flash('Please fill all required fields', category='error')
            storage.rollback_session()
            return render_template('org_signup.html')

        flash('Registration successful! Please login.', category='success')
        return redirect(url_for('app_auth.login'))
        
    return render_template('org_signup.html')