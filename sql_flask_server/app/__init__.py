# created by following Miguel Grinberg's Flask Mega Tutorial

# '__init__' module for backend API package, defines the Flask application instance
from flask import Flask

app = Flask(__name__)

# import statement at end of module avoids "circular imports", where modules attempt to reference each other before either are full loaded
from app import routes