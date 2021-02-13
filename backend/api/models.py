from typing import Optional
from pydantic.main import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    full_name = Column(String)
    disabled = Column(Boolean)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    warm_up = Column(String)
    conditioning = Column(String)
    timestamp = Column(DateTime)

    main_lift_sets = relationship(
        "MainLiftSet",
        back_populates="post",
        lazy="joined",
    )
    accessory_lifts = relationship(
        "AccessoryLift",
        back_populates="post",
        lazy="joined",
    )


class MainLiftSet(Base):
    __tablename__ = "main_lift_sets"
    id = Column(Integer, primary_key=True, index=True)
    lift = Column(String, index=True)
    set_order = Column(Integer, index=True)
    reps = Column(Integer)
    weight = Column(Float)
    pr = Column(Boolean)
    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship("Post", back_populates="main_lift_sets")


class AccessoryLift(Base):
    __tablename__ = "accessory_lifts"
    id = Column(Integer, primary_key=True, index=True)
    lift = Column(String, index=True)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float)
    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship("Post", back_populates="accessory_lifts")
