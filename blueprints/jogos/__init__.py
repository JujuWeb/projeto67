from flask import Blueprint
jogos_bp = Blueprint("jogos", __name__, template_folder="templates")

from . import routes