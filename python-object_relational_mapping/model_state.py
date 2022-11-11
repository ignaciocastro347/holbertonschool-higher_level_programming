#!/usr/bin/python3
"""
    State model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ State Class """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, uniqe=True, nullable=False)
    name =  Column(String(128), nullable=False)