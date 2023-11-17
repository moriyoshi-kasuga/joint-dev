from flask import render_template

def add_create_route(app, db):
    @app.route("/create", methods=["POST", "GET"])
    def create():
        return render_template("create.html")