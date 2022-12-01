#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storage


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """  getter attribute cities that returns the list of
        City instances with state_id equals to the current State.id """
            allcities = storage.all(City)
            city_list = []

            for city in allcities.values():
                if city.state_id == self.id:
                    city_list.append(city)
        
            return city_list