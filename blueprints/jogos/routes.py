from flask import render_template, request, redirect, url_for, session
from blueprints.jogos import jogos_bp

@jogos_bp.route("/inicio", methods=["GET", "POST"])
def inicio():
    nome = session.get("nome")
    return render_template("jogos/inicio.html", nome=nome)

@jogos_bp.route("/jogo")
def jogo():
    return render_template("jogos/jogo.html")

@jogos_bp.route("/jogo2")
def jogo2():
    return render_template("jogos/jogo2.html")

@jogos_bp.route("/jogo3")
def jogo3():
    return render_template("jogos/jogo3.html")

@jogos_bp.route("/jogo4")
def jogo4():
    return render_template("jogos/jogo4.html")