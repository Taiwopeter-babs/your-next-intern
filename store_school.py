#!/usr/bin/python3
"""This module uses an api to get the names of all
higher institutions in Nigeria from a JSON file
"""
import json
from models.school import School


def get_institution_names() -> list:
    """
    Load the names of all the universities from a file
    into an object

    Return:
        A sorted list of all schools
    """
    file_name = "universities.json"

    try:
        with open(file_name, "r+", encoding="utf-8") as json_file:
            school_list = json.load(json_file)

            school_names = [school.get("name") for school in school_list]
            school_names = sorted(school_names)
            return school_names
    except FileNotFoundError:
        return None


def store_school_to_database():
    """Stores each school name to the database"""
    school_names = get_institution_names()

    if school_names:
        for sch_name in school_names:
            school_instance = School(name=sch_name)
            school_instance.save()


if __name__ == "__main__":
    #get_institution_names()
    store_school_to_database()
