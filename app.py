from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/greeting')
def greeting():
    return render_template('index.html', name="Constance")

ingredients = ['Milk', 'Butter', 'Eggs', 'Flour', 'Ground beef', 'Potatoes']

@app.route('/pie')
def pie():
    global ingredients
    random.shuffle(ingredients)
    for i in ingredients:
        return jsonify({'pie ingredient': i})
    
        