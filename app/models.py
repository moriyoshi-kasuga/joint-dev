from datetime import datetime
from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    threads = db.relationship("Thread", backref="user")
    comments = db.relationship("Comment", backref="user")

    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)


threads_tags = db.Table(
    "threads_tags",
    db.Column("threads_id", UUID(as_uuid=True), db.ForeignKey("threads.id")),
    db.Column("tags_id", UUID(as_uuid=True), db.ForeignKey("tags.id")),
)


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(20), unique=True, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)


class Thread(db.Model):
    __tablename__ = "threads"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = db.Column(db.String(100), nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))
    comments = db.relationship("Comment", backref="thread")
    tags = db.relationship("Tag", secondary=threads_tags, backref="threads")

    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))
    thread_id = db.Column(UUID(as_uuid=True), db.ForeignKey("threads.id"))

    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
