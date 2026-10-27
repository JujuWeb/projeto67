from operator import index
from models import Usuario, Jogo, Categoria
from flask import render_template, request, redirect, url_for, session
from blueprints.jogos import jogos_bp
from banco import db

@jogos_bp.route("/inicio", methods=["GET", "POST"])
def inicio():
    user = Usuario.query.get(session["user_id"])
    categorias = Categoria.query.all()
    categoria_id = request.args.get("categoria", type=int)

    if categoria_id:
        jogos = Jogo.query.filter_by(categoria_id=categoria_id).all()
    else:
        jogos = Jogo.query.all()
    return render_template("jogos/inicio.html", user=user, jogos=jogos, categorias=categorias, categoria_id=categoria_id)

@jogos_bp.route("/jogo/<int:id>", methods=["GET", "POST"])
def jogo(id):
    jogo = Jogo.query.get(id)
    return render_template("jogos/jogo.html", jogo=jogo)