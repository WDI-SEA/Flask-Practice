from flask import Flask, render_template, jsonify, redirect, request
import random

app = Flask(__name__)

ingredients = ['apples', 'milk', 'dough', 'sugar', 'butts']

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


@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    global ingredients
    if request.method == 'POST':
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)
        return redirect('/recipe')
    else:
        return render_template('recipe.html', ingredients=ingredients)