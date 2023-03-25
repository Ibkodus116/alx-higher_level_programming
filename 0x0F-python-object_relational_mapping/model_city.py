#!/usr/bin/python3
"""
A Python file similar to model_state.py
named model_city.py that
contains the class definition of a City.
"""

from sqlalchemy import String, Column, Integer, ForeignKey
from model_state import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
        )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
