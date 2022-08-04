#!/usr/bin/python3
"""
handles the module initialization
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
