#!/usr/bin/env python3
"""This module uses an api to get the names of all
higher institutions in Nigeria from a JSON file
"""
import json
from models.school import School
from typing import List, Union


def get_institution_names() -> Union[List[str], None]:
    """
    Load the names of all the schools from a file
    into an object

    Return:
        A sorted list of all schools
    """
    file_name = "schools.json"

    try:
        with open(file_name, "r+", encoding="utf-8") as json_file:
            school_dict = json.load(json_file)

            keys = [key for key in school_dict]

            school_names = [
                school for key in keys for school in school_dict.get(key)
            ]
            return sorted(school_names)
    except FileNotFoundError:
        return None


def store_school_to_database() -> None:
    """Stores each school name to the database"""

    school_names = get_institution_names()

    if school_names:
        for sch_name in school_names:
            school_instance = School(name=sch_name)
            school_instance.save()


if __name__ == "__main__":

    get_institution_names()
    # store_school_to_database()
