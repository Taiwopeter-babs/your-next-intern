#!/usr/bin/python3
"""This module delivers authentication for a user"""
from datetime import date
from flask import render_template, url_for, render_template, redirect, request, make_response, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from models.intern import Intern
import re
from web_app.auth import app_auth

# email regex pattern
pattern = '[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'

@app_auth.route("/")
def go_home():
    return render_template("index.html", user=current_user)


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
                return redirect(next)
            else:
                flash('Incorrect email or password', category='error')
                return redirect(url_for('app_auth.login'))

        if company:
            if company.validate_password(password):
                flash("Login successful", category='success')
                login_user(company, remember=True)

                # return client to requested page
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('app_auth.go_home')
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
        last_name = request.form.get('last_name')
        gender = request.form.get('gender')
        birthday = request.form.get('birthday')
        school = request.form.get('school')
        course = request.form.get('course')
        address = request.form.get('address')
        phone = request.form.get('phone')
        preferred_organization = request.form.get('preferred_organzation')

        school_id = storage.get_school_id(school)
        if school_id:
            sch_id = school_id
        else:
            storage.rollback_session()
            flash('Please choose a school', category='error')
            return render_template('intern_signup.html', schools=schools)

            
        email = request.form.get('email')
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
        
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(password1) < 8:
            flash('Password too short', category='error')
            return render_template('intern_signup.html', schools=schools)
        if password1 != password2:
            storage.rollback_session()
            flash('passwords do not match', category='error')
            return render_template('intern_signup.html', schools=schools)
        
        data = {'first_name': first_name, 'last_name': last_name, 'gender': gender,
                'birthday': date.fromisoformat(birthday), 'school': school,
                'course': course, 'address': address, 'phone': phone,
                ' preferred_organization': preferred_organization,
                'email': email, 'password': password1, 'school_id': sch_id}
        
        intern = Intern(**data)
        try:
            intern.save()
            storage.rollback_session()
        except:
            flash('Please fill all required fields', category='error')

        flash('Registration successful! Please login.', category='success')
        return redirect(url_for('app_auth.login'))
        
    return render_template('intern_signup.html', schools=schools)