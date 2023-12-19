# defines the user database model (e.g. object representation of a row/entry within the user database)
from typing import Optional
import sqlalchemy as sa       # provides general purpose database functions & classes, like types and query build helpers
import sqlalchemy.orm as so   # provides support for using models
from app import db

# User class inherits from db.Model, base class for all models in SQLAlchemy
class User(db.Model):
  # python type mapping - specifies variable 'id' is of type 'so.Mapped[int]', as well as makes the field non-nullable/required
  # so.Mapped is SQLAlchemy's generic type
  # so.mapped_column() allows for configurations through parameters
  id: so.Mapped[int] = so.mapped_column(primary_key=True)                               # marks field as primary_key
  username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)   # sets string max length, set column to be indexed for faster search, and if values should be unique
  email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
  password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))                 # optional key allows column to be optional/nullable

  # tells Python how to print out objects of the class
  # good for debug use
  def __repr__(self):
    return '<User - {}>'.format(self.username)