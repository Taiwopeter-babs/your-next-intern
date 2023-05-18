#!/usr/bin/python3
"""This module delivers authentication for a user"""
from flask import render_template, url_for, render_template, redirect, request
from models import storage
from web_app.auth import app_auth



@app_auth.route("/intern_login", methods=['POST'])
def intern_login():
    """ Intern login route """
    return render_template('intern_login.html')

@app_auth.route("/intern_signup", methods=['POST'])
def intern_signup():
    """ Intern registration route """
    if request.method == 'POST':
        pass
    