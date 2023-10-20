#!/usr/bin/python3
"""Test for the console"""

import unittest
import console
from console import HBNBCommand
from unittest import mock


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = Console()

    def test_create(self):
        with mock.patch('models.storage.save') as mock_save:
            self.console.do_create('BaseModel')
            mock_save.assert_called_once()

    def test_show(self):
        with mock.patch('models.storage.all') as mock_all:
            mock_all.return_value = {'BaseModel.1': BaseModel()}
            self.console.do_show('BaseModel', '1')
            mock_all.assert_called_once()

    def test_destroy(self):
        with mock.patch('models.storage.all') as mock_all:
            mock_all.return_value = {'BaseModel.1': BaseModel()}
            self.console.do_destroy('BaseModel', '1')
            mock_all.assert_called_once()

    def test_all(self):
        with mock.patch('models.storage.all') as mock_all:
            mock_all.return_value = {'BaseModel.1': BaseModel()}
            self.console.do_all('BaseModel')
            mock_all.assert_called_once()

    def test_update(self):
        with mock.patch('models.storage.all') as mock_all:
            mock_all.return_value = {'BaseModel.1': BaseModel()}
            self.console.do_update('BaseModel', '1', 'name', 'John Doe')
            mock_all.assert_called_once()

    def test_count(self):
        with mock.patch('models.storage.all') as mock_all:
            mock_all.return_value = {'BaseModel.1': BaseModel()}
            self.console.do_count('BaseModel')
            mock_all.assert_called_once()


if __name__ == '__main__':
    unittest.main()

