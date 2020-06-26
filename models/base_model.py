#!/usr/bin/python3
""" Class BaseModel """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Define all common attributes/methods for others classes. """
    def __init__(self, *args, **kwargs):
        """ Initialize Basemodel"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k,
                            datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif not k == "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation  """
        return("[{}] ({}) {}".format(
               self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
