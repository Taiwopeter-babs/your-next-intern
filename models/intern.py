#!/usr/bin/python3
"""This module defines the Intern class"""
import hashlib
from flask_login import UserMixin
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Boolean, DATE, String, ForeignKey
from sqlalchemy.orm import relationship


class Intern(BaseModel, Base, UserMixin):
    """This class maps to the interns table in the database"""

    if models.storage_type == "db":
        __tablename__ = "interns"

        email = Column(String(128), nullable=False, index=True, unique=True)
        password = Column(String(256), nullable=False)
        first_name = Column(String(100), nullable=False)
        last_name = Column(String(100), nullable=False)
        gender = Column(String(10))
        birthday = Column(DATE, nullable=False)
        school = Column(String(128), nullable=False)
        course = Column(String(128), nullable=False)
        image_path = Column(String(128), nullable=True)
        address = Column(String(256), nullable=False)
        phone = Column(String(15), nullable=False, unique=True)
        preferred_organization = Column(String(256))
        is_administrator = Column(Boolean, default=False)
        school_id = Column(String(50), ForeignKey("schools.id"),
                           nullable=False)
        intern_school = relationship("School", back_populates="school_interns")
        companies = relationship(
            "Company", secondary="company_intern", back_populates="interns", viewonly=False
        )

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        super().__init__(*args, **kwargs)
