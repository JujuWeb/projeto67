from app import app
from banco import db
from models import criar_tabelas, cadastrar_dados

with app.app_context():
    criar_tabelas()
    cadastrar_dados()