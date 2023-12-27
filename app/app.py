import os

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}".format(
    user=os.environ.get("POSTGRES_USER"),
    passwd=os.environ.get("POSTGRES_PASSWORD"),
    host=os.environ.get("POSTGRES_HOST"),
    port=int(os.environ.get("POSTGRES_PORT", 5432)),
    db=os.environ.get("POSTGRES_DB"),
)

from models import db  # noqa: E402
from models import User  # noqa: E402

login = LoginManager(app)
login.login_view = "login"


@login.user_loader
def load_user(id):
    return User.query.get(id)


db.init_app(app)
migrate = Migrate(app, db)

from route import main  # noqa: E402

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
