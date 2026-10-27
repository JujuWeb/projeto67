from flask import render_template, request, redirect, url_for, session
from blueprints.jogos import jogos_bp

@jogos_bp.route("/inicio", methods=["GET", "POST"])
def inicio():
    return render_template("jogos/inicio.html")

@jogos_bp.route("/jogo")
def jogo():
    return render_template("jogos/jogo.html")

@jogos_bp.route("/jogo2")
def jogo2():
    return render_template("jogos/jogo2.html")