from flask import Flask

def create_app():
    # Cria a instância da aplicação Flask
    app = Flask(__name__)

    # Importa as rotas
    from . import routes
    app.register_blueprint(routes.bp)

    return app