#!/usr/bin/python3
""" This module contains the Config class"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    """ The Config class holds the configuration for the
    application factory
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Configuration for the upload
    UPLOAD_FOLDER = '/home/taiwop/yni_intern_users_photos/'
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024