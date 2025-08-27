from petshop import create_app

# Cria a instância da aplicação
app = create_app()

# Executa o servidor, se o script for chamado diretamente
if __name__ == '__main__':
    app.run(debug=True)