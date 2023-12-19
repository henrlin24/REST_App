# created by following Miguel Grinberg's Flask Mega Tutorial
# '__init__' module for backend API package, defines the Flask application instance
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # imports custom Config class object, using it to configure the Flask app's configuration

# import statement at end of module avoids "circular imports", where modules attempt to reference each other before either are full loaded
from app import routes