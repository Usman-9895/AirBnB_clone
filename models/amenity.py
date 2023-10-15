#!/usr/bin/python3
"""Il s'agit du module Modèle d'agrément.

Contient la classe Amenity qui hérite de BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Cette classe définit un agrément.

    Les attributs:
        name (str) : le nom de l'équipement.
    """

    name = ""