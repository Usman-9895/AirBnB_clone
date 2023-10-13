#!/usr/bin/env python3
import uuid
from datetime import datetime
import models.engine.storage as storage


# Create the BaseModel class

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    setattr(self, key, type(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def validate(self):
        """Validates the attributes of the object before saving."""
        for key, value in self.__dict__.items():
            if key == 'name' and not value:
                raise ValueError("Name cannot be empty")
            # add more validations here

            if not isinstance(self.id, uuid.UUID):
                raise ValueError("Id must be a valid UUID")

    def delete(self):
        """Deletes the object from the storage engine."""
        storage.delete(self)

    def to_dict(self, nested=False):
        """Returns a dictionary representation of the BaseModel object.

        If nested is True, includes nested models as dictionaries.
        """
        model_dict = self.__dict__.copy()
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        model_dict['__class__'] = self.__class__.__name__

        if nested:
            if hasattr(self, 'children'):
                model_dict['children'] = [c.to_dict() for c in self.children]

        return model_dict

    def save(self):
        """Saves the object to the storage engine."""
        self.updated_at = datetime.now()
        storage.save(self)

    @classmethod
    def from_dict(cls, model_dict):
        """Creates a new BaseModel instance from a dictionary representation."""
        return cls(**model_dict)
