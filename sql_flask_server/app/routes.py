# module to handle different URLs for the application
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required # current_user can be referenced at any time during request handling to obtain user object representing request client
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm
from app.models import User
from urllib.parse import urlsplit

# view functions, which are mapped to one or more route URLs, and tell Flask what logic to respond with for different URLs
# the '@app.route' lines are decorators, a unique feature to Python, which modifies the function that follows
# the '@app.route' lines specifically associate the URL(s) specified as arguments with the function
# the '@login_required' line redirects the user to login before accesing the page, and facilates returning to the page after login
@app.route('/')
@app.route('/index')
@login_required
def index():
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
  return render_template('index.html', title='Home', posts=posts)

# app route '/login' handles both 'GET' and 'POST' HTTP requests
@app.route('/login', methods = ['GET', 'POST'])
def login():
  # if user is logged in, redirect to home page
  if current_user.is_authenticated:
    return redirect(url_for("index"))
  
  form = LoginForm()
  # returns true if 'there is an active request' and the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
  if form.validate_on_submit():
    # shows a message to user, stored on Flask message buffer
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data) )

    # form and carry out query for user of matching username
    user = db.session.scalar(
      sa.select(User).where(User.username == form.username.data)
    )
    # if user is not found, or if submitted password is incorrect, flash error message and return login page
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for("login"))

    # if user found
    # login user, setting remember_me status to submitted remember_me value on login form
    login_user(user, remember=form.remember_me.data)
    flash("user {} successfully logged in".format(form.username.data))

    # handle any 'next' query strings in the login request
    next_page = request.args.get('next')                      # is dictionary, fun!
    # handles 3 possible cases: no argument for 'next', valid relative URL, or a full URL with a domain name (which is ignored for security) indicated by a non-empty netloc property
    if not next_page or urlsplit(next_page).netloc != '':     
      next_page = url_for('index')
    # has browser automatically redirect to different URL
    # url_for automatically retrieves the URL associates with a view function of the same name as the argument
    return redirect(next_page)
  return render_template('login.html', title='Sign In', form=form)

# logout function
@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))