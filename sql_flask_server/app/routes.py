# module to handle different URLs for the application
from app import app

# view functions, which are mapped to one or more route URLs, and tell Flask what logic to respond with for different URLs
# the '@app.route' lines are decorators, a unique feature to Python, which modifies the function that follows
# the '@app.route' lines specifically associate the URL(s) specified as arguments with the function
@app.route('/')
@app.route('/index')
def index():
  return "Hello, world!"