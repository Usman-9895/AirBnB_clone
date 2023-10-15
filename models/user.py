#!/usr/bin/python3
"""Il s'agit du module Modèle utilisateur.

Contient la classe User qui hérite de BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Cette classe définit un utilisateur.

    Les attributs:
        email (str): l'e-mail de l'utilisateur.
        password (str) : le mot de passe de l'utilisateur.
        first_name (str): le prénom de l'utilisateur.
        last_name (str): le nom de famille de l'utilisateur.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
