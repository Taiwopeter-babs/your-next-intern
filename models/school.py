#!/usr/bin/python3
"""This module defines the Intern class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DATE
from sqlalchemy.orm import relationship


class School(BaseModel, Base):
    """This class maps to the schools table in the database"""

    if models.storage_type == "db":
        __tablename__ = "schools"

        name = Column(String(256), nullable=False)
        school_interns = relationship(
            "Intern", cascade="all, delete, delete-orphan",
            back_populates="intern_school"
        )

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def interns(self):
            """getter for list of intern instances related to the school"""
            all_interns = models.storage.all("Intern").values()
            
            intern_list = [intern for intern in all_interns
                           if intern.school_id == self.id]
            return intern_list
