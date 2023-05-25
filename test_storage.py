#!/usr/bin/python3
# from models.school import School
# from models.intern import Intern
# from models.company import Company
from models import storage
from datetime import date, datetime
import uuid
import hashlib
import re


data1 = {"name": "A new company", "specialization": "Software", "available slots": 152, "email": "anewcompany@gmail.com",
         "website": "anewcompany2.com", "address": "56, a new company22 street"}
data = {"first_name": "Tee", "last_name": "Pret", "password": "mytpass123", "email": "babafgglolataiwop@gmail.com",
        "birthday": date.fromisoformat("2002-04-30"), "school_id": "011319e7-fbe7-48ad-8072-5e896a3b6053",
        "course": "Chemistry", "address": "56, test5433 street", "phone": "+234-523442", "school": "OAU", "gender": "Male"}
# company = Company(**data1)
# company.save()

# intern = storage.get_user_by_id("57813677-0552-49bb-8468-805361aa0f66")
# print(intern.password)

hashed = hashlib.sha256('yni_secret_key@#__6991'.encode('utf-8')).hexdigest()
# hashed2 = hashlib.sha256('sapeir123'.encode('utf-8')).hexdigest()


com = storage.get('Company', 'b5d3ad91-1040-4361-a51c-60caaecc75f3')
print(com.application_open)
# intern_obj = storage.get("Intern", '45cdf2e9-b073-4aeb-910a-be810a7c565e')
# print(intern_obj.to_dict())
# for com in intern_obj.companies:
#         print(com.to_dict())

# pattern = '[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
# res = re.search(pattern, "sef-hi@gmail.com")
# phone_pattern = re.compile(r'(\d{3,5})\D*(\d{2})\D*(\d{3})\D*(\d{3})$')
# res = phone_pattern.search('+2348052002346').groups()

# if res:
#     print(res)
# else:
#     print('No match')

# print(hashed)
