# module to handle different URLs for the application
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

# app route '/login' handles both 'GET' and 'POST' HTTP requests
@app.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm()
  # returns true if 'there is an active request' and the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
  if form.validate_on_submit():
    # shows a message to user, stored on Flask message buffer
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data) )
    # has browser automatically redirect to different URL
    # url_for automatically retrieves the URL associates with a view function of the same name as the argument
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)