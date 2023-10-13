#!/usr/bin/env python3
import uuid
from datetime import datetime
import models.engine.storage as storage


# Create the BaseModel class

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def validate(self):
        """Validate the attributes of the object before saving."""
        for key, value in self.__dict__.items():
            if key == 'name' and not value:
                raise ValueError("Name cannot be empty")
            # add more validations here

    def delete(self):
        """Delete the object from the storage engine."""
        storage.delete(self)

    def to_dict(self, nested=False):
        """Return a dictionary representation of the BaseModel object.

        If nested is True, include nested models as dictionaries.
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
        """Save the object to the storage engine."""
        storage.save(self)
