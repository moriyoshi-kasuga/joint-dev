from flask import render_template

from . import main


@main.route("/thread", methods=["POST", "GET"])
def thread():
    return render_template("thread.html")
