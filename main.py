from flask import Flask
from config import Config
from products.main import products

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(products, url_prefix="/products")
