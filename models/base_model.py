#!/usr/bin/python3
"""
This module defines a base class `BaseModel`, which defines attributes
and methods that other classes inherit from
"""

from datetime import datetime
import hashlib
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid


# This is the mapper factory function that enables mapping of
# class to tables
if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """This class defines methods and attributes that
    other classes of the package inherits from
    """
    if models.storage_type == "db":
        id = Column(String(50), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Constructor for the base class"""
        time = "%Y-%m-%dT%H:%M:%S"

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            """The created_at and updated_at attributes can be string type
            due to the to_dict() method parsing of the datetime to string
            """
            if kwargs.get("created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id") is None:
                self.id = str(uuid.uuid4())
            if kwargs.get("password"):
                self.password = hashlib.sha256(
                    kwargs["password"].encode('utf-8')).hexdigest()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def save(self):
        """saves the object to storage"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """converts the object to a dictionary instance"""

        time_format = "%Y-%m-%dT%H:%M:%S"
        new_dict = {}
        new_dict.update(self.__dict__)

        str_created = self.created_at.strftime(time_format)
        str_updated = self.updated_at.strftime(time_format)

        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = str_created
        new_dict["updated_at"] = str_updated

        if '_sa_instance_state' in new_dict:
            del new_dict["_sa_instance_state"]
        if models.storage_type == "db":
            if "password" in new_dict:
                del new_dict["password"]

        return new_dict

    def __str__(self):
        """returns a string representation of the object"""
        cls_name = type(self).__name__
        _id = self.id
        obj_dict = self.__dict__

        return "[{}] ({}) {}".format(cls_name, _id, obj_dict)
