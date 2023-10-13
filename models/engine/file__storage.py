#!/usr/bin/env python3

import json
from models.storage import Storage


class FileStorage(Storage):
    def save(self, model):
        """Saves the model to a JSON file."""
        model_dict = model.to_dict()

        with open(f"{model.__class__.__name__}.json", "w") as f:
            json.dump(model_dict, f)

    def get(self, class_name, id):
        """Gets a model from a JSON file."""
        with open(f"{class_name}.json", "r") as f:
            model_dict = json.load(f)

        model = BaseModel(**model_dict)

        return model
