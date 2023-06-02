#!/usr/bin/python3
from models.school import School
from models.intern import Intern
from models.company import Company
import json
from models import storage
from datetime import date, datetime
import uuid
import hashlib
import re
import os
import string
import random

# date_form = "%Y-%m-%d"
# intern_coms = storage.get_company_by_date('45cdf2e9-b073-4aeb-910a-be810a7c565e')
# for com in intern_coms:
#         print(type(com['date_applied']))
# path = '/home/taiwop/yni_intern_users_photos'

# try:
#         os.mkdir(path)
# except (FileExistsError, FileNotFoundError):
#         pass
# base_dir = os.path.join('~/')

comp = storage.get('Company', 'b5d3ad91-1040-4361-a51c-60caaecc75f3')
for key in comp.to_dict().keys():
        print(type(comp.to_dict()[key]), comp.to_dict()[key])
print(comp)


# companies = [obj.to_dict() for obj in intern.companies]
# int_dict = intern.to_dict()
# int_dict['companies'] = companies
        
# all_coms = storage.all("Company").values()
# for com in all_coms:
#         print(com.to_dict())
        # [print(inster.to_dict()) for inter in com.interns]
# sorted_coms = sorted(all_coms, key=lambda k: k.name)
        
# return_list = []
# for com in sorted_coms:
#         com_dict = com.to_dict()
#         interns = [obj.to_dict() for obj in com.interns]
#         com_dict['interns'] = interns
#         return_list.append(com_dict)

# with open('test.json', 'w+') as jfile:
#         json.dump(return_list, jfile)


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
# print("taiwo.iu_p.png".rsplit('.', 1)[1])

# def allowed_filename(filename: str) -> bool:
#     """ Checks if the filename is allowed """
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ['jpeg', 'jpg', 'png']

# if allowed_filename('tee.jpg'):
#         print('Saving...')
#         os.path.join(path, 'tee.jpg')
#         print('Saved')



# datetime_format = "%Y-%m-%dT%H:%M:%S"
# curr_date = datetime.now().strftime(datetime_format)


# file_str = string.ascii_letters + '12345678910'
# rand_str = ''.join([random.choice(file_str) for n in range(0, 30)])
# print(rand_str)
# print()
# file_ext = os.path.splitext('tee.jpg')[1]
# file_path = "{}_{}{}".format(rand_str, curr_date, file_ext)

# user_path = os.path.join(path, file_path)
# print(len(user_path))

