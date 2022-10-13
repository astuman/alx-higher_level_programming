#!/usr/bin/python3
"""
create model_city.py
"""

import sqlalchemy
from sqlalchemy import column, Integer, String, ForeignKey
from model_state import Bas, State

class city(Base):
    """defining city class"""
    __tablename__ = "cities"
    id = column(Integer, primary_key=True)
    name = column(String(128), nullable=False)
    state_id = column(Integer, ForeignKey('states.id'))

