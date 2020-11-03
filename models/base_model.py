#!/usr/bin/python3
"""
   This is the module of the base_models.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
       Define BaseModel class.
    """
    def __init__(self):
        """
           Contructor.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
           special method.
        """
        name = self.__class__.__name__
        return "[{0}] ({1}) {2}".format(name, self.id, self.__dict__)

    def save(self):
        """
           Update date.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
           Return dictionary.
        """
        name = self.__class__.__name__
        New_dict = self.__dict__.copy()
        New_dict.update(__class__=name, created_at=self.created_at.isoformat())
        New_dict.update(updated_at=self.updated_at.isoformat())

        return New_dict
