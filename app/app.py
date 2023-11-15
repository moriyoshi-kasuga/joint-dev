import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from route.create import add_create_route
from route.thread import thread_route
from route.login import login_route
from route.signup import signup_route

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}".format(
    user=os.environ.get("POSTGRES_USER"),
    passwd=os.environ.get("POSTGRES_PASSWORD"),
    host=os.environ.get("POSTGRES_HOST"),
    port=os.environ.get("POSTGRES_PORT"),
    db=os.environ.get("POSTGRES_DB"),
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

add_create_route(app)
thread_route(app)
login_route(app)
signup_route(app)

class students(db.Model):
    id = db.Column("student_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))

    def __init__(self, name, city, addr):
        self.name = name
        self.city = city
        self.addr = addr


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
