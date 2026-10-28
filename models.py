from banco import db

usuario_jogo = db.Table(
    "usuario_jogo",
    db.Column("usuario_id", db.Integer, db.ForeignKey("usuario.id"), primary_key=True),
    db.Column("jogo_id", db.Integer, db.ForeignKey("jogo.id"), primary_key=True)
)

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    jogos_favoritos = db.relationship("Jogo", secondary=usuario_jogo, back_populates="usuarios_favoritaram")

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
    imagem_url = db.Column(db.String(500), nullable=True)
    url_jogo = db.Column(db.String(500), nullable=True)
    usuarios_favoritaram = db.relationship("Usuario", secondary=usuario_jogo, back_populates="jogos_favoritos")

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
        "descricao": "Jogo de plataforma com dois personagens e habilidades elementais.",
        "ano_lancamento": 2009,
        "criador_id": 1,
        "categoria_id": 1,
        "imagem_url": "/static/assets/AguaFogo.jpg",
        "url_jogo": "https://www.clickjogos.com.br/jogos-de-acao/fireboy-and-watergirl-1-in-forest-temple",
    },
    {
        "id": 2,
        "nome": "Cookie Clicker",
        "descricao": "Jogo incremental em que o jogador produz cookies e compra melhorias.",
        "ano_lancamento": 2013,
        "criador_id": 2,
        "categoria_id": 2,
        "imagem_url": "/static/assets/Biscoito.png",
        "url_jogo": "https://quackprep.org/class/cookie-clicker",
    },
    {
        "id": 3,
        "nome": "Plants vs. Zombies",
        "descricao": "Jogo de estratégia em que plantas defendem a casa contra zumbis.",
        "ano_lancamento": 2009,
        "criador_id": 3,
        "categoria_id": 3,
        "imagem_url": "/static/assets/PlantaZumbi.webp",
        "url_jogo": "https://www.crazygames.com/game/plants-vs-zombies",
    },
    {
        "id": 4,
        "nome": "Damas",
        "descricao": "Jogo de tabuleiro para dois jogadores.",
        "ano_lancamento": None,
        "criador_id": 4,
        "categoria_id": 4,
        "imagem_url": "/static/assets/Damas.jpg",
        "url_jogo": "https://www.crazygames.com/game/checkers-2",
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
