#!/usr/bin/python3
"""This module defines the Company class"""
from datetime import date
from flask_login import UserMixin
import hashlib
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table, DATE
from sqlalchemy.orm import relationship

if models.storage_type == "db":
    company_intern = Table(
        "company_intern",
        Base.metadata,
        Column(
            "intern_id",
            String(50),
            ForeignKey("interns.id", onupdate='CASCADE', ondelete='CASCADE'),
            primary_key=True,
            nullable=False
        ),
        Column(
            "company_id",
            String(50),
            ForeignKey("companies.id", onupdate='CASCADE', ondelete='CASCADE'),
            primary_key=True,
            nullable=False
        ),
        Column(
            "date_applied",
            DATE,
            nullable=False,
            default=date.today()
        )
    )


class Company(BaseModel, Base, UserMixin):
    """This class maps to the companies table in the database"""

    if models.storage_type == "db":

        __tablename__ = "companies"

        name = Column(String(100), nullable=False, unique=True)
        address = Column(String(256), nullable=False)
        specialization = Column(String(256), nullable=False)
        available_slots = Column(Integer, default=0)
        email = Column(String(128), nullable=False, unique=True)
        password =  Column(String(256), nullable=False, unique=True)
        website = Column(String(256), nullable=False, unique=True)
        interns = relationship(
            "Intern", secondary="company_intern", back_populates="companies", viewonly=False
        )

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        super().__init__(*args, **kwargs)

    def validate_password(self, input_password):
        """ Validates an Intern paswword """
        hashed = hashlib.sha256(input_password.encode('utf-8')).hexdigest()
        return (hashed == self.password)

    if models.storage_type != "db":
        @property
        def interns(self):
            """Returns a list of Intern objects related to
            the company
            """
            all_interns = models.storage.all("Intern").values()

            intern_list = [intern for intern in all_interns
                           if intern.company_id == self.id]
            return intern_list
