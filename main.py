from flask import Flask
from config import Config
from products.main import products
from database import init_db, init_app

app = Flask(__name__)
app.config.from_object(Config)
init_app(app)
app.register_blueprint(products, url_prefix="/products")
