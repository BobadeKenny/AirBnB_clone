#!/usr/bin/python3
"""
the class City that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """City Class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialisation
        """
        super().__init__(*args, **kwargs)
