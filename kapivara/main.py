from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
db = SQLAlchemy(app)

from common.db import *
from common.estoque import *


@app.route("/")
def index():
    return "<h1>TESTE</h1>"


if __name__ == "__main__":
    app.run(debug=True)
