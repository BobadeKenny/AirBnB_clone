#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project
"""

import uuid
from datetime import datetime


class BaseModel:
    """Base Class"""
    def __init__(self):
        """instance init
        Returns:
            None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """string
        Returns:
            str: string representation of class
        """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id,
                        self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        Returns:
            None
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:
        Returns:
            dict: dictionary representation of class
        """
        class_dict = self.__dict__.copy()
        if "created_at" in class_dict:
            class_dict["created_at"] = class_dict["created_at"].isoformat()
        if "updated_at" in class_dict:
            class_dict["updated_at"] = class_dict["updated_at"].isoformat()
        class_dict["__class__"] = self.__class__.__name__
        return class_dict
