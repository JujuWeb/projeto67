from banco import db

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

class Jogo(db.Model):
    __tablename__ = "jogo"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    ano_lancamento = db.Column(db.Integer, nullable=True)
    criador_id = db.Column(db.Integer, db.ForeignKey("criador.id"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)
    criador = db.relationship("Criador", backref=db.backref("jogos", lazy=True))
    categoria = db.relationship("Categoria", backref=db.backref("jogos", lazy=True))

class Criador(db.Model):
    __tablename__ = "criador"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Categoria(db.Model):
    __tablename__ = "categoria"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)