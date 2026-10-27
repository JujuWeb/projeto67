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

categorias = [
    {"id": 1, "nome": "Plataforma"},
    {"id": 2, "nome": "Incremental"},
    {"id": 3, "nome": "Estratégia"},
    {"id": 4, "nome": "Tabuleiro"},
]

criadores = [
    {"id": 1, "nome": "Oslo Albet"},
    {"id": 2, "nome": "Julien Thiennot"},
    {"id": 3, "nome": "PopCap Games"},
    {"id": 4, "nome": "Desconhecido"},
]

jogos = [
    {
        "id": 1,
        "nome": "Água e Fogo",
        "descricao": "jogo de plataforma onde dois personagens resolvem desafios usando suas habilidades elementais",
        "ano_lancamento": 2009,
        "criador_id": 1,
        "categoria_id": 1,
    },
    {
        "id": 2,
        "nome": "Cookie Clicker",
        "descricao": "jogo incremental onde o jogador produz cookies ao clicar e compra melhorias para aumentar a produção",
        "ano_lancamento": 2013,
        "criador_id": 2,
        "categoria_id": 2,
    },
    {
        "id": 3,
        "nome": "Plants vs. Zombies",
        "descricao": "jogo de estratégia e defesa de torres onde plantas são usadas para proteger a casa contra zumbis",
        "ano_lancamento": 2009,
        "criador_id": 3,
        "categoria_id": 3,
    },
    {
        "id": 4,
        "nome": "Damas",
        "descricao": "jogo de tabuleiro para dois jogadores, com o objetivo de capturar as peças do adversário",
        "ano_lancamento": None,
        "criador_id": 4,
        "categoria_id": 4,
    },
]

def criar_tabelas():
    db.create_all()

def cadastrar_dados():
    if Categoria.query.count() == 0:
        db.session.add_all([Categoria(**dados) for dados in categorias])

    if Criador.query.count() == 0:
        db.session.add_all([Criador(**dados) for dados in criadores])
    db.session.commit()

    if Jogo.query.count() == 0:
        db.session.add_all([Jogo(**dados) for dados in jogos])
    db.session.commit()
