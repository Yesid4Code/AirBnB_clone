#!/usr/bin/python3
""" module for class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User inherited from BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
