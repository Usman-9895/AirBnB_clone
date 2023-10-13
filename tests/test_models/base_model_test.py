#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_base_model_creation(self):
        """Test the creation of a BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_base_model_attributes(self):
        """Test the attributes of the BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_base_model_string_representation(self):
        """Test the string representation of a BaseModel instance."""
        model = BaseModel()
        expected_format = "[BaseModel] ({})".format(model.id)
        self.assertEqual(expected_format, str(model))


    def test_base_model_save_method(self):
        """Test the save method of a BaseModel instance."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_base_model_to_dict_method(self):
        """Test the to_dict method of a BaseModel instance."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_base_model_nested_models(self):
        """Test support for nested models in the to_dict method."""
        model = BaseModel()
        model.children = [BaseModel(), BaseModel()]
        model_dict = model.to_dict(nested=True)
        self.assertIsInstance(model_dict['children'], list)
        self.assertEqual(len(model_dict['children']), 2)
        self.assertEqual(model_dict['children'][0]['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
