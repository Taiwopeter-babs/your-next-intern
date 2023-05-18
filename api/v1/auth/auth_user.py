#!/usr/bin/python3
"""This module delivers authentication for a user"""
from api.v1.auth import app_auth
from flask import render_template, url_for, render_template, redirect


@app_auth.route("/login")
def login():
    """ login route """
    return render_template("")