from datetime import datetime
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=user.password,
        full_name=user.full_name,
        disabled=False,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(
        title=post.title,
        warm_up=post.warm_up,
        conditioning=post.conditioning,
        timestamp=datetime.utcnow(),
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def create_main_lift_set(
    db: Session, main_lift_set: schemas.MainLiftSetCreate, post_id: int
):
    db_item = models.MainLiftSet(**main_lift_set.dict(), post_id=post_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_accessory_lift(
    db: Session, accessory_lift: schemas.AccessoryLiftCreate, post_id: int
):
    db_item = models.AccessoryLift(**accessory_lift.dict(), post_id=post_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
