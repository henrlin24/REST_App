import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

# for use with 'flask shell'
# decorator registers function as shell context function, which will then run when 'flask shell' is run
@app.shell_context_processor
def make_shell_context():
  # returns dictionary of reference name within shell and associated item
  return {'sa': sa, 'so': so, 'app': app, 'db': db, 'User': User, 'Post': Post}