from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from app import User
import datetime

def signup_route(app, db):
    @app.route('/signup', methods=['POST'])
    def signup():
        id = str(uuid4())
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        created_at = datetime.now()

        new_user = User(id=id, name=name, email=email, password=password, created_at=created_at)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201