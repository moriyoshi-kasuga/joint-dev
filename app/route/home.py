from flask import render_template

from . import main


@main.route("/", methods=["POST", "GET"])
def index():
    return render_template("home.html")
