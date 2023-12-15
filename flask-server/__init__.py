import os

from flask import Flask

# application factory function, default sets test_config to be None
def create_app(test_config=None):
  print("Hello world")

  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    database=os.path.join(app.instance_path, 'jpr.sqlite')
  )

  # for any config presets to load in
  if test_config is None:
      # overwrites with config file with instance folder, if it exists, when not testing
      # silent=True allows for "silent" failures when load fails, aka no config preset to load
      app.config.from_pyfile('config.py', silent=True)
  else:
      # load the test config if passed in
      # allows for test configs, separate from deployment config
      app.config.from_mapping(test_config)

  # ensure instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # test route to return a simple page on URL '/hello'
  @app.route('/hello')
  def hello():
    return 'Hello, World!'

  return app