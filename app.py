from flask import Flask, render_template, jsonify, redirect, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/greeting')
def hello():
    return render_template('index.html', name='Akilah')

ingredients = [
    {'apple_pie' : ['apples', 'sugar', 'flour']},
    {'banana_pie' : ['bananas', 'sugar', 'flour']}
]

@app.route('/pie')
def pie():
    return jsonify(random.choice(ingredients))

@app.route('/recipe')
def recipe():
    return render_template('recipe.html', ingredients=ingredients)
