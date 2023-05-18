#!/usr/bin/python3
from models.school import School
from models.intern import Intern
from models.company import Company
from models import storage
from datetime import date


# school = School(name="Test School")
# school.save()

data1 = {"name": "A new company", "specialization": "Software", "available slots": 152, "email": "anewcompany@gmail.com",
        "website": "anewcompany2.com", "address": "56, a new company22 street"}
# data = {"first_name": "Tee", "last_name": "Pret", "password": "mytpass123", "email": "babafgglolataiwop@gmail.com",
#         "birthday": date.fromisoformat("2002-04-30"), "school_id": "4aeaed4a-6520-45f2-b235-910f4595c025",
#         "course": "Chemistry", "address": "56, test5433 street", "phone": "+234-523442", "school": "OAU"}
# company = Company(**data1)
# company.save()

# intern = Intern(**data)
# intern.save()
intern = storage.get("Intern", 'f3551173-de61-4f23-b01c-2b2360c1b192')
print(intern.validate_password("mytpass124"))
# interns = [obj.to_dict() for obj in all_interns]
# for ob in interns:
#     print(interns)