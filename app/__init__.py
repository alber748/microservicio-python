from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    jwt = JWTManager(app)

    with app.app_context():
        from . import routes  # Importa las rutas para registrarlas con la aplicación
        db.create_all()  # Crea las tablas en la base de datos

    return app
