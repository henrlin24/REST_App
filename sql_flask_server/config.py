# module to configure secret key for Flask app, external to app modules
import os
# retrieve file path to current file
basedir = os.path.abspath(os.path.dirname(__file__))

# custom 'Config' class, where more configuration items can be added as needed.
class Config:
  # secret key value is used in Flask applications as a cryptographic key for generating things like tokens and signatures.
  # Flask-WTF uses this value to protect web forms against CSRF attacks
  # set to retrieve an environment variable from the OS for the key, but if missing otherwise uses a hard coded string
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'insert-really-good-password-here'

  # take location of app's database. Either from the environment variable, or create a database dubbed 'app.db' in the current folder
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')