#!/usr/bin/python3
"""Defines the City model for SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """Represents a city in the cities database table."""

    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
