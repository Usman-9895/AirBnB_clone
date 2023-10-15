#!/usr/bin/python3
'''créez une instance FileStorage unique pour l'application'''
from models.engine.file_storage import FileStorage

'''Un stockage variable, une instance de FileStorage'''
storage = FileStorage()
storage.reload()
