# created by following Miguel Grinberg's Flask Mega Tutorial
# '__init__' module for backend API package, defines the Flask application instance
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)  # imports custom Config class object, using it to configure the Flask app's configuration
db = SQLAlchemy(app)            # represents the database as an object
migrate = Migrate(app, db)      # represents the database migration engine
login = LoginManager(app)       # login manager, handles user logged-in state
login.login_view = 'login'      # configure Flask_login, allows redirecting to login page when accesing certain pages - allows for decorator @login_required to be used

# import statement at end of module avoids "circular imports", where modules attempt to reference each other before either are full loaded
from app import routes, models