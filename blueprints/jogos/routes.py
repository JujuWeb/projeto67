from operator import index
from models import Usuario, Jogo, Categoria, Criador
from flask import render_template, request, redirect, url_for, session
from urllib.parse import urlparse
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

@jogos_bp.route("/favoritar/<int:id>", methods=["POST"])
def favoritar(id):
    user = Usuario.query.get_or_404(session["user_id"])
    jogo = Jogo.query.get_or_404(id)
    if jogo in user.jogos_favoritos:
        user.jogos_favoritos.remove(jogo)
    else:
        user.jogos_favoritos.append(jogo)

    db.session.commit()
    return redirect(request.referrer or url_for("jogos.inicio"))


@jogos_bp.route("/jogo/novo", methods=["GET", "POST"])
def criar_jogo():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    categorias = Categoria.query.all()
    criadores = Criador.query.all()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        descricao = request.form.get("descricao", "").strip()
        ano = request.form.get("ano_lancamento", "").strip()
        imagem_url = request.form.get("imagem_url", "").strip()
        url_jogo = request.form.get("url_jogo", "").strip()
        categoria_id = request.form.get("categoria_id", type=int)
        criador_id = request.form.get("criador_id", type=int)
        novo_criador = request.form.get("novo_criador", "").strip()

        categoria = db.session.get(Categoria, categoria_id)

        if not nome:
            erro = "informe o nome do jogo"
        elif not categoria:
            erro = "selecione uma categoria válida"
        elif ano and not ano.isdigit():
            erro = "o ano de lançamento deve ser um número"
        elif novo_criador:
            criador = Criador(nome=novo_criador)
            db.session.add(criador)
            db.session.flush()
            erro = None
        elif criador_id:
            criador = db.session.get(Criador, criador_id)
            erro = None if criador else "selecione um criador válido"
        else:
            erro = "selecione um criador ou informe um novo nome"

        if erro:
            return render_template( "jogos/criar.html", categorias=categorias, criadores=criadores, erro=erro)

        jogo = Jogo(
            nome=nome,
            descricao=descricao or None,
            ano_lancamento=int(ano) if ano else None,
            imagem_url=imagem_url or None,
            url_jogo=url_jogo or None,
            categoria_id=categoria.id,
            criador_id=criador.id
        )
        db.session.add(jogo)
        db.session.commit()

        return redirect(url_for("jogos.inicio"))
    return render_template("jogos/criar.html", categorias=categorias, criadores=criadores)