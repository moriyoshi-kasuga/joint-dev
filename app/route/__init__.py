from flask import Blueprint

main = Blueprint("main", __name__)

from . import create, home, login, thread, logout, register  # noqa
