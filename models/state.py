#!/usr/bin/python3
"""
the class State that inherits from BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialisation
        """
        super().__init__(*args, **kwargs)
