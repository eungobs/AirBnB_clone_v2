#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """ Review class representing the reviews table """

    __tablename__ = 'reviews'

    id = Column(String(60), primary_key=True, nullable=False)
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Relationships
    user = relationship('User', backref='reviews')
    place = relationship('Place', backref='reviews')
