from flask import Blueprint, render_template

# Cria um blueprint para as rotas do petshop
bp = Blueprint('petshop', __name__, url_prefix='/')

# Rota para a tela inicial
@bp.route('/')
def home():
    return render_template('index.html')

# Rota de exemplo para o dashboard
@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')