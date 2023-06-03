#!/usr/bin/python3
"""Selects the storage type to load the storage engine"""
import os
from dotenv import load_dotenv

load_dotenv()

storage_type = os.getenv("YNI_STORAGE_TYPE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
