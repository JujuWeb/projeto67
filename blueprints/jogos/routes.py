from operator import index
from models import Usuario, Jogo
from flask import render_template, request, redirect, url_for, session
from blueprints.jogos import jogos_bp
from banco import db

@jogos_bp.route("/inicio", methods=["GET", "POST"])
def inicio():
    user = Usuario.query.get(session["user_id"])
    jogos = Jogo.query.all()
    return render_template("jogos/inicio.html", user=user, jogos=jogos)

@jogos_bp.route("/jogo/<int:id>", methods=["GET", "POST"])
def jogo(id):
    jogo = Jogo.query.get(id)
    return render_template("jogos/jogo.html", jogo=jogo)