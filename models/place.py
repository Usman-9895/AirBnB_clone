#!/usr/bin/python3
"""This is the Place Model module.

Contains the Place class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Cette classe définit un lieu.

    Les attributs:
        city_id (str) : l'identifiant de la ville du lieu.
        user_id (str): l'identifiant de l'utilisateur du lieu.
        name (str): le nom du lieu.
        description (str): la description du lieu.
        number_rooms (int) : le nombre de pièces du lieu.
        number_bathrooms (int) : le nombre de salles de bains du lieu.
        max_guest (int) : le nombre maximum d'invités du lieu.
        price_by_night (int) : le prix du lieu par nuit.
        latitude (float) : la latitude du lieu.
        longitude (float) : la longitude du lieu.
        amenity_ids (list) : la liste des identifiants des commodités du lieu.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
