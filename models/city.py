#!/usr/bin/python3
"""This is the City Model module.

Contains the City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Cette classe définit une ville.

    Les attributs:
        state_id (str) : l'identifiant de l'état de la ville.
        name (str) : le nom de la ville.
    """

    state_id = ""
    name = ""
