from flask import jsonify, render_template, request
from models import User, db

from . import main

@main.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return render_template("register.html")
