from flask import redirect, render_template, request, url_for
from flask_login import logout_user

from . import main


@main.route("/logout", methods=["POST", "GET"])
def logout():
    if request.method == "POST":
        logout_user()
        return redirect(url_for("login"))
    return render_template("logout.html")
