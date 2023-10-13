#!/usr/bin/env python3

class Storage:
    def save(self, model):
        """Save the model to the storage engine."""
        raise NotImplementedError()

    def get(self, class_name, id):
        """Get a model from the storage engine."""
        raise NotImplementedError()
