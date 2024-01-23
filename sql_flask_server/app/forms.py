from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])        # ensures data entered matches structure of email address
  password = PasswordField('Password', validators=[DataRequired()])
  # reconfirms password, checking it matches with initial password entry
  password2 = PasswordField(
    'Re-confirm password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

  # validators of the pattern validate_<field_name>, WTForms recognizes them as custom validators and runs alongside stock validators
  def validate_username(self, username):
    # uses scalar() instead of scalars(), as its safe to assume only one result if any (None otherwise)
    user = db.session.scalar(sa.select(User).where(
      User.username == username.data
    ))
    if user is not None:
      raise ValidationError('The username {} is taken. Try a different username!'.format(username.data))
  
  def validate_email(self, email):
    email = db.session.scalar(sa.select(User).where(
      User.email == email.data
    ))
    if email is not None:
      raise ValidationError('The email {} is already in use. Try registering with a different email!'.format(email.data))