#!/usr/bin/python3
"""This is the Review Model module.

Contains the Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Cette classe définit une révision.

    Les attributs:
        place_id (str) : l'identifiant du lieu de l'avis.
        user_id (str) : l'identifiant utilisateur de l'émetteur de l'avis.
        text (str) : la critique.
    """

    place_id = ""
    user_id = ""
    text = ""
