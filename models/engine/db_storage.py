#!/usr/bin/python3
"""This module contains the DBStorage class"""
from datetime import date
from dotenv import load_dotenv
# from models.admin import Admin
from models.intern import Intern
from models.company import Company, company_intern
from models.school import School
from models.base_model import Base
import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker

# load environment variables
load_dotenv()

classes = {"Intern": Intern, "Company": Company,
           "School": School}


class DBStorage:
    """This class holds the session initialization
    and methods that enable interactions with the database

    Args:
        __engine: The database engine
        __session: session handler for database connections
    """

    __engine = None
    __session = None

    def __init__(self) -> None:
        """instantiates a database engine"""

        # Set the variables
        DB = os.getenv("YNI_MYSQL_DB")
        PWD = os.getenv("YNI_MYSQL_PWD")
        USER = os.getenv("YNI_MYSQL_USER")
        HOST = os.getenv("YNI_MYSQL_HOST")
        ENVIRONMENT = os.getenv("YNI_ENV")

        # Set the url for the database engine
        db_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(USER, PWD, HOST, DB)

        # create the engine
        """
        The pool_pre_ping parameter is used for the pessimistic testing of
        database connections whether it is live or not.

        The `pool_recycle` parameter prevents the database from using a
        connection that has passed a certain age - 1 hour.
        Any database connection that has been open for more than one hour
        will be invalidated and replaced upon next checkout
        """
        self.__engine = create_engine(db_URL, pool_pre_ping=True)
        #   pool_recycle=3600)
        # drop all tables if envinronment is test
        if ENVIRONMENT == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls_name=None) -> dict:
        """
        Returns a dictionary instance of all objects with cls_name instance,
        otherwise if cls_name is None, a dictionary instance of all objects
        of all class instances - Intern, Company is returned.
        """
        all_objs = {}
        if cls_name:
            if type(cls_name) is str:
                cls_name = classes.get(cls_name)
            statement = select(cls_name)
            result_objs = self.__session.scalars(statement).all()

            for obj in result_objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs.update({key: obj})
            return all_objs

        # Queries the database for objects of each class
        # and adds them to the dictionary
        for value in classes.values():
            statement = select(value)
            result_objs = self.__session.scalars(statement).all()

            for obj in result_objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs.update({key: obj})

        return all_objs

    def new(self, obj):
        """
        Adds/Places a new object to the database session
        if the object is not None
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commits/writes all changes to the database"""
        self.__session.commit()

    def delete(self, obj):
        """Places obj to be deleted from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates the tables in the database, and instantiates the current
        database session

        Base is an instance of sqlalchemy.orm.declarative_base that enables
        mapping of classes e.g Intern, Company to tables interns and companies.

        scoped_session enables maintainance of a distinct object per each
        application thread. It provides way of providing a single, global
        object in an application that is safe to be called upon from multiple
        threads.
        """
        # creates all the tables
        Base.metadata.create_all(self.__engine)

        # creates a session factory
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the current database session"""
        self.__session.close()

    def rollback_session(self):
        """ rollback session """
        self.__session.rollback()

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
            # stmt = select(cls).where(cls.id == id)
            # user = self.__session.execute(stmt).first()
            user = self.__session.query(cls).filter_by(id=id).first()
            return user
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

    def get_company_by_date(self, intern_id) -> list:
        """Returns a list of Company objects linked to an Intern
        Object. A list of tuples which contain the company applied to,
        and date e.g [(company_obj1, datetime.date(2023-05-15)),
        (company_obj2, datetime.date(2023-06-15))].

        These list of tuples will have the date added to the dictionary of the
        company
        """
        list_companies = []
        date_form = "%Y-%m-%d"

        if self.get("Intern", intern_id):
            companies = (
                self.__session.query(Company, company_intern.c.date_applied)
                .join(company_intern)
                .join(Intern)
                .filter(Intern.id == intern_id)
                .all()
            )

            if companies:
                # add the date applied to the companies dictionary
                for company, date_applied in companies:
                    int_list = [obj.to_dict() for obj in company.interns]
                    company_dict = company.to_dict()
                    company_dict["interns"] = int_list
                    company_dict["date_applied"] = date_applied.strftime(
                        date_form)
                    list_companies.append(company_dict)

                return list_companies
            return None

        return None

    def get_user_by_email(self, email: str, cls_name=None):
        """ Get a user by email """
        if cls_name:
            if type(cls_name) is str:
                cls_name = classes.get(cls_name)
            user = self.__session.query(
                cls_name).filter_by(email=email).first()
            if user:
                return user
            return None

        # find email match across tables
        for class_name in classes:
            cls_name = classes.get(class_name)
            user = self.__session.query(
                cls_name).filter_by(email=email).first()
            if user:
                return user

        return None

    def get_user_id(self, cls_name, user_id: str):
        """ Get a user id """
        if type(cls_name) is str:
            cls_name = classes.get(cls_name)
        user = self.__session.query(cls_name).filter_by(id=user_id).first()
        if user:
            return user.id
        return None

    def get_user_by_id(self, user_id: str):
        """ Get a user by id """
        all_objs = self.all()

        for obj in all_objs:
            if user_id == obj.split(".")[1]:
                return all_objs.get(obj)
        return None

    def get_school_id(self, sch_name: str) -> str:
        """ Returns the school id of school_name from the database storage."""

        stmt = select(School.id).where(School.name == sch_name)
        sch_id = self.__session.scalars(stmt).all()

        if sch_id:
            return sch_id[0]
        else:
            return None
