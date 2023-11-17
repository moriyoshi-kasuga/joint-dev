from flask import render_template

from . import main


@main.route("/create", methods=["POST", "GET"])
def create():
    return render_template("create.html")
