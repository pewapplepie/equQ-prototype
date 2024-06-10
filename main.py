from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route("/")
def index():
    return 'TEST'

if __name__ in '__main__':
    app.run(debug=True)