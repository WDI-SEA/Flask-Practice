from flask import Flask, render_template, jsonify
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greetings/<name>')
def greeting(name):
    return render_template('index.html', name=name)

@app.route('/pie')
def api_call():
    ingredients = ['apples', 'milk', 'dough', 'sugar', 'butts']
    return jsonify({'pie ingredient': random.choice(ingredients)})

    