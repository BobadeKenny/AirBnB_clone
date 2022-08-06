#!/usr/bin/python3
"""
the class Review that inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initialisation
        """
        super().__init__(*args, **kwargs)
