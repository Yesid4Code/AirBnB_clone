#!/usr/bin/python3
""" Class BaseModel """

from uuid import uuid4
from detetime import daterime


class BaseModel:
    """ Define all common attributes/methods for others classes. """
    def __init__(self):
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """ String representation  """
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        dic = self.__dict__.copy()
        dict['create_at'] = self.create_at.isoformat()
        dict['update_at'] = self.uptade_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
