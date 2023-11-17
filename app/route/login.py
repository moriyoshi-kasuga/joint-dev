from flask import render_template

from . import main


@main.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")
