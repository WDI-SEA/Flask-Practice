from flask import Flask, render_template, jsonify
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/greeting/<name>')
def greetings(name):
    return render_template('index.html', name=name)

@app.route('/pie')
def ingredients_list():
    ingredients = ["apples", "brown sugar", "pie crust"]
    return jsonify({'pie ingredients': random.choice(ingredients) })