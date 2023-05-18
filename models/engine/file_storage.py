#!/usr/bin/python3
"""
This module contains the class FileStorage
that manages the local storage engine
"""
import json
from models.base_model import BaseModel
from models.intern import Intern
from models.company import Company
from models.school import School


classes = {"BaseModel": BaseModel, "Intern": Intern, "Company": Company,
           "School": School}


class FileStorage:
    """Manages the local storage engine"""

    # dictionary - will store objects with key <classname>.id
    __objects = {}

    # string - path to JSON file
    __file_path = "yni.json"

    def all(self, cls_name=None) -> dict:
        """returns all the objects of a class
        or all objects of all the classes if cls is None
        """
        if cls_name:
            if type(cls_name) is str:
                cls_name = classes.get(cls_name)
            cls_dict = {}
            for key in FileStorage.__objects.keys():
                if classes.get(key.split(".")[0]) == cls_name:
                    cls_dict[key] = FileStorage.__objects.get(key)
            return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds the obj to the __objects dictionary"""
        if obj:
            obj_id = obj.id
            obj_cls = type(obj).__name__
            key = "{}.{}".format(obj_cls, obj_id)

            FileStorage.__objects.update({key: obj})

    def save(self):
        """Serializes the FileStorage__objects dictionary to JSON"""
        all_objs = FileStorage.__objects
        new_dict = {obj: all_objs[obj].to_dict() for obj in all_objs.keys()}

        with open(FileStorage.__file_path, "w+", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """This method reloads the saved json file for use"""

        try:
            with open(FileStorage.__file_path, "r+", encoding="utf-8") as file:
                all_obj = json.load(file)

            for key, val in all_obj.items():
                cls_name = all_obj[key].get("__class__")
                del all_obj[key]["__class__"]
                self.all()[key] = classes.get(cls_name)(**val)
        except FileNotFoundError:
            pass

    def get(self, cls, id):
        """Returns the object of the class name and id specified.
        If no object is found with the id, None is returned

        Args:
            cls: class name of the object to be returned
            id(str): unique id of the object
        """
        if cls and id:
            if type(cls) is str:
                cls = classes.get(cls)
            obj_key = "{}.{}".format(cls.__name__, id)
            cls_obj = self.all(cls).get(obj_key)
            return cls_obj
        return None

    def count(self, cls=None) -> int:
        """Returns the number of object of class cls
        If no cls is specified, the amount of objects in the
        storage is returned
        """
        if cls:
            cls_objs = self.all(cls)
            return len(cls_objs)
        return len(self.all())
