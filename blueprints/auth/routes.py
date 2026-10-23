from flask import render_template, request, redirect, url_for, session
from blueprints.auth import auth_bp

@auth_bp.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        return redirect(url_for("auth.login", nome=nome, senha=senha))
    return render_template("auth/cadastro.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        user = Usuario(nome=nome, senha=senha)
        if user and user.senha == senha:
            session["user_id"] = user.id
            return redirect(url_for("jogos.inicio"))
    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(debug=True)