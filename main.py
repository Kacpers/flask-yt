# Nie restartuje przy zmianach:
# flask --app main run

# Restart przy zmianie
# flask --app main --debug run
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello/<name>', methods=["GET"])
def say_hello(name):
    return render_template('say_hello.html', name=name)