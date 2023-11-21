from flask import Blueprint

products = Blueprint('Products', __name__)

@products.route('/', methods=['GET'])
def index():
    return []

@products.route('/<int:product_id>', methods=['GET'])
def get(product_id):
    return {}
