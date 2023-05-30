#!/usr/bin/python3
# from models.school import School
# from models.intern import Intern
# from models.company import Company
import json
from models import storage
from datetime import date, datetime
import uuid
import hashlib
import re

date_form = "%Y-%m-%d"
intern_coms = storage.get_company_by_date('45cdf2e9-b073-4aeb-910a-be810a7c565e')
for com in intern_coms:
        print(type(com['date_applied']))

# comp = storage.get('Company', 'b5d3ad91-1040-4361-a51c-60caaecc75f3')
# print(comp)


# companies = [obj.to_dict() for obj in intern.companies]
# int_dict = intern.to_dict()
# int_dict['companies'] = companies
        
# all_coms = storage.all("Company").values()
# sorted_coms = sorted(all_coms, key=lambda k: k.name)

# return_list = []
# for com in all_coms:
#         com_dict = com.to_dict()
#         # print(com_dict)
#         interns = [obj.to_dict() for obj in com.interns]
#         com_dict['interns'] = interns
#         return_list.append(com_dict)
# for obj in return_list:
#         print(type(obj))
# with open('test.json', 'w+') as jfile:
#         json.dump(intern_coms, jfile)


# hashed = hashlib.sha256('yni_secret_key@#__6991'.encode('utf-8')).hexdigest()
# hashed2 = hashlib.sha256('sapeir123'.encode('utf-8')).hexdigest()


# pattern = '[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
# res = re.search(pattern, "sef-hi@gmail.com")
# phone_pattern = re.compile(r'(\d{3,5})\D*(\d{2})\D*(\d{3})\D*(\d{3})$')
# res = phone_pattern.search('+2348052002346').groups()

# if res:
#     print(res)
# else:
#     print('No match')

# print(hashed)
