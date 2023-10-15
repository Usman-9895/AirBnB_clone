#!/usr/bin/python3
"""créer une instance FileStorage unique pour votre application"""
from models.engine.file_storage import FileStorage

"""Un stockage variable, une instance de FileStorage"""
storage = FileStorage()
storage.reload()