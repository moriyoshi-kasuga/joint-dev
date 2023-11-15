from flask import render_template

def signup_route(app):
    @app.route('/signup', methods=['POST','GET'])
    def signup():
        return render_template('signup.html')