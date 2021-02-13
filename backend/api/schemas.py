from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    hashed_password: str
    disabled: Optional[bool] = None

    class Config:
        orm_mode = True


class AccessoryLiftBase(BaseModel):
    lift: str
    sets: int
    reps: int
    weight: Optional[float]


class AccessoryLiftCreate(AccessoryLiftBase):
    pass


class AccessoryLift(AccessoryLiftBase):
    id: int
    post_id: int

    class Config:
        orm_mode = True


class MainLiftSetBase(BaseModel):
    lift: str
    set_order: int
    reps: int
    weight: float
    pr: bool


class MainLiftSetCreate(MainLiftSetBase):
    pass


class MainLiftSet(MainLiftSetBase):
    id: int
    post_id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    warm_up: Optional[str] = None
    conditioning: Optional[str] = None


class PostCreate(PostBase):
    main_lift_sets: List[MainLiftSetCreate] = []
    accessory_lifts: List[AccessoryLiftCreate] = []


class Post(PostBase):
    id: int
    timestamp: datetime
    main_lift_sets: List[MainLiftSet] = []
    accessory_lifts: List[AccessoryLift] = []

    class Config:
        orm_mode = True
