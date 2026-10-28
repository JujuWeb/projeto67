from flask import Flask
from blueprints.auth import auth_bp
from blueprints.jogos import jogos_bp
from banco import db

app = Flask(__name__)
app.secret_key = "batata"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///catalogo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(jogos_bp)

if __name__ == "__main__":
    app.run(debug=True)