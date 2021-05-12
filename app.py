from flask import Flask, request, jsonify
from datetime import datetime
from database.komercio import produtos

app = Flask(__name__)


@app.route('/products/<int:product>')
def hello_flask(product):
    for produto_id in produtos:
        if produto_id['id'] == product:
            return jsonify(produto_id)
    return ('', 404)


@app.route('/products/')
def hello():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    if page and per_page:
        page = int(page)
        per_page = int(per_page)
        return jsonify(produtos[per_page * page - per_page:per_page * page])
    
