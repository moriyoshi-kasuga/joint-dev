import os
from uuid import uuid4

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from route.create import add_create_route
from route.login import login_route
from route.signup import signup_route
from route.thread import thread_route
from sqlalchemy.dialects.postgresql import UUID

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


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    threads = db.relationship("Thread", backref="user")
    comments = db.relationship("Comment", backref="user")

    created_at = db.Column(db.DateTime, server_default=db.func.now())


threads_tags = db.Table(
    "threads_tags",
    db.Column("threads_id", UUID(as_uuid=True), db.ForeignKey("threads.id")),
    db.Column("tags_id", UUID(as_uuid=True), db.ForeignKey("tags.id")),
)


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(20), unique=True, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Thread(db.Model):
    __tablename__ = "threads"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = db.Column(db.String(100), nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))
    comments = db.relationship("Comment", backref="thread")
    tags = db.relationship("Tag", secondary=threads_tags, backref="threads")

    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))
    thread_id = db.Column(UUID(as_uuid=True), db.ForeignKey("threads.id"))

    created_at = db.Column(db.DateTime, server_default=db.func.now())


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
