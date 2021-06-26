from flask import Flask


def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/raiz')
def raiz():
    return 'Olá, mundo'