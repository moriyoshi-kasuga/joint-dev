from flask import Blueprint

main = Blueprint("main", __name__)

from . import create, index, login, signup, thread  # noqa: E402
