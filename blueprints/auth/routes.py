from flask import render_template, request, redirect, url_for, session
from blueprints.auth import auth_bp
from werkzeug.security import generate_password_hash, check_password_hash
from banco import db
from models import Usuario

@auth_bp.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = generate_password_hash(request.form["senha"])
        user = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("auth/cadastro.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        user = Usuario.query.filter_by(email=email).first()
        if user and check_password_hash(user.senha, senha):
            session["user_id"] = user.id
            return redirect(url_for("jogos.inicio"))
    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("auth.login"))