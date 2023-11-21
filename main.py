from flask import Flask
from products.main import products

app = Flask(__name__)
app.register_blueprint(products, url_prefix="/products")

