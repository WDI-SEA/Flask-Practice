from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('index.html', name=name)

ingredients = ["sugar", "flour", "butter", "fruit"]

@app.route('/pie')
def pie():
    global ingredients
    return jsonify({'pie ingredient': ingredients[1]})