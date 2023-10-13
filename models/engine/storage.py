#!/usr/bin/env python3

import json

class JSONStorage:
    def __init__(self, filename="models.json"):
        self.filename = filename

    def save(self, model):
        """Save a BaseModel object to JSON."""
        model_json = model.to_dict()
        with open(self.filename, "w") as f:
            json.dump(model_json, f)

    def load(self, id):
        """Load a BaseModel object from JSON."""
        with open(self.filename, "r") as f:
            model_json = json.load(f)

        model = BaseModel(**model_json)
        return model

    def delete(self, model):
        """Delete a BaseModel object from JSON."""
        with open(self.filename, "r") as f:
            model_json = json.load(f)

        model_id = model.id
        if model_id in model_json:
            del model_json[model_id]

        with open(self.filename, "w") as f:
            json.dump(model_json, f)


