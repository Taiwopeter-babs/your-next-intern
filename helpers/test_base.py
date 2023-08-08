#!/usr/bin/python3
# from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
# from models.intern import Intern
from datetime import datetime, date
import hashlib

# hashed = hashlib.sha256('teepane2547'.encode('utf-8')).hexdigest()
# print(hashed)

date_new = datetime.utcnow()
print(date_new.strftime("%Y-%m-%dT%H:%M:%S"))
# datetime.fromisoformat(datetime.utcnow())
