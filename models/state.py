#!/usr/bin/python3
"""This is the State Model module.

Contains the State class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Cette classe définit un État.

    Les attributs:
        name (str) : le nom de l'état.
    """

    name = ""
