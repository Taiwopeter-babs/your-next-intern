#!/usr/bin/python3
"""This module delivers authentication for a user"""
from datetime import date
from flask import render_template, url_for, render_template, redirect, flash, jsonify
from flask_login import login_required, current_user
from models.intern import Intern
import re
from web_app.views import app_views


@app_views.route("/intern_profile/<intern_id>", methods=['GET', 'POST'])
@login_required
def intern_profile(intern_id):
    from models import storage
    if current_user.is_authenticated:
        storage.get_user_id(Intern, intern_id)
        return render_template("intern_profile.html", user=current_user)