# module to handle different URLs for the application
from flask import render_template
from app import app

# view functions, which are mapped to one or more route URLs, and tell Flask what logic to respond with for different URLs
# the '@app.route' lines are decorators, a unique feature to Python, which modifies the function that follows
# the '@app.route' lines specifically associate the URL(s) specified as arguments with the function
@app.route('/')
@app.route('/index')
def index():
  # mock user
  user = {'username': 'Henry'}

  # mock posts
  posts = [
    {
      'author' : {'username': 'John'},
      'body' : 'Beautiful day! Somewhere, at least.'
    },
    {
      'author' : {'username': 'Doe'},
      'body': 'I\'m at somewhere!'
    }
  ]

  # returns a rendered complete HTML page using the template provided, using the jinja template engine bundled with Flask
  return render_template('index.html', title='Home', user=user, posts=posts)