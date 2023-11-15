from flask import render_template

def thread_route(app):
    @app.route("/thread", methods=["POST","GET"])
    def thread():
        return render_template('thread.html')