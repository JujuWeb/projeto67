from flask import Flask
from blueprints.auth import auth_bp
from blueprints.jogos import jogos_bp

app = Flask(__name__)
app.secret_key = "batata"

app.register_blueprint(auth_bp)
app.register_blueprint(jogos_bp)

if __name__ == "__main__":
    app.run(debug=True)