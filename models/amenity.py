#!/usr/bin/python3
"""
the class Amenity that inherits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialisation
        """
        super().__init__(*args, **kwargs)
