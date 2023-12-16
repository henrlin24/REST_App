from flask import Flask

app = Flask(__name__)

@app.route("/members")
def members():
  return {"members" : ["Member1", "Member2", "Member3"]}

if (True):
  app.run(debug=True)