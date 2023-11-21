from flask import Blueprint, request, jsonify
from database import get_db

products = Blueprint('Products', __name__)

@products.route('/', methods=['GET'])
def index():
    db = get_db()
    cursor = db.execute('SELECT * FROM products')
    results = cursor.fetchall()
    results = [dict(row) for row in results]
    return jsonify(results)

@products.route('/<int:product_id>', methods=['GET'])
def get(product_id):
    return {}


@products.route('/', methods=['POST'])
def create():
    new_product = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO products(title, body,price) VALUES(?, ?, ?)', (
        new_product.get('title'),
        new_product.get('body'),
        new_product.get('price')
    ))
    db.commit()