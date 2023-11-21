# Nie restartuje przy zmianach:
# flask --app main run

# Restart przy zmianie
# flask --app main --debug run
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hello/<name>', methods=["POST"])
def say_hello(name):
    return f"Hello {name}!"