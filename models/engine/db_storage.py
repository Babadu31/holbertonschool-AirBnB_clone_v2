#!/usr/bin/python3
""" this module contains the database storage engine for AirBnB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from os import getenv


class DBStorage:
    """ dbstorage engine """
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """ instantiation """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(
                        getenv('HBNB_MYSQL_USER'),
                        getenv('HBNB_MYSQL_PWD'),
                        getenv('HBNB_MYSQL_HOST'),
                        getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session)
        all objects depending of the class name"""
        d = {}
        if cls is None:
            for c in self.all_classes:
                c = eval(c)
                for instance in self.__session.query(c).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    d[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                d[key] = instance
        return d

    def new(self, obj):
        """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ creates database tables and session """
        Base.metadata.create_all(self.__engine)
        sessionf = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionf)
        self.__session = Session()

    def close(self):
        self.__session.close()
