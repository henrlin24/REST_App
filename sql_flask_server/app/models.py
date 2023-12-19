# defines the user database model (e.g. object representation of a row/entry within the user database)
from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa       # provides general purpose database functions & classes, like types and query build helpers
import sqlalchemy.orm as so   # provides support for using models
from app import db

# User class inherits from db.Model, base class for all models in SQLAlchemy
class User(db.Model):
  # tables generated automatically use snake_case for table names
  # can specify specific table name with field '__tablename__'

  # python type mapping - specifies variable 'id' is of type 'so.Mapped[int]', as well as makes the field non-nullable/required
  # so.Mapped is SQLAlchemy's generic type
  # so.mapped_column() allows for configurations through parameters
  id: so.Mapped[int] = so.mapped_column(primary_key=True)                               # marks field as primary_key
  username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)   # sets string max length, set column to be indexed for faster search, and if values should be unique
  email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
  password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))                 # optional key allows column to be optional/nullable

  # NOT actual database field. High-level view of relationship between user and post, and allows app to access connected user and posts entries
  # so.relationship is a model class that references the other side of the relationship, thus associating the corresponding attributes of the relationship
  # WriteOnlyMapped defines posts as a colleciton type with Post objects inside
  posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

  # tells Python how to print out objects of the class
  # good for debug use
  def __repr__(self):
    return '<User - {}>'.format(self.username)
  
class Post(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  body: so.Mapped[str] = so.mapped_column(sa.String(140))
  # in general, servers will want to use UTC rather than local times. can be converted to local time on view.
  timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
  # set as foreign key to User.id, so it references values fromt the 'id' column in the Users table
  # index not always created automatically for foreign keys, so need to create explictly
  user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
  
  author: so.Mapped[User] = so.relationship(back_populates='posts')
  
  def __repr__(self):
    return '<Post - {} @time {}'.format(self.body, self.timestamp)